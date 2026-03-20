---
title: "MolRGen: A Training and Evaluation Setting for De Novo Molecular Generation with Reasonning Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18256"
published: "2026-03-20"
summarized: "2026-03-20T12:09:18.829851"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了MolRGen，一个用于训练和评估基于推理的大语言模型（LLMs）进行从头分子生成（de novo molecular generation）的大规模基准和数据集。针对现有方法依赖真实标签监督（如已知性质修饰的分子对）的问题，MolRGen首次建立了无需先验高分候选知识的生成与评估框架，并引入了多样性感知的top-k分数来综合衡量生成分子的质量与多样性。研究团队利用该框架通过强化学习训练了一个240亿参数的LLM，并对其性能和局限性进行了深入分析。

【方法概述 / Method】

MolRGen构建了一个端到端的训练和评估环境，支持推理型LLM在无需配对监督数据的情况下学习分子生成策略。该方法采用强化学习（RL）对大型语言模型进行微调，使其能够直接优化分子性质得分，同时通过新提出的多样性感知指标平衡生成分子的质量与化学空间覆盖度。

【实验结果 / Results】

研究成功训练了一个240亿参数（24B）的推理LLM用于分子生成任务，并提供了详细的性能分析。实验表明该模型能够有效生成优化目标性质的新颖分子，多样性感知top-k分数验证了生成结果在质量与多样性之间的良好权衡，同时也揭示了当前方法在探索性与利用性平衡方面的局限性。

【应用价值 / Applications】

MolRGen为药物发现中的从头分子设计提供了可扩展的AI训练基础设施，使研究人员能够在缺乏已知活性分子的情况下探索广阔的化学空间。该框架可加速先导化合物优化和新药候选物的发现过程，降低传统药物研发中对大量实验筛选的依赖，具有显著的制药工业应用潜力。
