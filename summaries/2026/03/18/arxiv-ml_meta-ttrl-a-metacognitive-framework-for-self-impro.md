---
title: "Meta-TTRL: A Metacognitive Framework for Self-Improving Test-Time Reinforcement Learning in Unified Multimodal Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15724"
published: "2026-03-18"
summarized: "2026-03-18T15:34:53.901750"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Meta-TTRL，一种用于统一多模态模型（UMMs）的元认知测试时强化学习框架，旨在解决现有文本到图像生成测试时缩放方法仅能进行实例级改进、无法跨提示累积知识的局限。该框架通过模型内在的元知识监控信号指导测试时参数优化，实现了测试时的自我改进和能力级提升。实验表明，Meta-TTRL在Janus-Pro-7B、BAGEL和Qwen-Image等代表性UMMs上具有良好的泛化性，在组合推理任务和多个T2I基准上取得显著提升，且仅需有限数据。

【方法概述 / Method】
Meta-TTRL采用元认知测试时强化学习框架，利用统一多模态模型自身的元知识生成内在监控信号，指导测试时的参数优化过程。该方法突破了传统搜索或采样策略的局限，使模型能够在测试阶段进行自我改进并从先前推理中学习累积知识。

【实验结果 / Results】
Meta-TTRL在三个代表性统一多模态模型（Janus-Pro-7B、BAGEL、Qwen-Image）上展现出良好的跨模型泛化能力，在组合推理任务和多个文本到图像生成基准上均取得显著性能提升。研究还揭示了有效测试时强化学习的关键机制——"元认知协同"，即监控信号与模型优化机制的对齐是实现自我改进的核心。

【应用价值 / Applications】
该研究为统一多模态模型的文本到图像生成提供了首个全面的测试时强化学习分析框架，可广泛应用于需要高质量图像生成的场景，如创意内容生产、自动化设计等。其自我改进机制减少了对大量训练数据的依赖，为部署后的模型持续优化提供了可行路径，具有重要的实际部署价值。
