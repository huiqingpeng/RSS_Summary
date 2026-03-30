---
title: "DataFlex: A Unified Framework for Data-Centric Dynamic Training of Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26164"
published: "2026-03-30"
summarized: "2026-03-31T07:22:32.639915"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 DataFlex，一个基于 LLaMA-Factory 构建的统一数据中心动态训练框架，用于解决现有数据选择、数据混合优化和数据重加权方法在孤立代码库中开发、接口不一致的问题。DataFlex 支持样本选择、领域混合调整和样本重加权三种动态数据优化范式，并与原始训练工作流完全兼容。实验表明，动态数据选择在 MMLU 上持续优于静态全数据训练；DoReMi 和 ODM 数据混合方法在 Qwen2.5-1.5B 的预训练中改善了 MMLU 准确率和语料级困惑度；同时 DataFlex 相比原始实现具有一致的运行效率提升。

【方法概述 / Method】

DataFlex 基于 LLaMA-Factory 构建，提供可扩展的 trainer 抽象和模块化组件，实现了即插即用的标准 LLM 训练替代方案。该框架统一了嵌入提取、推理和梯度计算等关键模型相关操作，并支持 DeepSpeed ZeRO-3 等大规模训练设置，使三种数据中心范式（样本选择、领域混合调整、样本重加权）能够在统一接口下协同工作。

【实验结果 / Results】

在 Mistral-7B 和 Llama-3.2-3B 上的实验显示，动态数据选择在 MMLU 基准上持续优于静态全数据训练。在 Qwen2.5-1.5B 的 SlimPajama 预训练实验中（6B 和 30B token 规模），DoReMi 和 ODM 数据混合方法相比默认比例在 MMLU 准确率和语料级困惑度上均有提升。此外，DataFlex 在运行效率上相比各方法的原始实现也表现出一致的改进。

【应用价值 / Applications】

DataFlex 为 LLM 数据中心动态训练提供了一个有效、高效且可复现的基础设施，降低了研究者实现和对比不同数据优化方法的门槛。该框架可广泛应用于 LLM 预训练和微调阶段的数据优化，帮助开发者在计算预算有限的情况下通过更智能的数据选择策略提升模型性能，同时促进该领域的公平比较和实际集成。
