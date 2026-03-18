---
title: "Connecting Jensen-Shannon and Kullback-Leibler Divergences: A New Bound for Representation Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.20644"
published: "2026-03-18"
summarized: "2026-03-18T16:20:13.278568"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究建立了Jensen-Shannon散度（JSD）与Kullback-Leibler散度（KLD）之间的理论联系，推导出一个新的、紧致且可处理的KLD下界作为JSD的函数。该研究证明了最大化基于JSD的信息量可以保证提升互信息（MI）的下界，为表示学习中广泛使用判别式损失优化替代目标函数提供了理论依据。实验表明，该下界估计器在MI估计中具有稳定性高、方差低的优势，并在信息瓶颈框架中展现了实用价值。

【方法概述 / Method】

作者通过数学推导建立了JSD与KLD之间的解析关系，得到了一个通用的KLD下界公式，并将其特化到联合分布与边缘分布的情形以关联互信息。在实现层面，研究分析了通过二元分类器交叉熵损失区分联合样本与边缘样本来估计JSD的变分方法，并验证了该方法恢复已知的JSD变分下界。

【实验结果 / Results】

实验表明，所提出的下界在MI估计中具有紧致性，相比现有最先进的神经估计器，该下界估计器在多个标准基准场景中始终提供稳定且低方差的MI下界估计。在信息瓶颈框架的应用中，该方法展现出良好的实用性能，验证了理论结果的有效性。

【应用价值 / Applications】

该研究为表示学习中基于判别式学习的MI优化方法（如InfoNCE、DIM等）提供了严格的理论支撑，可广泛应用于自监督学习、表征学习和信息瓶颈等场景。研究成果有助于理解和改进对比学习等方法的优化目标设计，提升表示学习算法的可解释性和可靠性。
