---
title: "GIST: Gauge-Invariant Spectral Transformers for Scalable Graph Neural Operators"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16849"
published: "2026-03-18"
summarized: "2026-03-18T16:04:20.160780"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了GIST（Gauge-Invariant Spectral Transformers），一种新型图Transformer架构，解决了将Transformer位置编码适配到网格和图结构数据时的计算挑战与规范不变性问题。该架构通过随机投影实现端到端O(N)复杂度，同时通过基于内积的注意力机制在投影嵌入上算法化地保持规范不变性。理论证明GIST实现了具有有界失配误差的不变性学习，支持神经算子应用中跨任意网格分辨率的参数迁移。实验表明，GIST在标准图基准测试上达到SOTA性能（PPI数据集99.50% micro-F1），同时独特地扩展到75万节点的网格神经算子基准，在DrivAerNet和DrivAerNet++数据集上实现SOTA空气动力学预测。

【方法概述 / Method】
GIST采用随机投影技术将高维谱特征映射到低维空间，避免立方复杂度的精确特征分解，实现线性复杂度计算。核心创新在于设计基于内积的注意力机制，确保在随机投影后的嵌入空间仍保持规范不变性，从而消除数值求解器伪影导致的对称性破缺。

【实验结果 / Results】
在标准图学习基准（如PPI）上，GIST达到99.50% micro-F1的SOTA性能；在神经算子基准测试中，GIST成功扩展至75万节点的大规模网格，在具有挑战性的DrivAerNet和DrivAerNet++汽车空气动力学数据集上取得SOTA预测效果。模型展现出跨不同网格分辨率的强泛化能力，验证了理论保证的不变性学习特性。

【应用价值 / Applications】
GIST可广泛应用于科学计算中的神经算子学习，特别是需要处理多分辨率网格的物理仿真场景，如计算流体力学（CFD）、结构力学和气候建模。其规范不变性和线性复杂度特性使其能够部署于工业级大规模仿真，支持训练好的模型直接迁移到不同精度的网格离散化，显著降低多尺度物理系统建模的计算成本。
