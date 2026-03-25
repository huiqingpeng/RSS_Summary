---
title: "Problems with Chinchilla Approach 2: Systematic Biases in IsoFLOP Parabola Fits"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22339"
published: "2026-03-25"
summarized: "2026-03-26T07:12:46.354721"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文揭示了Chinchilla Approach 2（一种广泛使用的神经缩放定律拟合方法）存在系统性偏差问题：其抛物线近似会在计算最优分配估计中引入偏差，即使在无噪声合成数据上也是如此。将该方法应用于Llama 3的IsoFLOP数据时，这些偏差导致参数分配不足，相当于浪费了6.5%的训练计算预算（约3.8×10²⁵ FLOP）和140万美元的计算成本。作者进一步证明，常被认为存在数据效率低、数值不稳定等问题的Chinchilla Approach 3实际上可以通过变量投影（Variable Projection）技术有效解决，为缩放定律研究提供了更可靠的方法选择。

【方法概述 / Method】

论文通过理论分析和实证验证相结合的方式，系统检验了Chinchilla Approach 2中抛物线拟合的误差来源，包括IsoFLOP采样网格宽度、非中心采样以及损失曲面不对称性（α≠β）三个因素。针对Chinchilla Approach 3，作者利用目标函数的部分线性结构，采用变量投影技术将其转化为二维优化问题，实现了对所有五个损失曲面参数的无偏推断。

【实验结果 / Results】

在Llama 3开源IsoFLOP数据上的分析显示，Approach 2的偏差导致约140万美元（90%置信区间：41.2万-290万美元）的不必要计算成本，参数分配不足达6.5%。模拟实验表明，多模态模型的损失曲面不对称性更高，资源错配的机会成本更为显著。相比之下，采用变量投影的Approach 3能够在保持良好数值稳定性的同时，通过密集甚至穷举的网格搜索实现无偏参数估计。

【应用价值 / Applications】

该研究对大规模语言模型训练的资源优化具有直接经济价值，可帮助研究机构和企业避免数百万美元的计算浪费。提出的改进方法可替代现有的Approach 2，或作为更复杂的Approach 3扩展的基础，适用于需要精确估计计算最优分配的各种缩放定律研究场景，特别是在多模态模型等损失曲面不对称性较高的领域。
