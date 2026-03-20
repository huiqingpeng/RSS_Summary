---
title: "HAViT: Historical Attention Vision Transformer"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18585"
published: "2026-03-20"
summarized: "2026-03-20T15:12:02.752379"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种跨层注意力传播方法HAViT（Historical Attention Vision Transformer），通过保留和整合编码器层间的历史注意力矩阵，解决传统Vision Transformer中注意力机制独立运行、限制信息流动的问题。该方法实现了注意力模式在Transformer层级结构中的渐进式优化，仅需添加注意力矩阵存储和混合操作即可最小化架构改动。在CIFAR-100和TinyImageNet上的实验表明，ViT准确率分别提升1.33%和1.25%，且跨架构验证显示多种Transformer变体均有类似增益。

【方法概述 / Method】

HAViT的核心是在标准Vision Transformer的各编码器层之间引入历史注意力传播机制，将当前层的注意力计算与之前层的历史注意力矩阵进行混合（blending）。具体实现上，每层维护一个可存储的历史注意力矩阵，通过可学习的混合超参数α（实验确定最优值为0.45）平衡当前注意力与历史注意力的贡献，从而实现跨层的信息流动和注意力模式的渐进式精化。

【实验结果 / Results】

在CIFAR-100数据集上，HAViT将ViT的准确率从75.74%提升至77.07%（+1.33%）；在TinyImageNet上从57.82%提升至59.07%（+1.25%）。跨架构验证中，CaiT等其他Transformer变体也获得了约1.01%的性能提升。系统分析表明混合超参数α=0.45在所有配置中均为最优，且随机初始化历史注意力矩阵始终优于零初始化，有助于加速收敛并提升最终性能。

【应用价值 / Applications】

HAViT可广泛应用于各类Vision Transformer架构的图像分类任务中，作为一种即插即用的增强模块提升模型性能，无需大规模修改现有网络结构。该方法对计算资源受限场景下的视觉模型优化具有重要价值，同时其揭示的跨层注意力传播机制可为后续Transformer架构设计提供理论参考，潜在适用于目标检测、语义分割等需要精细特征学习的下游视觉任务。
