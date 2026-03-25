---
title: "TreeTeaming: Autonomous Red-Teaming of Vision-Language Models via Hierarchical Strategy Exploration"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22882"
published: "2026-03-25"
summarized: "2026-03-26T07:17:54.131550"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了TreeTeaming，一种用于视觉-语言模型（VLMs）的自动化红队测试框架，突破了传统线性探索范式的局限。该框架通过层次化策略探索，将策略发现从静态测试转变为动态进化过程，在12个主流VLM中的11个上达到了最先进的攻击成功率（最高达87.60%）。生成的攻击在保持高成功率的同时，平均毒性降低23.09%，展现了更好的隐蔽性和微妙性。

【方法概述 / Method】

TreeTeaming的核心是一个由大语言模型（LLM）驱动的策略编排器（Orchestrator），它自主决定是进化有前景的攻击路径还是探索多样化的策略分支，从而动态构建和扩展策略树。多模态执行器负责执行这些复杂策略，实现从单一策略优化到层次化、进化式策略发现的范式转变。

【实验结果 / Results】

在12个主流VLMs的实验中，TreeTeaming在11个模型上取得了最先进的攻击成功率，在GPT-4o上达到87.60%。与先前公开的越狱策略集合相比，该方法展现出更优的策略多样性。此外，生成攻击的平均毒性降低23.09%，表明攻击更加隐蔽和微妙。

【应用价值 / Applications】

TreeTeaming为自动化漏洞发现引入了新范式，对保障前沿AI模型的安全具有重要价值。该方法可广泛应用于VLM安全测试、模型鲁棒性评估以及AI对齐研究，帮助开发者在模型部署前主动发现并修复潜在的安全漏洞，推动更安全的视觉-语言系统开发。
