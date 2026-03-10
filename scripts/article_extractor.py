"""Article Extractor Module - Extracts article content using trafilatura."""

import logging
import trafilatura
from typing import Optional, Dict
import time

logger = logging.getLogger(__name__)


class ArticleExtractor:
    """Extracts article content from URLs."""

    def __init__(self, timeout: int = 30, retry_count: int = 2):
        """
        Initialize the article extractor.

        Args:
            timeout: Timeout for HTTP requests in seconds
            retry_count: Number of retries on failure
        """
        self.timeout = timeout
        self.retry_count = retry_count

    def extract(self, url: str) -> Optional[Dict]:
        """
        Extract article content from URL.

        Args:
            url: Article URL

        Returns:
            Dictionary with 'content' and 'text' keys, or None on failure
        """
        for attempt in range(self.retry_count):
            try:
                # Extract content using trafilatura
                result = trafilatura.fetch_url(url)

                if not result:
                    logger.warning(f"No content retrieved from {url}")
                    if attempt < self.retry_count - 1:
                        time.sleep(1)
                        continue
                    return None

                # Extract text content
                text = trafilatura.extract(
                    result,
                    output_format='txt',
                    include_comments=False,
                    include_tables=True,
                    deduplicate=False
                )

                if not text or len(text.strip()) < 100:
                    logger.warning(f"Extracted content too short from {url}")
                    if attempt < self.retry_count - 1:
                        time.sleep(1)
                        continue
                    return None

                logger.info(f"Successfully extracted {len(text)} chars from {url}")
                return {
                    'content': text,
                    'text': text,
                    'url': url
                }

            except Exception as e:
                logger.error(f"Error extracting {url} (attempt {attempt + 1}/{self.retry_count}): {e}")
                if attempt < self.retry_count - 1:
                    time.sleep(1)
                    continue

        return None