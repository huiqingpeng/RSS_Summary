---
title: "Capturing Multivariate Dependencies of EV Charging Events: From Parametric Copulas to Neural Density Estimation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29554"
published: "2026-04-01"
summarized: "2026-04-02T07:19:04.923337"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文首次将Vine copulas和Copula密度神经网络估计框架（CODINE）应用于电动汽车（EV）充电事件建模，以解决传统统计方法无法捕捉充电变量（到达时间、持续时长、能源需求）之间复杂非线性依赖关系的问题。研究在三个真实数据集上验证了这些高容量依赖模型，结果表明Vine copulas和CODINE在显式建模联合依赖结构方面优于传统参数化方法，且与条件高斯混合模型网络等最先进基准相比具有高度竞争力。这些方法能更好地保留尾部行为和相关结构，为不同基础设施场景下的合成充电事件生成提供了稳健框架。

【方法概述 / Method】
论文采用两类先进的依赖建模方法：Vine copulas通过分层分解多元联合分布为二元copula的乘积来灵活捕捉复杂依赖结构；CODINE（Copula Density Neural Estimation）则利用神经网络直接学习copula密度函数，实现非参数化的密度估计。两种方法均专注于显式建模变量间的联合依赖结构，而非仅拟合边缘分布。

【实验结果 / Results】
在三个多样化的真实世界EV充电数据集上，Vine copulas和CODINE均显著优于传统参数化copula族（如Gaussian、t、Gumbel等）；与当前最先进的条件高斯混合模型网络（cGMMN）相比，所提方法保持高度竞争力，尤其在保留尾部依赖和相关结构方面表现更优。实验证明了显式依赖建模对合成数据生成质量的关键作用。

【应用价值 / Applications】
该研究为电网可靠性分析和智能充电策略设计提供了更精确的EV充电行为建模工具，可支持充电基础设施规划、电网负荷预测及需求响应优化。生成的合成充电事件数据可用于模拟不同场景下的电网影响，助力运营商在多样化基础设施环境中评估和优化充电策略，推动电动汽车与电网的协同发展。
