---
title: "China issues second warning on OpenClaw risks amid adoption frenzy"
source: "SCMP Business"
url: "https://www.scmp.com/tech/tech-trends/article/3346138/china-issues-second-warning-openclaw-risks-amid-adoption-frenzy?utm_source=rss_feed"
published: "2026-03-10"
summarized: "2026-03-11T09:08:23.825369"
ai_provider: "openai"
---

【是什么 / What it is】
中国网络安全机构 CNCERT 于本周二第二次发布警告，指出 AI 智能体 OpenClaw 存在严重的安全与数据风险。OpenClaw 是由奥地利开发者 Peter Steinberger 于去年年底发布的软件，能够自主执行邮件处理、报告撰写、幻灯片制作等任务，目前在中国正被地方政府和科技企业广泛采用。

China's cybersecurity agency CNCERT issued its second warning on Tuesday about serious security and data risks associated with the AI agent OpenClaw. OpenClaw, released by Austrian developer Peter Steinberger late last year, is software capable of autonomously performing tasks such as organizing emails, drafting reports, and preparing slide decks, and is currently being widely adopted by local governments and tech companies in China.

---

【为什么重要 / Why it matters】
OpenClaw 的自主任务执行能力需要高级系统权限，这使其面临"提示词注入"攻击（攻击者通过网页隐藏恶意指令窃取系统密钥）和"操作错误"（误删关键数据）等双重威胁。在中国各地掀起 AI 应用热潮、云服务商大力推广快速部署之际，这一警告揭示了技术便利性与安全性之间的深层矛盾，对企业数据治理和国家网络安全具有重要警示意义。

OpenClaw's autonomous task execution requires high-level system permissions, exposing it to dual threats of "prompt injection" attacks (where hidden malicious instructions on webpages steal system keys) and "operational errors" (accidental deletion of critical data). This warning highlights the fundamental tension between technological convenience and security at a time of nationwide AI adoption frenzy and aggressive cloud service promotion, carrying significant implications for enterprise data governance and national cybersecurity.

---

【我能用什么 / How I can use it】
在评估或部署 AI Agent 类工具时，应优先审查其权限最小化配置、输入过滤机制和数据操作日志功能，避免直接赋予系统级访问权限。可参考 CNCERT 的风险分类建立内部安全评估框架，将"提示词注入"防护和"操作边界"设定纳入 AI 应用准入标准，同时制定人机协同的确认机制以防止自主误操作。

When evaluating or deploying AI agent tools, prioritize reviewing their least-privilege configuration, input filtering mechanisms, and data operation logging capabilities, avoiding direct system-level access grants. Consider establishing an internal security assessment framework referencing CNCERT's risk categories, incorporating "prompt injection" protection and "operational boundary" settings into AI application admission standards, while implementing human-in-the-loop confirmation mechanisms to prevent autonomous misoperations.
