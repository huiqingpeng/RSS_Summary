"""File Archiver Module - Archives articles and summaries to markdown files."""

import os
import json
import logging
from datetime import datetime
from typing import Dict, Optional
from slugify import slugify

logger = logging.getLogger(__name__)


class FileArchiver:
    """Archives articles and summaries to markdown files."""

    def __init__(self, config: Dict):
        """
        Initialize the file archiver.

        Args:
            config: Configuration with 'articles_dir', 'summaries_dir', 'seen_file'
        """
        self.articles_dir = config.get('articles_dir', 'articles')
        self.summaries_dir = config.get('summaries_dir', 'summaries')
        self.seen_file = config.get('seen_file', 'data/seen.json')

    def archive_article(self, article: Dict, content: str) -> str:
        """
        Archive the original article.

        Args:
            article: Article metadata dictionary
            content: Article text content

        Returns:
            Path to the archived file
        """
        date = article.get('published', datetime.now().strftime('%Y-%m-%d'))
        year, month, day = date.split('-')

        source_slug = article.get('source_slug', 'unknown')
        title_slug = slugify(article.get('title', 'untitled'))[:50]

        filename = f"{source_slug}_{title_slug}.md"
        filepath = os.path.join(self.articles_dir, year, month, day, filename)

        # Create directory if needed
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Build markdown content
        markdown = self._build_article_markdown(article, content)

        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)

        logger.info(f"Archived article to {filepath}")
        return filepath

    def archive_summary(self, article: Dict, summary: str, ai_provider: str) -> str:
        """
        Archive the AI summary.

        Args:
            article: Article metadata dictionary
            summary: AI summary text
            ai_provider: AI provider used ('claude' or 'openai')

        Returns:
            Path to the archived file
        """
        date = article.get('published', datetime.now().strftime('%Y-%m-%d'))
        year, month, day = date.split('-')

        source_slug = article.get('source_slug', 'unknown')
        title_slug = slugify(article.get('title', 'untitled'))[:50]

        filename = f"{source_slug}_{title_slug}.md"
        filepath = os.path.join(self.summaries_dir, year, month, day, filename)

        # Create directory if needed
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Build markdown content
        markdown = self._build_summary_markdown(article, summary, ai_provider)

        # Write file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)

        logger.info(f"Archived summary to {filepath}")
        return filepath

    def mark_seen(self, url: str, status: str = 'success'):
        """
        Mark a URL as seen in seen.json.

        Args:
            url: Article URL
            status: Processing status ('success' or 'failed')
        """
        seen_data = {}

        # Load existing data
        if os.path.exists(self.seen_file):
            try:
                with open(self.seen_file, 'r', encoding='utf-8') as f:
                    seen_data = json.load(f)
            except json.JSONDecodeError:
                seen_data = {}

        # Add/update entry
        seen_data[url] = {
            'processed_at': datetime.now().isoformat(),
            'status': status
        }

        # Save
        os.makedirs(os.path.dirname(self.seen_file), exist_ok=True)
        with open(self.seen_file, 'w', encoding='utf-8') as f:
            json.dump(seen_data, f, ensure_ascii=False, indent=2)

    def load_seen(self) -> set:
        """
        Load seen URLs from seen.json.

        Returns:
            Set of seen URLs
        """
        if not os.path.exists(self.seen_file):
            return set()

        try:
            with open(self.seen_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return set(data.keys())
        except (json.JSONDecodeError, IOError):
            return set()

    def _build_article_markdown(self, article: Dict, content: str) -> str:
        """Build markdown for original article."""
        return f"""---
title: "{article.get('title', 'Untitled')}"
source: "{article.get('source_name', 'Unknown')}"
url: "{article.get('url', '')}"
published: "{article.get('published', '')}"
fetched: "{datetime.now().isoformat()}"
---

{content}
"""

    def _build_summary_markdown(self, article: Dict, summary: str, ai_provider: str) -> str:
        """Build markdown for AI summary."""
        return f"""---
title: "{article.get('title', 'Untitled')}"
source: "{article.get('source_name', 'Unknown')}"
url: "{article.get('url', '')}"
published: "{article.get('published', '')}"
summarized: "{datetime.now().isoformat()}"
ai_provider: "{ai_provider}"
---

{summary}
"""