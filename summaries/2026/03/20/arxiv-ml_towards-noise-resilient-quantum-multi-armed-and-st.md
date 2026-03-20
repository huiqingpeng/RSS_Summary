---
title: "Towards Noise-Resilient Quantum Multi-Armed and Stochastic Linear Bandits"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18431"
published: "2026-03-20"
summarized: "2026-03-20T12:11:31.197264"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了噪声鲁棒的量子多臂赌博机（QMAB）和随机线性赌博机（QSLB）算法，解决了现有量子算法假设理想无噪声量子电路的局限性。作者提出了一种噪声鲁棒的量子蒙特卡洛（QMC）估计器，能够在查询量子奖励预言机时提高估计精度。基于该估计器构建的QMAB和QSLB算法在保留相比经典方法二次加速优势的同时，显著提升了在噪声环境下的性能表现。

【方法概述 / Method】
论文首先设计了一种噪声鲁棒的QMC算法，通过改进估计策略来对抗量子噪声对奖励估计的影响；随后将该估计器分别嵌入到多臂赌博机和随机线性赌博机的决策框架中，构建出完整的噪声鲁棒QMAB和QSLB算法。

【实验结果 / Results】
实验表明，所提出的噪声鲁棒方法在多种量子噪声模型下均提升了QMAB的估计精度并降低了累积遗憾（regret）；该方法在存在噪声的实际NISQ设备环境中仍能保持相对于经典算法的性能优势。

【应用价值 / Applications】
该研究为当前含噪声中等规模量子（NISQ）设备上的在线决策和强化学习应用提供了实用算法，可应用于量子计算辅助的推荐系统、资源分配和自适应实验设计等场景，推动了量子机器学习算法从理论理想环境向实际硬件部署的转化。
