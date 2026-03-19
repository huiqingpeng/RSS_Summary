---
title: "SENSE: Efficient EEG-to-Text via Privacy-Preserving Semantic Retrieval"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17109"
published: "2026-03-19"
summarized: "2026-03-19T12:07:36.278357"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SENSE（SEmantic Neural Sparse Extraction），一种轻量级且隐私保护的脑电信号（EEG）到文本转换框架。与现有依赖大语言模型（LLM）微调的方法不同，SENSE将解码过程解耦为两个阶段：设备端语义检索和基于提示的语言生成，在无需微调LLM的情况下实现了高质量的文本生成。该框架在128通道EEG数据集上的评估表明，其生成质量达到或超越了完全微调的基线模型（如Thought2Text），同时显著降低了计算开销。

【方法概述 / Method】
SENSE采用两阶段架构：首先，一个仅含约600万参数的轻量级EEG-to-Keyword模块在本地设备上将原始EEG信号映射到离散文本空间，提取非敏感的词袋（Bag-of-Words）表示；随后，这些语义关键词作为条件输入，通过零样本提示工程驱动现成的LLM生成流畅文本。这种设计实现了神经解码的本地化，原始神经数据始终保留在设备端。

【实验结果 / Results】
在包含6名受试者的128通道EEG数据集上，SENSE在文本生成质量方面匹配或超越了完全微调的Thought2Text等基线方法，同时大幅减少了计算资源需求。核心EEG处理模块的轻量化设计（~6M参数）使其能够在边缘设备上高效运行。

【应用价值 / Applications】
SENSE为下一代脑机接口（BCI）提供了一种可扩展且隐私感知的检索增强架构，特别适用于辅助通信、神经技术和人机交互等领域。通过本地化敏感神经数据处理并仅共享抽象语义线索，该框架在保障用户隐私的同时提升了系统的可访问性和实用性，为需要保护神经数据隐私的医疗和日常应用场景开辟了新的可能性。
