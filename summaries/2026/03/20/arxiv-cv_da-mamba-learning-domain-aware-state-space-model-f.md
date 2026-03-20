---
title: "DA-Mamba: Learning Domain-Aware State Space Model for Global-Local Alignment in Domain Adaptive Object Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18757"
published: "2026-03-20"
summarized: "2026-03-20T15:15:51.419963"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了DA-Mamba，一种用于域自适应目标检测（DAOD）的新型混合架构。针对现有CNN方法受限于局部连接、Transformer方法计算成本过高的问题，DA-Mamba结合CNN的效率与状态空间模型（SSMs）的线性时间长程建模能力，同时捕获全局和局部域不变特征。论文设计了图像感知SSM（IA-SSM）和对象感知SSM（OA-SSM）两个模块，分别实现图像级和实例级的全局-局部对齐。实验表明该方法能有效提升跨域检测性能。

【方法概述 / Method】

DA-Mamba采用CNN-SSM混合架构，在主干网络中集成IA-SSM模块以增强全局域感知，实现图像级特征对齐；在检测头中插入OA-SSM模块建模对象间的空间与语义依赖关系，实现实例级对齐。这种设计以线性计算复杂度实现了全局-局部多粒度特征融合。

【实验结果 / Results】

论文通过全面的实验验证了DA-Mamba的有效性，表明该方法能够高效提升目标检测器在跨域场景下的性能。具体量化结果未在提供的摘要中详述，但强调了在计算效率与检测精度之间取得了优于CNN和Transformer基线方法的平衡。

【应用价值 / Applications】

该研究适用于需要跨域部署目标检测模型的实际场景，如自动驾驶（仿真到真实环境）、监控分析（不同光照/天气条件）及工业检测（不同设备或批次）等。其线性复杂度的设计使其特别适合资源受限的边缘设备部署，解决了Transformer在实际应用中的计算瓶颈问题。
