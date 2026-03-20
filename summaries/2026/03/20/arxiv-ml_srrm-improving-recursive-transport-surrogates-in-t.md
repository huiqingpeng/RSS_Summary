---
title: "SRRM: Improving Recursive Transport Surrogates in the Small-Discrepancy Regime"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18781"
published: "2026-03-20"
summarized: "2026-03-20T13:16:10.105782"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了递归划分方法作为Wasserstein距离计算代理的统计特性，特别是在小差异（small-discrepancy）情形下的分辨率问题。作者以递归秩匹配（RRM）为典型代表，在基于总体锚定的参考框架下建立了其一致性和显式收敛速率，并识别出导致小差异情形下分辨率损失的主导性错配机制。基于此分析，作者提出了选择性递归秩匹配（SRRM），该算法通过抑制主导性错配，在适度增加计算成本的前提下显著提升了Wasserstein距离代理的保真度。

【方法概述 / Method】
论文采用理论分析与算法设计相结合的方法，首先在总体锚定参考（population-anchored reference）的设定下对RRM进行严格的统计理论分析，建立其一致性并推导显式收敛速率；随后通过机制分析识别出小差异情形下的主导性错配来源，进而设计选择性抑制策略，提出改进算法SRRM。

【实验结果 / Results】
论文在二次成本（quadratic cost）设定下证明了锚定经验RRM的一致性并给出显式收敛速率；SRRM通过选择性抑制主导性错配，在小差异情形下实现了比标准RRM更高的保真度，且仅带来适度的额外计算开销。

【应用价值 / Applications】
该研究为Wasserstein距离的高效近似计算提供了理论基础和实用算法，可应用于最优传输、生成模型训练（如Wasserstein GAN）、分布匹配等机器学习任务，特别是在需要精细分辨分布间微小差异的场景中具有重要价值。
