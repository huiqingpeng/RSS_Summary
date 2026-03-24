---
title: "Putnam 2025 Problems in Rocq using Opus 4.6 and Rocq-MCP"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20405"
published: "2026-03-24"
summarized: "2026-03-25T07:08:56.209579"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究报告了Claude Opus 4.6配备Rocq证明助手的Model Context Protocol（MCP）工具套件后，在2025年普特南数学竞赛中自主证明了12道题中的10道。MCP工具采用"先编译、后交互回退"策略，由Claude通过分析先前miniF2F-Rocq实验的日志设计而成。该实验在隔离虚拟机环境下运行，部署了141个子代理，消耗约19亿token，所有证明均已公开。

【方法概述 / Method】
研究团队开发了一套MCP工具，使大语言模型能够与Rocq证明助手交互，核心策略为优先尝试自动编译证明，失败时回退到交互式证明模式。该工具设计基于对先前实验日志的分析，实现了无互联网访问环境下的自主定理证明。

【实验结果 / Results】
系统在2025年普特南竞赛12道题目中成功证明10道，运行总时长17.7小时（ wall-clock时间51.6小时），共部署141个子代理，消耗约19亿token。所有生成的证明均经过验证并可公开获取。

【应用价值 / Applications】
该研究展示了大型语言模型结合形式化证明助手在高级数学竞赛中的自主解题能力，为自动化数学研究、形式化验证和教育辅助工具开发提供了新思路。MCP工具框架可推广至其他证明助手和数学推理场景，推动AI辅助形式化数学的发展。
