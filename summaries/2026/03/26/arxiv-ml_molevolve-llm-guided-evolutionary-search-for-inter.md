---
title: "MolEvolve: LLM-Guided Evolutionary Search for Interpretable Molecular Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24382"
published: "2026-03-26"
summarized: "2026-03-27T07:23:13.184942"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出MolEvolve，一种由大语言模型（LLM）引导的进化搜索框架，用于可解释的分子优化。该框架将分子发现重新表述为自主的前瞻性规划问题，利用LLM主动探索化学符号操作库，并通过蒙特卡洛树搜索（MCTS）结合外部工具（如RDKit）进行测试时规划。实验表明，MolEvolve不仅能生成透明、人类可读的化学推理链，还在性质预测和分子优化任务中优于基线方法，有效解决了深度学习在化学中面临的活性悬崖（activity cliffs）和可解释性不足的挑战。

【方法概述 / Method】

MolEvolve采用LLM驱动的进化框架，通过LLM进行"冷启动"生成初始化学操作，结合蒙特卡洛树搜索（MCTS）引擎实现测试时的自主规划。系统利用外部化学工具（如RDKit）验证分子结构，自我发现最优转化路径，形成可执行的化学符号操作库，无需人工设计特征或依赖刚性先验知识。

【实验结果 / Results】

实验结果表明，MolEvolve在性质预测和分子优化任务中均优于基线方法。该框架成功进化出透明的推理链，能够将复杂的结构转化转化为人类可读的化学洞察，有效捕捉结构-活性间断性（activity cliffs），突破了传统表示学习方法受限于相似性原理的瓶颈。

【应用价值 / Applications】

MolEvolve在药物发现和分子设计领域具有重要应用价值，可辅助化学家理解结构修饰与性质变化的因果关系，提供可解释的优化建议。其自主进化能力和人类可读的推理链有助于加速先导化合物优化，降低实验成本，特别适用于需要精细结构调控以跨越活性悬崖的复杂优化场景。
