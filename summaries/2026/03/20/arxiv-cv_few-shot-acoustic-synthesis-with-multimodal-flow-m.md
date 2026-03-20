---
title: "Few-shot Acoustic Synthesis with Multimodal Flow Matching"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19176"
published: "2026-03-20"
summarized: "2026-03-20T16:09:34.171499"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了FLAC（flow-matching acoustic generation），一种基于流匹配的概率化少样本声学合成方法，用于在给定极少场景上下文的情况下建模合理房间脉冲响应（RIR）的分布。该方法利用以流匹配目标训练的扩散Transformer，在新场景中任意位置生成RIR，条件包括空间、几何和声学线索。FLAC在AcousticRooms和Hearing Anything Anywhere数据集上，仅用单样本即可超越最先进的八样本基线方法。此外，作者还提出了AGREE（joint acoustic-geometry embedding），用于几何一致性地评估生成RIR。这是首个将生成式流匹配应用于显式RIR合成的研究。

【方法概述 / Method】

FLAC采用基于流匹配（flow matching）目标的扩散Transformer架构，通过连续归一化流学习从简单先验分布到复杂RIR分布的映射。该方法以多模态条件（包括空间位置、场景几何和稀疏声学测量）为输入，实现概率化生成，从而捕捉场景声学固有的不确定性。

【实验结果 / Results】

在AcousticRooms和Hearing Anything Anywhere两个基准数据集上，FLAC仅用单样本（one-shot）即超越了现有最先进的八样本（eight-shot）确定性基线方法。作者还引入AGREE嵌入空间，通过检索和分布度量验证了生成RIR与场景几何的一致性。

【应用价值 / Applications】

该研究可广泛应用于沉浸式虚拟现实、游戏音频、元宇宙环境以及建筑声学设计等领域，能够以极少量的声学测量快速为新场景生成空间连续且物理合理的声学效果，大幅降低传统神经声场方法所需的数据采集和训练成本。
