---
title: "ELiC: Efficient LiDAR Geometry Compression via Cross-Bit-depth Feature Propagation and Bag-of-Encoders"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.14070"
published: "2026-03-20"
summarized: "2026-03-20T17:04:24.703512"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ELiC，一种高效的LiDAR几何压缩实时框架，通过跨位深度特征传播、编码器袋（Bag-of-Encoders）选择机制和Morton序保持层次结构，解决了现有方法在各深度独立处理、重复估计局部上下文导致的压缩效率低下问题。该方法在Ford和SemanticKITTI数据集上实现了最先进的压缩性能，同时保持实时吞吐量。核心创新在于利用低密度层的特征支持高密度层预测，并根据占用统计动态选择编码网络，避免了为每层单独训练模型。

【方法概述 / Method】
ELiC采用三项关键技术：跨位深度特征传播机制，将较密低深度提取的特征重用于较稀疏高深度的预测；Bag-of-Encoders（BoE）选择方案，为每个深度从小型编码器池中选择最适合的网络，自适应匹配占用统计；Morton序保持层次结构，在深度转换间维持全局Z序，消除每层的排序操作。

【实验结果 / Results】
ELiC在Ford和SemanticKITTI数据集上取得了最先进的压缩性能，同时实现了实时吞吐量。跨位深度特征传播和BoE机制显著提升了熵建模效率，Morton层次结构有效降低了延迟，整体在压缩率与计算效率之间达到了最优平衡。

【应用价值 / Applications】
该研究适用于自动驾驶、机器人导航等需要实时传输和存储大规模LiDAR点云数据的场景，可显著降低带宽需求和存储成本。其实时处理能力使其特别适合边缘计算环境，为车载LiDAR数据压缩提供了实用的解决方案。
