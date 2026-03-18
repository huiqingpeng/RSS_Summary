---
title: "Residual Stream Duality in Modern Transformer Architectures"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16039"
published: "2026-03-18"
summarized: "2026-03-18T15:39:39.199109"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了Transformer架构中的"残差流对偶性"（Residual Stream Duality）概念，揭示了深度方向上的残差注意力读取与序列方向上的短滑动窗口注意力（ShortSWA）在算子层面的数学等价性。作者指出，虽然这种对偶性在算子层面成立，但在系统层面并不对称：对于大规模自回归模型，序列轴的ShortSWA更具硬件友好性，而若目标是修改残差捷径本身，则直接修改残差算子的Deep Delta Learning（DDL）是更简洁的干预方式。基于这一分析，论文为不同场景下的架构选择提供了明确建议。

【方法概述 / Method】

本文采用理论分析与架构对比相结合的方法，通过将Transformer的两个有序维度（序列位置和层深度）进行对偶映射，建立了残差流与注意力机制之间的形式化联系。具体而言，作者固定token位置、将层索引视为有序变量，证明了因果深度方向残差注意力读取与因果短滑动窗口注意力（ShortSWA）的算子等价性，并系统梳理了近期文献中ELC-BERT、DenseFormer、Vertical Attention、DCA、MUDDFormer等工作在这一设计空间中的位置。

【实验结果 / Results】

本文主要为概念性/理论性工作，未报告新的实验结果，而是基于对现有工作的分析得出结论： learned aggregation over depth（如ELC-BERT和DenseFormer）已证明优于均匀残差累积，而Vertical Attention、DCA、MUDDFormer等进一步展示了显式注意力路由的潜力；在系统效率方面，序列轴ShortSWA能够复用现有的token侧滑动窗口内核、KV缓存布局和分块执行机制，对大规模自回归模型更为实用。

【应用价值 / Applications】

本研究为现代Transformer架构设计提供了清晰的概念框架和实用指南：当研究目标是修改残差捷径本身时，推荐使用DDL方法；当目标是实现局部自适应混合且需考虑硬件效率时，推荐使用序列轴ShortSWA。这一分类有助于研究者在残差流设计空间中做出更明智的选择，避免重复造轮子或采用次优方案，对大规模语言模型的高效架构优化具有直接指导意义。
