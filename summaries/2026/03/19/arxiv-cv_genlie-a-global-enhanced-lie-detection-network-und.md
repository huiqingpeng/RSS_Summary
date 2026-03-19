---
title: "GenLie: A Global-Enhanced Lie Detection Network under Sparsity and Semantic Interference"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16935"
published: "2026-03-19"
summarized: "2026-03-19T14:21:19.933748"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了GenLie，一种全局增强的谎言检测网络，用于解决视频中欺骗信号稀疏且易被冗余信息淹没的问题。该网络通过局部特征建模结合全局监督优化，有效抑制了与身份相关的噪声干扰。在涵盖高利害和低利害场景的多个公开数据集上，GenLie均显著优于现有最先进方法。

【方法概述 / Method】
GenLie采用"局部建模+全局监督"的双层架构：在局部层面捕捉稀疏且细微的欺骗性线索，同时通过全局监督和优化机制确保表征的鲁棒性和判别性。该设计特别针对欺骗信号的短时性和个体差异性带来的语义干扰问题。

【实验结果 / Results】
实验在三个公开数据集上进行，覆盖高利害（high-stakes）和低利害（low-stakes）两种场景，结果表明GenLie在所有测试集上均持续超越当前最优方法，验证了其在不同欺骗情境下的泛化能力和有效性。

【应用价值 / Applications】
该研究可应用于安全审讯、司法取证、金融风控等需要识别欺骗行为的场景，尤其在处理真实世界中稀疏、隐蔽的欺骗信号时具有重要价值。方法对身份相关噪声的抑制能力也使其更适用于跨个体的实际部署环境。
