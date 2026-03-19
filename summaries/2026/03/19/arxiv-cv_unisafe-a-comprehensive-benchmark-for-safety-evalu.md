---
title: "UniSAFE: A Comprehensive Benchmark for Safety Evaluation of Unified Multimodal Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17476"
published: "2026-03-19"
summarized: "2026-03-19T15:11:47.127771"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了UniSAFE，首个针对统一多模态模型（UMMs）进行系统级安全评估的综合基准测试。该基准涵盖7种输入/输出模态组合，包含传统任务和新型多模态上下文图像生成场景，共6,802个精选实例。通过对15个最先进的UMM（包括专有和开源模型）的评估，研究发现当前UMM存在严重安全漏洞，特别是在多图像组合和多轮对话设置中，且图像输出任务比文本输出任务更易受攻击。

【方法概述 / Method】
UniSAFE采用共享目标设计（shared-target design），将共同风险场景投影到特定任务的输入/输出配置中，实现跨任务安全故障的受控比较。该基准系统性地覆盖了7种I/O模态组合，包括文本、图像的多种输入输出排列，以及多模态上下文图像生成等新兴任务场景。

【实验结果 / Results】
评估揭示了当前UMM的关键脆弱性：多图像合成场景和多轮交互设置中的安全违规率显著升高；图像生成任务 consistently 比文本生成任务更容易出现安全问题。这些发现表明现有UMM在系统级安全对齐方面存在明显不足。

【应用价值 / Applications】
UniSAFE为UMM开发者和部署者提供了全面的安全评估工具，可用于识别模型在复杂多模态交互中的漏洞，指导更安全的多模态系统设计与安全对齐策略制定。该基准对于推动统一多模态模型的负责任发展和实际应用具有重要意义。
