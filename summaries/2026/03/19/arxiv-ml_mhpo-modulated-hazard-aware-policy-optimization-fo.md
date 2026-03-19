---
title: "MHPO: Modulated Hazard-aware Policy Optimization for Stable Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16929"
published: "2026-03-19"
summarized: "2026-03-19T12:05:47.425519"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Modulated Hazard-aware Policy Optimization (MHPO)，一种用于稳定强化学习的新框架，以解决基于GRPO的方法中重要性比率调控不稳定的问题。MHPO通过引入Log-Fidelity Modulator (LFM)将无界重要性比率映射到有界可微域，并设计了Decoupled Hazard Penalty (DHP)利用生存分析的累积风险函数独立调节正负策略偏移。在多种文本和视觉-语言推理基准上的广泛评估表明，MHPO在提升性能的同时显著增强了训练稳定性。

【方法概述 / Method】
MHPO的核心包含两个创新组件：Log-Fidelity Modulator (LFM)通过数学变换将重要性比率压缩到有界区间，消除硬裁剪带来的非可微边界和梯度消失问题；Decoupled Hazard Penalty (DHP)则引入生存分析中的累积风险函数，对策略的过度扩张（正向偏移）和灾难性收缩（负向偏移）进行非对称的细粒度惩罚，从而在稳定的信任区域内实现策略优化。

【实验结果 / Results】
MHPO在多样化的推理基准测试（包括纯文本和视觉-语言任务）上进行了全面评估，结果表明该方法始终优于现有基线方法，在取得更优性能的同时显著提升了训练稳定性，有效缓解了模式崩溃和策略侵蚀等问题。

【应用价值 / Applications】
MHPO可广泛应用于基于强化学习的大语言模型后训练场景，特别是需要稳定优化过程的复杂推理任务（如数学推理、代码生成和多模态理解）。该方法为工业级RLHF和推理能力增强提供了更可靠的优化框架，有助于降低训练过程中的策略崩溃风险，提升模型部署的稳定性。
