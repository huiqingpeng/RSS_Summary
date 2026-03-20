---
title: "InfoMamba: An Attention-Free Hybrid Mamba-Transformer Model"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18031"
published: "2026-03-20"
summarized: "2026-03-20T12:05:24.557490"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了InfoMamba，一种无注意力机制的混合Mamba-Transformer架构，旨在解决序列建模中细粒度局部建模与长程依赖捕获之间的平衡问题。作者通过一致性边界分析，刻画了对角短记忆SSM何时能近似因果注意力，并识别了其结构性缺陷。InfoMamba采用概念瓶颈线性滤波层替代token级自注意力，并通过信息最大化融合（IMF）机制动态将全局上下文注入SSM动态中，在分类、密集预测和非视觉任务上均优于强Transformer和SSM基线，同时保持近线性复杂度扩展。

【方法概述 / Method】
InfoMamba的核心是一个混合架构，包含两个关键组件：（1）概念瓶颈线性滤波层，作为最小带宽的全局接口替代传统自注意力；（2）选择性递归流，通过信息最大化融合（IMF）机制与全局接口协同工作。IMF基于互信息启发的目标函数，动态地将全局上下文注入SSM状态更新中，并鼓励两个信息流之间的互补信息使用。

【实验结果 / Results】
InfoMamba在多种任务设置下进行了广泛评估，包括图像分类、密集预测（如语义分割）以及非视觉任务，结果表明该模型在准确率-效率权衡方面持续优于强大的Transformer和纯SSM基线模型。具体而言，InfoMamba在保持近线性计算复杂度扩展的同时，实现了与现有最先进方法相竞争甚至超越的性能表现。

【应用价值 / Applications】
InfoMamba的高效架构设计使其特别适用于需要处理长序列且计算资源受限的场景，如边缘设备部署、实时视频分析和大规模文档处理。该研究为开发下一代高效序列模型提供了新思路，有望推动视觉-语言多模态模型、科学计算模拟和基因组学分析等领域的应用发展，在保持高性能的同时显著降低计算成本。
