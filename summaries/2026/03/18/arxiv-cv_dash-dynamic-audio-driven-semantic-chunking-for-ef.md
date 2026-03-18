---
title: "DASH: Dynamic Audio-Driven Semantic Chunking for Efficient Omnimodal Token Compression"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15685"
published: "2026-03-18"
summarized: "2026-03-18T18:22:23.430183"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DASH（Dynamic Audio-driven Semantic cHunking），一种无需训练的动态音频驱动语义分块框架，用于全模态大语言模型（OmniLLMs）的token压缩。该方法利用音频嵌入作为语义锚点，通过余弦相似度不连续性检测边界，生成动态变长片段以逼近序列的分段相干结构，并将边界投影到视频token实现显式跨模态分割。实验表明，DASH在AVUT、VideoMME和WorldSense数据集上实现了更高的压缩比，同时保持了优于现有方法的准确率。

【方法概述 / Method】
DASH采用三阶段技术方案：首先以音频嵌入为语义锚点，通过检测余弦相似度突变识别语义边界候选；其次将音频边界投影至视频token，建立跨模态对齐的显式分段；最后在每段内通过融合结构边界线索、表征独特性和注意力显著性的三信号重要性估计器，确定token保留策略，克服纯注意力选择的稀疏性偏差。

【实验结果 / Results】
DASH在AVUT、VideoMME和WorldSense三个基准数据集上进行了广泛验证，结果表明该方法在实现更高token压缩比的同时，保持了优于现有固定窗口分区和纯注意力剪枝方法的准确率，证明了其在激进token削减条件下的鲁棒性。

【应用价值 / Applications】
DASH可广泛应用于需要实时处理长序列音视频的多模态大模型场景，如视频会议分析、智能监控和沉浸式虚拟现实等，显著降低推理成本；其无需训练的特性使其易于部署到现有OmniLLMs中，为边缘设备上的高效全模态理解提供了可行方案。
