---
title: "On-Policy RL Meets Off-Policy Experts: Harmonizing Supervised Fine-Tuning and Reinforcement Learning via Dynamic Weighting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2508.11408"
published: "2026-03-18"
summarized: "2026-03-18T16:18:46.910824"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了CHORD框架，通过动态加权机制统一监督微调（SFT）与强化学习（RL），将SFT重新定位为在线策略RL过程中的动态辅助目标而非独立阶段。该框架采用全局系数和token级权重函数的双重控制机制，在促进在线策略探索的同时缓解离线策略数据的干扰，实现了稳定高效的学习过程，并在多个实际任务上显著超越基线方法。

【方法概述 / Method】

CHORD框架基于离线策略与在线策略的统一视角，首先通过全局系数控制从离线模仿到在线探索的整体过渡，然后利用token级权重函数实现对专家数据的细粒度学习，使模型能够动态调整对离线专家数据的依赖程度，从而在RL训练过程中自适应地平衡模仿与探索。

【实验结果 / Results】

实验表明CHORD在多种实际任务上实现了稳定且高效的学习过程，通过有效协调离线专家数据与在线策略探索，相比基线方法取得了显著性能提升，同时避免了破坏已建立的响应模式和过度拟合专家数据的风险。

【应用价值 / Applications】

该研究为大语言模型的后训练提供了更高效的SFT-RL整合方案，适用于需要同时保持专家知识质量和探索更优策略的场景，如对话系统优化、代码生成改进和复杂推理任务等领域，有助于降低多阶段训练的计算成本并提升模型对齐效果。
