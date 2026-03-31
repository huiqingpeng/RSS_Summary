---
title: "Sparse-by-Design Cross-Modality Prediction: L0-Gated Representations for Reliable and Efficient Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26801"
published: "2026-03-31"
summarized: "2026-04-01T07:18:50.248967"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种跨模态稀疏预测的统一框架L0GM（L0-Gated Cross-Modality Learning），旨在解决当前图、文本、表格等不同模态数据稀疏化方法碎片化的问题。该框架通过硬混凝土随机门控机制直接在表示层施加L0稀疏性，实现了模态无关的端到端可训练稀疏化，并引入L0退火调度策略以产生清晰的准确率-稀疏性帕累托前沿。在三个公开基准数据集上的实验表明，L0GM在减少激活特征维度的同时保持了竞争性预测性能，并降低了期望校准误差（ECE），为异构模态间的准确率、效率和校准权衡分析提供了可复现的原语。

【方法概述 / Method】

L0GM采用硬混凝土（hard-concrete）随机门控机制，为每种模态的分类器接口附加可学习的稀疏门控：图神经网络的节点嵌入、Transformer的池化序列嵌入（如CLS）以及表格模型的学习嵌入向量。该方法通过显式的L0范数约束直接作用于表示层，并设计L0退火调度策略来稳定优化过程，使稀疏性比例成为可解释的控制参数。

【实验结果 / Results】

在ogbn-products（图）、Adult（表格）和IMDB（文本）三个基准数据集上，L0GM实现了与密集基线相当的预测准确率，同时显著减少了激活的表示维度；此外，L0GM在评估中表现出更低的期望校准误差（ECE），表明稀疏化表示有助于提升模型预测的概率校准质量。

【应用价值 / Applications】

L0GM为跨模态机器学习系统提供了统一的稀疏化原语，简化了异构数据（如图、文本、表格）混合场景下的部署和可靠性分析，特别适用于资源受限环境下的多模态预测系统；其显式的稀疏性控制机制支持可解释的准确率-效率-校准权衡决策，有助于构建更可靠、更高效的知识发现与数据挖掘（KDD）端到端流水线。
