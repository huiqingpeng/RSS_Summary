---
title: "Probabilistic approximate optimization using single-photon avalanche diode arrays"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2602.13943"
published: "2026-03-19"
summarized: "2026-03-19T12:04:39.372456"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文首次在基于单光子雪崩二极管（SPAD）阵列的硬件上实现了概率近似优化算法（PAOA）。该研究利用64×64的CMOS集成pgSPAD阵列，通过变分学习直接适应器件固有的非理想特性（如非对称Gompertz型激活函数），无需对器件进行繁琐的校准。在26自旋Sherrington-Kirkpatrick模型上的实验表明，PAOA能够以较少参数（最多17层，即34个参数）实现高近似比，且硬件推理结果与CPU仿真高度一致，为大规模CMOS兼容的概率计算提供了可行路径。

【方法概述 / Method】

论文采用概率近似优化算法（PAOA），将优化问题的能量景观本身视为可变的，通过迭代采样学习电路参数。该方法区别于传统固定哈密顿量的采样方式，利用SPAD阵列中每个p比特固有的、因暗计数变化导致的器件特异性非对称激活函数，将残余激活和器件失配吸收到变分参数中，而非强制校准为标准的对称逻辑/双曲正切函数。

【实验结果 / Results】

在典型的26自旋Sherrington-Kirkpatrick（SK）自旋玻璃实例上，PAOA使用最多17层（34个参数）即达到了高近似比。pgSPAD硬件上的推理结果与CPU仿真结果紧密吻合，验证了变分学习方法能够有效包容纳米尺度器件的非理想特性，同时保持了算法的优化性能。

【应用价值 / Applications】

该研究为组合优化问题（在科学和工程中广泛存在）提供了一种CMOS兼容的专用硬件解决方案，避免了量子退火器等替代方案所需的低温环境。通过利用成熟CMOS工艺制造的概率计算器件，PAOA方法可扩展至更大规模系统，为机器学习、物流调度、芯片设计等需要高效求解NP难优化问题的领域开辟了实用化路径。
