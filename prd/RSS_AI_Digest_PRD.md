# RSS AI Digest — 项目需求文档 (PRD)

**版本**: v1.0  
**日期**: 2026-03-10  
**项目名称**: RSS AI Digest — 自动拉取 · AI 提炼 · 静态发布

---

## 一、项目背景与目标

在信息爆炸的时代，手动追踪多个技术博客、AI 前沿、财经资讯的成本极高。本项目旨在构建一套**全自动的信息消化管道**，部署在 Jetson Nano Orin（或任意 Ubuntu 主机）上，定时拉取订阅源的完整文章，喂给 AI 接口生成结构化双语笔记，并自动发布到 GitHub Pages 静态网站，供随时随地浏览回顾。

**核心价值**: 把"泛读"变成"精读摘要存档"，形成个人知识库。

---

## 二、系统架构总览

```
[Jetson Nano Orin / Ubuntu 本机]
        │
        │  cron 每 6 小时触发
        ▼
┌─────────────────────────────┐
│   1. RSS 拉取模块            │  feedparser
│   2. 正文抓取模块            │  trafilatura
│   3. 去重模块               │  seen.json
│   4. AI 总结模块            │  Claude API / OpenAI API（可切换）
│   5. 文件归档模块            │  按年/月/日写入 Markdown
│   6. Git Push 模块          │  推送到 GitHub 仓库
└─────────────────────────────┘
        │
        │  GitHub Actions 检测到 push
        ▼
[GitHub Pages]
  静态网站 — 按日期浏览 + 按来源筛选
```

---

## 三、运行环境

| 项目 | 说明 |
|------|------|
| 主机 | Jetson Nano Orin 或任意 Ubuntu 20.04+ |
| 语言 | Python 3.9+ |
| 触发方式 | crontab，每 6 小时执行一次 |
| 网络要求 | 能访问 RSS 源 URL 及 AI API 端点 |
| 存储 | 本地 Git 仓库，push 到 GitHub |

---

## 四、RSS 订阅源配置

所有订阅源统一维护在 `config/sources.yaml`，支持随时增删。

### 4.1 当前订阅列表

#### 嵌入式系统与底层开发
| 名称 | RSS URL |
|------|---------|
| CNX Software | https://www.cnx-software.com/feed/ |
| Bootlin Blog | https://bootlin.com/blog/feed/ |
| Hackaday | https://hackaday.com/blog/feed/ |
| NVIDIA Developer Blog | https://developer.nvidia.com/blog/feed/ |

#### 人工智能与 LLM 前沿
| 名称 | RSS URL |
|------|---------|
| Hugging Face Blog | https://huggingface.co/blog/feed.xml |
| HuggingFace Daily Papers | https://rsshub.app/huggingface/daily-papers |
| The Pragmatic Engineer | https://newsletter.pragmaticengineer.com/feed |

#### 技术视野与团队领导力
| 名称 | RSS URL |
|------|---------|
| Will Larson (StaffEng) | https://lethain.com/feeds/ |

#### 宏观周期与财务投资
| 名称 | RSS URL |
|------|---------|
| SCMP Business | https://www.scmp.com/rss/91/feed |

#### 科学健康与生活方式
| 名称 | RSS URL |
|------|---------|
| Examine.com | https://examine.com/feed/ |
| Sprudge | https://sprudge.com/feed/ |
| Perfect Daily Grind | https://perfectdailygrind.com/feed/ |

### 4.2 特殊说明
- **The Batch (DeepLearning.AI)** 及 **Ray Dalio** 为邮件 Newsletter，建议通过 [Kill the Newsletter!](https://kill-the-newsletter.com) 转换为 RSS 后加入配置。
- Substack 专栏（如 Pragmatic Engineer）在 URL 末尾加 `/feed` 即可直接使用。

---

## 五、核心功能模块详述

### 5.1 RSS 拉取模块

- 依赖：`feedparser`
- 行为：
  - 遍历 `config/sources.yaml` 中所有源
  - 拉取每条 feed 的最新条目列表（entry list）
  - 提取：标题、原文链接、发布时间、来源名称
  - 与 `data/seen.json` 比对，**跳过已处理的文章**（以 URL 为唯一标识）
- 输出：待处理文章列表（含元数据）

### 5.2 正文抓取模块

- 依赖：`trafilatura`（专为文章正文提取优化，自动去除导航栏、广告、评论区等噪音）
- 行为：
  - 对每篇新文章，请求原始 URL
  - 提取纯文本正文（保留段落结构）
  - 若抓取失败（如反爬、付费墙），记录 `failed` 状态，跳过不处理
- 输出：文章正文字符串

### 5.3 去重模块

- 文件：`data/seen.json`
- 结构：
  ```json
  {
    "https://example.com/article-1": {
      "processed_at": "2026-03-10T08:00:00",
      "status": "success"
    }
  }
  ```
- 每次成功处理后写入，防止重复 AI 调用产生费用

### 5.4 AI 总结模块

- 支持两个 Provider，通过配置文件切换：
  - **Claude API**（Anthropic）
  - **OpenAI API**（GPT-4o 等）
- 输入：文章标题 + 正文全文
- Prompt 模板（中英双语三段式）：

```
你是一位专业的技术知识提炼助手。请阅读以下文章，并按照以下结构输出笔记，每段同时提供中文和英文：

【是什么 / What it is】
用 2-3 句话描述这篇文章的核心主题和背景。

【为什么重要 / Why it matters】
用 2-3 句话解释这件事的意义、影响或趋势价值。

【我能用什么 / How I can use it】
用 2-3 句话给出具体的行动建议、应用场景或延伸方向。

---文章内容如下---
{article_content}
```

- 输出格式：结构化 Markdown 文本

### 5.5 文件归档模块

所有文件按 **年/月/日** 目录层级存储，文件名格式为 `{来源slug}_{文章标题slug}.md`。

#### 目录结构
```
repo/
├── articles/               # 原始文章存档
│   └── 2026/
│       └── 03/
│           └── 10/
│               ├── cnx-software_jetson-orin-nx-review.md
│               └── hackaday_new-risc-v-board.md
│
├── summaries/              # AI 总结笔记
│   └── 2026/
│       └── 03/
│           └── 10/
│               ├── cnx-software_jetson-orin-nx-review.md
│               └── hackaday_new-risc-v-board.md
│
├── data/
│   └── seen.json           # 去重记录
│
├── config/
│   └── sources.yaml        # RSS 源配置
│
├── scripts/
│   └── fetch_and_summarize.py
│
└── docs/                   # GitHub Pages 网站源文件
    ├── index.html
    └── assets/
```

#### 原始文章 Markdown 格式
```markdown
---
title: "文章标题"
source: "CNX Software"
url: "https://原文链接"
published: "2026-03-10"
fetched: "2026-03-10T08:23:00"
---

（正文内容）
```

#### AI 总结 Markdown 格式
```markdown
---
title: "文章标题"
source: "CNX Software"
url: "https://原文链接"
published: "2026-03-10"
summarized: "2026-03-10T08:23:45"
ai_provider: "claude"
---

## 是什么 / What it is

（中文）...

(English) ...

## 为什么重要 / Why it matters

（中文）...

(English) ...

## 我能用什么 / How I can use it

（中文）...

(English) ...
```

### 5.6 Git Push 模块

- 每次运行结束后，自动执行：
  ```bash
  git add .
  git commit -m "digest: YYYY-MM-DD HH:MM — N articles processed"
  git push origin main
  ```
- Push 触发 GitHub Actions，自动重建 GitHub Pages 网站

---

## 六、GitHub Pages 网站

### 6.1 页面结构

| 页面 | 路径 | 内容 |
|------|------|------|
| 首页 | `/` | 最新笔记列表，按日期倒序 |
| 日期页 | `/2026/03/10/` | 当天所有笔记 |
| 文章详情页 | `/2026/03/10/cnx-software_xxx/` | 单篇 AI 笔记 + 原文链接 |

### 6.2 首页功能

- 笔记卡片列表，按日期倒序排列
- 顶部提供**来源筛选**下拉/按钮（CNX Software / Hackaday / HuggingFace 等）
- 每张卡片显示：
  - 文章标题（可点击跳转原文）
  - 来源名称 + 发布日期
  - AI 三段式笔记（中英双语完整展示）

### 6.3 技术选型

- **构建方式**：GitHub Actions 触发 Python 脚本，将 `summaries/` 目录下的 Markdown 渲染为 HTML
- **样式**：纯 HTML + CSS（无框架依赖，轻量，适合静态托管）
- **搜索/筛选**：前端 JavaScript 实现，无需后端

---

## 七、配置文件设计

### config/sources.yaml
```yaml
sources:
  - name: "CNX Software"
    slug: "cnx-software"
    url: "https://www.cnx-software.com/feed/"
    category: "embedded"
    
  - name: "Hackaday"
    slug: "hackaday"
    url: "https://hackaday.com/blog/feed/"
    category: "embedded"

  - name: "Hugging Face Blog"
    slug: "huggingface"
    url: "https://huggingface.co/blog/feed.xml"
    category: "ai"
```

### config/settings.yaml
```yaml
ai:
  provider: "claude"          # "claude" 或 "openai"
  model_claude: "claude-opus-4-6"
  model_openai: "gpt-4o"
  max_tokens: 1000
  language: "bilingual"       # 中英双语

schedule:
  interval_hours: 6

storage:
  seen_file: "data/seen.json"
  articles_dir: "articles"
  summaries_dir: "summaries"

git:
  auto_push: true
  remote: "origin"
  branch: "main"
```

---

## 八、定时任务配置

### crontab 设置
```bash
# 每 6 小时执行一次：0:00, 6:00, 12:00, 18:00
0 0,6,12,18 * * * /usr/bin/python3 /home/user/rss-digest/scripts/fetch_and_summarize.py >> /var/log/rss-digest.log 2>&1
```

---

## 九、GitHub Actions 配置

文件路径：`.github/workflows/deploy.yml`

```yaml
name: Deploy GitHub Pages

on:
  push:
    branches: [main]

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Build static site
        run: python scripts/build_site.py
      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs
```

---

## 十、异常处理策略

| 场景 | 处理方式 |
|------|---------|
| RSS 源无法访问 | 跳过该源，记录日志，不影响其他源 |
| 正文抓取失败（反爬/付费墙） | 标记 `status: failed`，写入 seen.json，不调用 AI |
| AI API 超时或报错 | 最多重试 2 次，仍失败则跳过，记录日志 |
| Git Push 失败 | 本地文件已保存，下次运行时会再次尝试 push |
| 文章过长超出 Token 限制 | 截取前 8000 字符后送入 AI |

---

## 十一、依赖清单

```
# Python 依赖
feedparser>=6.0
trafilatura>=1.6
anthropic>=0.25          # Claude API
openai>=1.0              # OpenAI API
pyyaml>=6.0
requests>=2.31
python-slugify>=8.0
jinja2>=3.1              # 网站模板渲染
```

---

## 十二、项目文件结构（完整）

```
rss-digest/
├── README.md
├── requirements.txt
├── config/
│   ├── sources.yaml
│   └── settings.yaml
├── scripts/
│   ├── fetch_and_summarize.py   # 主脚本
│   ├── rss_fetcher.py           # RSS 拉取模块
│   ├── article_extractor.py     # 正文抓取模块
│   ├── ai_summarizer.py         # AI 总结模块
│   ├── file_archiver.py         # 文件归档模块
│   └── build_site.py            # 静态网站构建脚本
├── data/
│   └── seen.json
├── articles/                    # 原始文章（按年/月/日）
├── summaries/                   # AI 笔记（按年/月/日）
├── docs/                        # GitHub Pages 输出
│   ├── index.html
│   └── assets/
│       ├── style.css
│       └── filter.js
└── .github/
    └── workflows/
        └── deploy.yml
```

---

## 十三、开发阶段规划

| 阶段 | 内容 | 优先级 |
|------|------|--------|
| Phase 1 | 核心脚本：RSS 拉取 + 正文抓取 + 去重 | 🔴 必须 |
| Phase 2 | AI 总结模块（Claude/OpenAI 双支持） | 🔴 必须 |
| Phase 3 | 文件归档 + Git 自动 Push | 🔴 必须 |
| Phase 4 | GitHub Pages 静态网站 + GitHub Actions | 🟠 高优 |
| Phase 5 | 来源筛选、搜索功能 | 🟡 迭代 |
| Phase 6 | 邮件/Telegram 通知（可选扩展） | 🟢 未来 |

---

*文档由对话需求梳理自动生成，确认后即可进入代码实现阶段。*
