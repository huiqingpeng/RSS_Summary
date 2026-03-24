---
title: "Neural collapse in the orthoplex regime"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20587"
published: "2026-03-24"
summarized: "2026-03-25T07:12:01.399697"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了神经网络在分类任务中的神经坍缩（neural collapse）现象。传统研究表明，当特征空间维度d与类别数n满足n≤d+1时，特征向量会坍缩到正则单形的顶点。本文发现，在正交多面体区域（orthoplex regime，即d+2≤n≤2d）中，神经坍缩现象仍然存在，但呈现出不同的几何结构，作者利用Radon定理和凸性分析对这些新出现的几何图形进行了刻画。

【方法概述 / Method】
本研究主要运用Radon定理和凸性分析工具，对高维特征空间中神经坍缩的几何特性进行理论刻画，重点关注类别数远大于特征维度时的正交多面体区域。

【实验结果 / Results】
论文确定了在正交多面体区域（d+2≤n≤2d）中神经坍缩所呈现的具体几何结构，揭示了当n≫d时（如语言模型场景）神经坍缩现象的新形式，扩展了经典神经坍缩理论的适用范围。

【应用价值 / Applications】
该研究对大规模语言模型等n≫d场景下的神经网络理解与优化具有重要指导意义，为设计更高效的网络架构和损失函数提供了理论基础，特别是在类别数量庞大的分类任务中。
