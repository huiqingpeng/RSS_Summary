---
title: "Probabilistic Geometric Alignment via Bayesian Latent Transport for Domain-Adaptive Foundation Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23783"
published: "2026-03-26"
summarized: "2026-03-27T07:17:02.600094"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种面向基础模型的不确定性感知概率潜空间迁移框架，将域适应问题重新表述为表示空间中的随机几何对齐问题。该框架引入贝叶斯传输算子在Wasserstein型测地轨迹上重分布潜概率质量，并通过PAC-贝叶斯正则化机制约束后验模型复杂度以防止灾难性过拟合。理论分析保证了在分布偏移下的收敛稳定性、损失景观平滑性和样本效率，实验表明该方法显著降低了潜流形差异、加速了传输能量衰减，并改善了协方差校准性能。

【方法概述 / Method】

论文核心方法是构建贝叶斯传输算子（Bayesian transport operator），在Wasserstein几何框架下沿测地线轨迹进行概率质量的重分布；同时采用PAC-贝叶斯正则化对后验分布施加约束，控制模型复杂度并稳定优化动态。该方法将随机最优传输几何与统计泛化理论相结合，形成 principled 的概率对齐机制。

【实验结果 / Results】

实验表明，相比确定性微调和对抗域适应基线，所提方法实现了潜流形差异的显著降低、传输能量的加速衰减以及协方差校准的明显改善；此外，后验不确定性的有界演化表明跨域迁移过程中概率可靠性的增强，验证了理论保证的收敛稳定性和样本效率。

【应用价值 / Applications】

该框架为异构环境下现代基础架构的鲁棒适应提供了新范式，特别适用于医疗影像分析、自动驾驶感知、多语言NLP等标注稀缺的跨域迁移场景；通过显式建模不确定性传播，该方法提升了高风险决策场景下的模型可靠性，为下一代深度表示系统的可信迁移学习奠定了理论基础。
