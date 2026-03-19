---
title: "Efficient Cross-Domain Offline Reinforcement Learning with Dynamics- and Value-Aligned Data Filtering"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.02435"
published: "2026-03-19"
summarized: "2026-03-19T14:10:34.152790"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了跨域离线强化学习（Cross-Domain Offline RL）问题，即利用有限的目标域数据和充足但可能存在动态偏移的源域数据来训练目标域智能体。作者从理论上证明了仅考虑动态对齐（dynamics alignment）是不够的，并推导出了新的目标域次优性边界，揭示了**价值对齐（value alignment）**的必要性——即需要从源域中选择高质量、高价值的样本。基于此理论洞察，作者提出了DVDF（Dynamics- and Value-aligned Data Filtering）方法，在多种动态偏移场景（包括运动学和形态学偏移）的实验中，即使目标域数据极其有限，DVDF也显著优于强基线方法。

【方法概述 / Method】
DVDF是一种统一的跨域离线强化学习框架，通过双重筛选机制选择性整合源域样本：首先筛选与目标域动态对齐的样本，其次进一步筛选具有高价值估计的优质样本。该方法将动态对齐和价值对齐结合在一个统一的框架中，避免了朴素合并数据集或仅考虑单一对齐准则带来的性能退化。

【实验结果 / Results】
实验在多种动态偏移场景下进行，包括运动学偏移（kinematic shifts）和形态学偏移（morphology shifts），并在多种任务和数据集上进行了评估。结果表明，即使在目标域数据极其有限的挑战性设置下，DVDF仍能持续显著优于现有强基线方法，验证了动态-价值双重对齐策略的有效性。

【应用价值 / Applications】
该研究适用于现实世界中目标环境数据稀缺但存在大量相关源环境数据的场景，如机器人控制（不同机器人形态迁移）、自动驾驶（不同车辆动力学迁移）、以及医疗决策（不同患者群体或医院环境迁移）。DVDF通过智能筛选源域数据，降低了跨域迁移的数据收集成本，提升了离线强化学习在资源受限环境下的实用性和泛化能力。
