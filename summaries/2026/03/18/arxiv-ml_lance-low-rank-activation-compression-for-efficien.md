---
title: "LANCE: Low Rank Activation Compression for Efficient On-Device Continual Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.21617"
published: "2026-03-18"
summarized: "2026-03-18T16:19:09.778523"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了LANCE（低秩激活压缩）框架，用于解决边缘设备上模型微调和持续学习中的高内存开销问题。该方法通过一次性高阶奇异值分解（SVD）获得可重用的低秩子空间，避免了重复分解带来的计算开销，同时利用固定的正交子空间实现无需存储大型任务特定矩阵的持续学习。实验表明，LANCE在保持与完整反向传播相当准确率的同时，可将激活存储压缩高达250倍，并在持续学习基准上达到与正交梯度投影方法相当的性能。

【方法概述 / Method】
LANCE采用一次性高阶SVD分解构建低秩子空间，将激活投影到该子空间进行压缩存储，反向传播时通过投影矩阵重建梯度。对于持续学习，该方法将不同任务分配到相互正交的子空间，利用子空间的正交性防止任务间干扰，无需额外存储任务特定的投影矩阵。

【实验结果 / Results】
在CIFAR-10/100、Oxford-IIIT Pets、Flowers102和CUB-200数据集上，LANCE实现了最高250倍的激活存储压缩，同时保持与完整反向传播相当的准确率。在持续学习基准（Split CIFAR-100、Split MiniImageNet、5-Datasets）上，其性能与正交梯度投影方法相当，但内存成本显著降低。

【应用价值 / Applications】
LANCE适用于资源受限的边缘设备上的个性化模型微调和持续学习场景，如智能手机、物联网设备等，能够在保护隐私的前提下实现本地模型适应和新任务学习。该方法为部署在终端设备上的AI系统提供了高效、可扩展的内存优化解决方案，支持长期自适应和终身学习应用。
