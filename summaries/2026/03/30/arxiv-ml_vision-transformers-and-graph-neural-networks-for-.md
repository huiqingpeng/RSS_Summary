---
title: "Vision Transformers and Graph Neural Networks for Charged Particle Tracking in the ATLAS Muon Spectrometer"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25793"
published: "2026-03-30"
summarized: "2026-03-31T07:27:20.690542"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对ATLAS实验在高亮度LHC时代面临的带电粒子重建挑战，提出了两种基于机器学习的解决方案。研究首先利用图神经网络（GNN）整合到基线重建链中，实现背景击中抑制，将重建速度提升15%（从255 ms降至217 ms）。其次，研究探索了基于Vision Transformer的端到端缪子径迹重建概念验证，在消费级GPU上实现了2.3 ms的超快速近似重建，同时保持98%的径迹重建效率。

【方法概述 / Method】
研究采用两种互补的深度学习架构：一是将图神经网络嵌入现有重建流程，用于识别和过滤探测器中的背景噪声击中；二是直接采用Vision Transformer架构进行端到端的缪子径迹重建，绕过传统分步重建算法。这两种方法分别针对"嵌入式优化"和"替代式重建"两种不同的应用需求。

【实验结果 / Results】
GNN方法在保持物理性能的同时，将重建时间从255 ms缩短至217 ms，实现15%的加速。Vision Transformer方法则实现了数量级的性能飞跃，重建时间仅为2.3 ms，同时达到98%的径迹重建效率，为实时触发系统提供了极具潜力的快速近似重建方案。

【应用价值 / Applications】
该研究对高亮度LHC时代的ATLAS实验触发系统具有重要价值，特别是满足事件过滤器（Event Filter）对实时数据处理的严苛要求。GNN方案可直接部署优化现有系统，而Vision Transformer方案为下一代超快速硬件触发（如FPGA或ASIC实现）提供了技术路径，有望应对每束团 crossing 高达200次质子-质子碰撞的极端高占据率环境。
