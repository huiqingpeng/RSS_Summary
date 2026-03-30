---
title: "In-Context Molecular Property Prediction with LLMs: A Blinding Study on Memorization and Knowledge Conflicts"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25857"
published: "2026-03-30"
summarized: "2026-03-31T07:18:23.025588"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究探讨了大型语言模型（LLMs）在分子性质预测任务中的上下文学习能力，核心问题是区分模型是否真正进行上下文回归还是依赖训练数据记忆。作者通过系统性的"盲化"实验，逐步减少可用信息，并分析预训练知识与上下文信息之间的冲突。研究评估了GPT-4.1、GPT-5和Gemini 2.5三个家族的九个LLM变体，在MoleculeNet的三个数据集（Delaney溶解度、Lipophilicity、QM7原子化能）上进行了0-shot、60-shot和1000-shot的对比实验，为控制信息访问条件下的分子性质预测评估建立了原则性框架。

【方法概述 / Method】
研究采用迭代式信息盲化方法，系统性地遮蔽分子结构的不同层面（如分子式、SMILES表示、数值标签等），以隔离模型的真实上下文学习能力与记忆效应。同时通过变化上下文样本数量（0-shot、60-shot、1000-shot）作为信息访问的控制变量，并设计实验探测预训练知识与提供的上下文示例之间的知识冲突。

【实验结果 / Results】
实验揭示了LLMs在分子性质预测中存在的记忆效应和知识冲突现象：当关键分子标识信息被遮蔽时，模型性能显著下降，表明其依赖训练数据记忆而非真正的上下文推理；预训练知识与不一致的上下文信息之间存在明显冲突，模型难以有效整合矛盾信号；增加上下文样本数量在某些条件下可改善性能，但效果受信息盲化程度制约。

【应用价值 / Applications】
该研究为科学机器学习领域提供了评估LLMs真实推理能力的方法论工具，对药物发现、材料科学等依赖分子性质预测的应用具有重要意义。研究框架可帮助识别和缓解训练数据污染问题，指导未来开发更具鲁棒性和可解释性的化学AI系统，确保模型在实际部署中的可靠性。
