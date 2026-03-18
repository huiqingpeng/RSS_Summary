"""AI Summarizer Module - Summarizes articles using Claude or OpenAI API."""

import logging
import os
from typing import Optional, Dict

logger = logging.getLogger(__name__)

# Try importing the API clients
try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


SUMMARIZE_PROMPT = """你是一位专业的技术知识提炼助手。请阅读以下文章，并按照以下结构输出笔记，每段同时提供中文和英文：

【是什么 / What it is】
用 2-3 句话描述这篇文章的核心主题和背景。

【为什么重要 / Why it matters】
用 2-3 句话解释这件事的意义、影响或趋势价值。

【我能用什么 / How I can use it】
用 2-3 句话给出具体的行动建议、应用场景或延伸方向。

---文章内容如下---
{content}
"""

# 学术论文专用的提示词 - 更适合 arXiv 论文结构
SUMMARIZE_PROMPT_PAPER = """你是一位专业的学术论文解读助手。请阅读以下学术论文，并按照以下结构输出笔记：

【论文摘要 / Abstract】
用 3-4 句话概括论文的核心贡献和主要发现。

【方法概述 / Method】
用 2-3 句话描述论文采用的方法或技术方案。

【实验结果 / Results】
用 2-3 句话总结关键实验结果或性能指标。

【应用价值 / Applications】
用 2-3 句话说明该研究的实际应用场景和价值。

---论文内容如下---
{content}
"""


class AISummarizer:
    """Summarizes articles using AI."""

    def __init__(self, config: Dict):
        """
        Initialize the AI summarizer.

        Args:
            config: Configuration dictionary with 'provider', 'model', 'api_key', 'max_tokens'
        """
        self.provider = config.get('provider', 'claude')
        self.max_tokens = config.get('max_tokens', 1000)
        self.max_chars = config.get('max_chars', 8000)

        # Get API key from config or environment
        api_key = config.get('api_key', '')

        if self.provider == 'claude':
            if not api_key:
                api_key = os.environ.get('ANTHROPIC_API_KEY', '')
            if not api_key:
                raise ValueError("Claude API key not provided. Set ANTHROPIC_API_KEY environment variable or api_key in settings.yaml")

            if not ANTHROPIC_AVAILABLE:
                raise ImportError("anthropic package not installed. Run: pip install anthropic")

            self.client = anthropic.Anthropic(api_key=api_key)
            self.model = config.get('model_claude', 'claude-opus-4-6')

        elif self.provider == 'openai':
            if not api_key:
                api_key = os.environ.get('OPENAI_API_KEY', '')
            if not api_key:
                raise ValueError("OpenAI API key not provided. Set OPENAI_API_KEY environment variable or api_key in settings.yaml")

            if not OPENAI_AVAILABLE:
                raise ImportError("openai package not installed. Run: pip install openai")

            # Support custom API base URL (e.g., for Alibaba DashScope)
            base_url = config.get('api_base_url', '')
            if base_url:
                self.client = OpenAI(api_key=api_key, base_url=base_url)
            else:
                self.client = OpenAI(api_key=api_key)

            self.model = config.get('model_openai', 'gpt-4o')

        else:
            raise ValueError(f"Unknown AI provider: {self.provider}")

    def summarize(self, title: str, content: str, category: str = None) -> Optional[str]:
        """
        Summarize an article.

        Args:
            title: Article title
            content: Article text content
            category: Source category (e.g., 'academic' for papers)

        Returns:
            Summarized text or None on failure
        """
        # Select prompt based on category
        if category == 'academic':
            prompt_template = SUMMARIZE_PROMPT_PAPER
        else:
            prompt_template = SUMMARIZE_PROMPT

        # Truncate content if too long
        if len(content) > self.max_chars:
            content = content[:self.max_chars] + "\n\n[Content truncated...]"

        try:
            if self.provider == 'claude':
                return self._summarize_claude(title, content, prompt_template)
            elif self.provider == 'openai':
                return self._summarize_openai(title, content, prompt_template)

        except Exception as e:
            logger.error(f"Error summarizing article '{title}': {e}")
            return None

    def _summarize_claude(self, title: str, content: str, prompt_template: str) -> str:
        """Summarize using Claude API."""
        message = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            messages=[
                {
                    "role": "user",
                    "content": prompt_template.format(content=f"标题: {title}\n\n{content}")
                }
            ]
        )

        return message.content[0].text

    def _summarize_openai(self, title: str, content: str, prompt_template: str) -> str:
        """Summarize using OpenAI API."""
        response = self.client.chat.completions.create(
            model=self.model,
            max_tokens=self.max_tokens,
            messages=[
                {
                    "role": "user",
                    "content": prompt_template.format(content=f"标题: {title}\n\n{content}")
                }
            ]
        )

        return response.choices[0].message.content