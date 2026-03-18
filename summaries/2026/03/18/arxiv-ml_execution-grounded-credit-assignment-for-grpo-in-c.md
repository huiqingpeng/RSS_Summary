---
title: "Execution-Grounded Credit Assignment for GRPO in Code Generation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16158"
published: "2026-03-18"
summarized: "2026-03-18T15:41:25.636746"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对代码生成任务中GRPO（Group Relative Policy Optimization）方法的信用分配问题提出改进。现有无评论家的可验证奖励强化学习（RLVR）虽能通过单元测试通过率优化代码生成，但GRPO将单一结果信号均匀分配给长程序的所有token，即使失败源于局部语义错误。作者提出执行锚定信用分配（EGCA），利用执行轨迹定位最早语义分歧点，仅对该token跨度分配优势信号，在HumanEval和MBPP基准上分别取得82.1%和68.9%的pass@1性能，较GRPO提升3.1和1.5个百分点。

【方法概述 / Method】

EGCA通过对比执行候选程序与离线预置的参考解（仅用于分析而非监督）的执行轨迹，识别最早出现语义分歧的位置。对于满足算法约束但测试失败的程序，该方法仅对导致分歧的token跨度计算优势值，并屏蔽下游token的梯度更新。此方案无需训练额外的评论模型、辅助损失函数或可学习验证器，可直接嵌入现有GRPO框架。

【实验结果 / Results】

在HumanEval基准上，EGCA达到82.1% pass@1，较基线GRPO提升3.1个百分点；在MBPP上达到68.9%，提升1.5个百分点。该方法仅引入18%的墙钟时间开销，实现了精度与效率的有效平衡。

【应用价值 / Applications】

该研究适用于大语言模型代码生成任务的强化学习微调场景，特别是需要精细错误定位的编程教育、自动化代码修复和竞赛级代码生成系统。EGCA的即插即用特性使其易于集成至现有RLVR流水线，为工业级代码生成模型的训练效率与输出质量优化提供了实用方案。
