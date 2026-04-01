---
title: "Big2Small: A Unifying Neural Network Framework for Model Compression"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29768"
published: "2026-04-01"
summarized: "2026-04-02T07:20:17.305354"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Big2Small，一个统一的神经网络模型压缩框架。作者基于测度理论构建了数学上统一的模型压缩框架，证明各种压缩技术（低秩分解、剪枝、量化、知识蒸馏等）在数学上等价于带正则化的神经网络。在此基础上，作者将隐式神经表示（INRs）从数据域拓展到网络参数域，通过训练紧凑的INRs来编码大模型权重并在推理时重建，实现了无需训练数据的模型压缩方法。

【方法概述 / Method】
Big2Small的核心方法是将大模型的权重张量视为连续信号，利用隐式神经表示（INRs）对其进行参数化编码。为提升重建保真度，作者设计了离群值感知预处理（Outlier-Aware Preprocessing）来处理极端权重值，以及频率感知损失函数（Frequency-Aware Loss）来保留高频细节。

【实验结果 / Results】
实验在图像分类和分割任务上进行，结果表明Big2Small在准确率和压缩比方面达到了与最先进基线方法相当的性能。该方法作为数据无关的压缩方案，能够在无需原始训练数据的情况下实现有效的模型压缩。

【应用价值 / Applications】
Big2Small适用于需要高效部署大模型的边缘设备和资源受限环境，特别是在数据隐私敏感场景（无法获取原始训练数据）中具有独特优势。该框架为模型压缩领域提供了统一的理论基础，有助于推动该领域从碎片化启发式方法向系统化学科发展。
