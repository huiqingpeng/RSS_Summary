"""RSS Fetcher Module - Fetches articles from RSS/Atom feeds."""

import feedparser
import logging
import os
from datetime import datetime, timedelta
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)


class RSSFetcher:
    """Fetches articles from RSS feeds."""

    def __init__(self, sources: List[Dict], seen_urls: set, max_days_back: int = 0):
        """
        Initialize the RSS fetcher.

        Args:
            sources: List of source dictionaries with 'name', 'slug', 'url', 'category'
            seen_urls: Set of URLs already processed
            max_days_back: Maximum days back to fetch (0 = no limit)
        """
        self.sources = sources
        self.seen_urls = seen_urls
        self.max_days_back = max_days_back

    def fetch_all(self) -> List[Dict]:
        """
        Fetch new articles from all sources.

        Returns:
            List of article dictionaries with metadata
        """
        all_articles = []

        for source in self.sources:
            articles = self._fetch_source(source)
            all_articles.extend(articles)

        logger.info(f"Fetched {len(all_articles)} new articles from {len(self.sources)} sources")
        return all_articles

    def _fetch_source(self, source: Dict) -> List[Dict]:
        """
        Fetch articles from a single source.

        Args:
            source: Source dictionary

        Returns:
            List of new article dictionaries
        """
        source_name = source.get('name', 'Unknown')
        source_slug = source.get('slug', 'unknown')
        source_url = source.get('url', '')
        source_category = source.get('category', 'unknown')

        logger.info(f"Fetching feed: {source_name}")

        try:
            feed = feedparser.parse(source_url)

            if feed.bozo and not feed.entries:
                logger.warning(f"Failed to parse feed: {source_name} - {feed.bozo_exception}")
                return []

            # Calculate cutoff date
            cutoff_date = None
            if self.max_days_back > 0:
                cutoff_date = datetime.now() - timedelta(days=self.max_days_back)

            articles = []
            for entry in feed.entries:
                url = self._get_entry_url(entry)

                # Skip if already processed
                if url in self.seen_urls:
                    continue

                # Parse published date
                published = self._parse_date(entry)

                # Skip if outside date range
                if cutoff_date:
                    try:
                        article_date = datetime.strptime(published, '%Y-%m-%d')
                        if article_date < cutoff_date:
                            continue
                    except ValueError:
                        pass

                article = {
                    'title': entry.get('title', 'Untitled'),
                    'url': url,
                    'published': published,
                    'source_name': source_name,
                    'source_slug': source_slug,
                    'source_category': source_category,
                    'summary': entry.get('summary', ''),
                }
                articles.append(article)

            logger.info(f"Found {len(articles)} new articles from {source_name}")
            return articles

        except Exception as e:
            logger.error(f"Error fetching {source_name}: {e}")
            return []

    def _get_entry_url(self, entry) -> str:
        """Extract the canonical URL from an entry."""
        # Try multiple sources for the URL
        if hasattr(entry, 'link'):
            return entry.link

        # Check for href in links array
        if hasattr(entry, 'links'):
            for link in entry.links:
                if link.get('rel') == 'alternate' or link.get('type', '').startswith('text/html'):
                    return link.get('href', '')

        # Fallback to id
        return entry.get('id', '')

    def _parse_date(self, entry) -> Optional[str]:
        """Parse the published date from an entry."""
        if hasattr(entry, 'published_parsed') and entry.published_parsed:
            try:
                dt = datetime(*entry.published_parsed[:6])
                return dt.strftime('%Y-%m-%d')
            except Exception:
                pass

        if hasattr(entry, 'updated_parsed') and entry.updated_parsed:
            try:
                dt = datetime(*entry.updated_parsed[:6])
                return dt.strftime('%Y-%m-%d')
            except Exception:
                pass

        return datetime.now().strftime('%Y-%m-%d')