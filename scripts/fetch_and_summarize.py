#!/usr/bin/env python3
"""RSS AI Digest - Main entry point for fetching and summarizing RSS articles.

This script orchestrates the entire pipeline:
1. Fetch RSS feeds
2. Extract article content
3. Generate AI summaries
4. Archive files
5. Push to GitHub
"""

import argparse
import logging
import os
import subprocess
import sys
import yaml
from datetime import datetime
from typing import Dict, List

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from rss_fetcher import RSSFetcher
from article_extractor import ArticleExtractor
from ai_summarizer import AISummarizer
from file_archiver import FileArchiver


def setup_logging(level: str = "INFO"):
    """Setup logging configuration."""
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('rss-digest.log')
        ]
    )


def load_config() -> Dict:
    """Load configuration from YAML files."""
    config_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config')

    # Load sources
    sources_file = os.path.join(config_dir, 'sources.yaml')
    with open(sources_file, 'r', encoding='utf-8') as f:
        sources_data = yaml.safe_load(f)

    # Load settings
    settings_file = os.path.join(config_dir, 'settings.yaml')
    with open(settings_file, 'r', encoding='utf-8') as f:
        settings_data = yaml.safe_load(f)

    # Load sensitive API config (if exists)
    api_keys_file = os.path.join(config_dir, 'api_keys.yaml')
    api_keys_data = {}
    if os.path.exists(api_keys_file):
        with open(api_keys_file, 'r', encoding='utf-8') as f:
            api_keys_data = yaml.safe_load(f) or {}

    # Merge AI config: settings + sensitive api_keys
    ai_config = {**settings_data.get('ai', {}), **api_keys_data.get('ai', {})}

    return {
        'sources': sources_data.get('sources', []),
        'ai': ai_config,
        'storage': settings_data.get('storage', {}),
        'git': settings_data.get('git', {}),
        'retry': settings_data.get('retry', {}),
        'content': settings_data.get('content', {}),
        'fetch': settings_data.get('fetch', {}),
    }


def git_push(config: Dict):
    """Push changes to GitHub."""
    if not config.get('auto_push', True):
        logging.info("Auto-push disabled, skipping git push")
        return

    try:
        # Add all changes
        subprocess.run(['git', 'add', '-A'], check=True, capture_output=True)

        # Check if there are changes
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        if not result.stdout.strip():
            logging.info("No changes to commit")
            return

        # Commit with timestamp
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        commit_msg = f"digest: {timestamp} — automated update"

        subprocess.run(['git', 'commit', '-m', commit_msg], check=True, capture_output=True)

        # Push
        branch = config.get('branch', 'main')
        remote = config.get('remote', 'origin')
        subprocess.run(['git', 'push', remote, branch], check=True, capture_output=True)

        logging.info("Successfully pushed to GitHub")

    except subprocess.CalledProcessError as e:
        logging.error(f"Git push failed: {e.stderr.decode() if e.stderr else str(e)}")
    except Exception as e:
        logging.error(f"Error during git push: {e}")


def process_article(article: Dict, extractor: ArticleExtractor, summarizer: AISummarizer,
                    archiver: FileArchiver, config: Dict) -> bool:
    """
    Process a single article: extract content and generate summary.

    Args:
        article: Article metadata
        extractor: Article extractor instance
        summarizer: AI summarizer instance
        archiver: File archiver instance
        config: Configuration dictionary

    Returns:
        True if successfully processed, False otherwise
    """
    url = article['url']
    title = article['title']

    logging.info(f"Processing: {title}")

    # Extract article content
    extracted = extractor.extract(url)

    if extracted is None:
        logging.warning(f"Failed to extract content from {url}, marking as failed")
        archiver.mark_seen(url, 'failed')
        return False

    # Archive original article
    try:
        archiver.archive_article(article, extracted['text'])
    except Exception as e:
        logging.error(f"Failed to archive article: {e}")

    # Generate AI summary
    summary = summarizer.summarize(title, extracted['text'])

    if summary is None:
        logging.warning(f"Failed to generate summary for {url}, marking as failed")
        archiver.mark_seen(url, 'failed')
        return False

    # Archive summary
    try:
        archiver.archive_summary(article, summary, config['ai'].get('provider', 'claude'))
    except Exception as e:
        logging.error(f"Failed to archive summary: {e}")
        archiver.mark_seen(url, 'failed')
        return False

    # Mark as seen
    archiver.mark_seen(url, 'success')

    logging.info(f"Successfully processed: {title}")
    return True


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description='RSS AI Digest - Fetch and summarize RSS articles')
    parser.add_argument('--dry-run', action='store_true', help='Dry run, do not push to GitHub')
    parser.add_argument('--log-level', default='INFO', help='Logging level')
    parser.add_argument('--max-articles', type=int, default=0, help='Maximum articles to process per run (0 = no limit)')
    args = parser.parse_args()

    setup_logging(args.log_level)
    logger = logging.getLogger(__name__)

    logger.info("=" * 50)
    logger.info("RSS AI Digest - Starting run")
    logger.info("=" * 50)

    # Load configuration
    try:
        config = load_config()
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        sys.exit(1)

    # Initialize components
    archiver = FileArchiver(config['storage'])

    # Load seen URLs
    seen_urls = archiver.load_seen()
    logger.info(f"Loaded {len(seen_urls)} seen URLs")

    # Fetch RSS feeds
    max_days_back = config.get('fetch', {}).get('max_days_back', 0)
    fetcher = RSSFetcher(config['sources'], seen_urls, max_days_back=max_days_back)
    articles = fetcher.fetch_all()

    if not articles:
        logger.info("No new articles found")
        sys.exit(0)

    # Limit articles (0 = no limit)
    if args.max_articles > 0:
        articles = articles[:args.max_articles]
    logger.info(f"Processing up to {len(articles)} articles")

    # Initialize extractor and summarizer
    extractor = ArticleExtractor(
        timeout=config.get('retry', {}).get('timeout_seconds', 30),
        retry_count=config.get('retry', {}).get('max_attempts', 2)
    )

    # Merge config for summarizer
    summarizer_config = {
        **config['ai'],
        'max_chars': config.get('content', {}).get('max_chars_for_ai', 8000)
    }

    try:
        summarizer = AISummarizer(summarizer_config)
    except Exception as e:
        logger.error(f"Failed to initialize AI summarizer: {e}")
        sys.exit(1)

    # Process articles
    success_count = 0
    for article in articles:
        try:
            if process_article(article, extractor, summarizer, archiver, config):
                success_count += 1
        except Exception as e:
            logger.error(f"Error processing article: {e}")
            continue

    logger.info(f"Successfully processed {success_count}/{len(articles)} articles")

    # Git push
    if not args.dry_run:
        git_push(config['git'])
    else:
        logger.info("Dry run - skipping git push")

    logger.info("=" * 50)
    logger.info("RSS AI Digest - Run complete")
    logger.info("=" * 50)


if __name__ == '__main__':
    main()