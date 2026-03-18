---
title: "HIPO: Instruction Hierarchy via Constrained Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16152"
published: "2026-03-18"
summarized: "2026-03-18T15:41:01.978007"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了HIPO（Hierarchical Instruction via Primal-dual Optimization），一种针对层级指令遵循（HIF）问题的新型对齐框架。现有方法如RLHF和DPO因仅优化单一目标而难以保证系统提示的优先遵守，而监督微调也无法在算法层面建立优先级不对称性。HIPO将HIF形式化为约束马尔可夫决策过程，通过原始-对偶安全强化学习方法将系统提示提升为严格的算法边界，在确保系统提示合规的约束区域内最大化用户效用。跨多种模型架构的评估表明，HIPO显著提升了系统合规性和用户效用，且机制分析显示该约束优化能自主驱动模型关注长程系统token。

【方法概述 / Method】
HIPO将层级指令遵循问题建模为约束马尔可夫决策过程（CMDP），其中系统提示合规性被显式编码为约束条件而非目标函数的一部分。算法采用原始-对偶（primal-dual）安全强化学习方法，通过动态调整拉格朗日乘子来严格强制执行系统提示边界，同时在该可行区域内优化用户效用最大化。

【实验结果 / Results】
在Qwen、Phi、Llama等多种模型架构上的广泛评估表明，HIPO相比标准方法显著提升了系统提示合规性和用户效用。机制分析进一步揭示，该约束优化过程能够自主驱动模型将注意力转向长距离的系统提示token，从而在神经机制层面实现了对高优先级指令的可靠遵循。

【应用价值 / Applications】
HIPO为复杂工作流中大型语言模型的可靠部署提供了原则性基础，特别适用于需要严格安全边界的多层级指令场景，如企业级AI助手、代码生成工具和自动化代理系统。该框架通过算法层面的优先级强制机制，有效解决了系统提示被用户提示覆盖或"越狱"攻击的安全隐患，提升了LLM在高风险应用中的可信度和鲁棒性。
