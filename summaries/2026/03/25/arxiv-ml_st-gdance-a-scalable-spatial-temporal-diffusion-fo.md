---
title: "ST-GDance++: A Scalable Spatial-Temporal Diffusion for Long-Duration Group Choreography"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22316"
published: "2026-03-25"
summarized: "2026-03-26T07:10:25.229203"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了ST-GDance++，一种可扩展的时空扩散框架，用于解决长时长群体舞蹈生成中的计算效率和多舞者协调问题。该框架通过解耦空间与时间依赖关系，分别采用轻量级距离感知图卷积进行空间建模，以及设计扩散噪声调度策略结合高效时间对齐注意力掩码进行时间建模。实验表明，该方法在AIOZ-GDance数据集上达到了与现有方法相当的生成质量，同时显著降低了推理延迟，实现了流式长序列生成。

【方法概述 / Method】

ST-GDance++采用空间-时间解耦的架构设计：空间维度上引入距离感知图卷积（Distance-Aware Graph Convolutions），以轻量级方式捕捉舞者间的相对位置关系与空间交互；时间维度上设计特定的扩散噪声调度策略，并配合时间对齐注意力掩码（Temporal-Aligned Attention Mask），将双向注意力转换为高效的单向流式处理，避免传统方法中二次增长的注意力计算开销。

【实验结果 / Results】

在AIOZ-GDance数据集上的评估显示，ST-GDance++在生成质量指标上与现有最优方法具有竞争力，同时实现了显著的推理速度提升和延迟降低。该方法能够有效支持长时长舞蹈序列的流式生成，在舞者数量增加和序列长度扩展时保持良好的可扩展性，减少了多舞者之间的运动碰撞现象。

【应用价值 / Applications】

该研究对影视制作、游戏开发和动画产业具有重要应用价值，可实现实时或近实时的交互式群体舞蹈生成。其高效的流式生成能力使其适用于需要长时长连续舞蹈内容的场景，如虚拟演唱会、元宇宙社交平台和交互式娱乐系统，为大规模多智能体动作合成提供了可部署的技术方案。
