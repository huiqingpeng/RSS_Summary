---
title: "Hierarchical Latent Structure Learning through Online Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19139"
published: "2026-03-20"
summarized: "2026-03-20T13:05:31.464972"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了HOLMES（Hierarchical Online Learning of Multiscale Experience Structure）模型，一种通过在线推理进行层次化潜在结构学习的计算框架。该模型结合了嵌套中国餐馆过程（nested Chinese Restaurant Process）先验与序列蒙特卡洛推理，能够在无需对潜在结构进行显式监督的情况下实现逐试次的层次化潜在表征推理。实验表明，HOLMES在保持与扁平模型相当预测性能的同时，学习到了更紧凑的表征，并支持向更高层次潜在类别的一次性迁移。

【方法概述 / Method】
HOLMES采用嵌套中国餐馆过程先验来建模层次化的潜在类别结构，并通过序列蒙特卡洛（SMC）方法实现高效的在线推理。该框架能够在数据流式到达时逐步更新对层次结构的信念，避免了传统层次贝叶斯模型所需的离线批量推理。

【实验结果 / Results】
在模拟实验中，HOLMES达到了与扁平潜在原因模型相当的预测性能，但学习到的表征更加紧凑，并实现了向高层类别的一次性迁移。在具有嵌套时间结构的依赖上下文任务中，HOLMES相比扁平模型显著改善了结果预测。

【应用价值 / Applications】
HOLMES适用于需要从连续经验中自适应发现多尺度结构的场景，如强化学习中的任务结构发现、时间序列分析中的事件层次建模，以及认知科学中人类和动物的多层次概念学习研究。该框架为构建能够在线学习抽象层次知识的智能系统提供了可计算的实现途径。
