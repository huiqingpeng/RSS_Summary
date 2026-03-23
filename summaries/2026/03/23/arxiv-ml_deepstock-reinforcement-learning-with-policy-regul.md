---
title: "DeepStock: Reinforcement Learning with Policy Regularizations for Inventory Management"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19621"
published: "2026-03-23"
summarized: "2026-03-24T07:20:16.366683"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DeepStock框架，通过将经典库存管理概念（如"Base Stock"）转化为策略正则化项，显著提升了深度强化学习（DRL）在库存管理中的训练稳定性和最终性能。研究表明，这种正则化方法能够大幅加速超参数调优过程，并改变了关于库存管理最佳DRL方法的传统认知。该框架已在阿里巴巴天猫电商平台实现100%部署，同时通过大量合成实验验证了其有效性。

【方法概述 / Method】
作者将经典库存理论中的"Base Stock"等概念形式化为策略正则化约束，嵌入到DRL的训练目标函数中。这种方法为DRL策略提供了先验知识引导，降低了策略搜索空间，从而减少对超参数的敏感性并加速收敛。

【实验结果 / Results】
在阿里巴巴天猫平台的实际部署中，带正则化的DRL方法成功替代了传统方案；合成实验表明，策略正则化显著提升了多种DRL算法的性能，并使得原本表现较差的算法（如某些off-policy方法）成为更具竞争力的选择，重塑了DRL方法在库存管理中的性能排序。

【应用价值 / Applications】
该研究为大规模电商平台的库存决策提供了可落地的AI解决方案，证明了DRL在真实工业环境中替代传统运筹学方法的可行性。其正则化思想可推广到其他具有领域知识的序列决策问题，为强化学习在供应链、物流管理等领域的应用提供了重要参考。
