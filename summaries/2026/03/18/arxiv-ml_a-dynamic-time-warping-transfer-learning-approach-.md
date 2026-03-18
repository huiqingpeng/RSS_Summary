---
title: "A Dynamic Time Warping-Transfer Learning Approach to Transferring Knowledge in Stress-strain Behaviors from Polymers to Metals: An Affordable and Generalizable Additive Manufacturing Part Qualification Framework"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.08699"
published: "2026-03-18"
summarized: "2026-03-18T17:03:50.968180"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究针对增材制造（AM）零件质量鉴定中传统测试方法成本高、耗时长的问题，提出了一种动态时间规整-迁移学习（DTW-TL）框架。该框架通过从低成本的增材制造聚合物材料（如Nylon、PLA、CF-ABS、Resin）向高性能昂贵的金属材料（AlSi10Mg、Ti6Al4V、碳钢）迁移应力-应变行为知识，实现了经济高效且可泛化的零件质量鉴定。实验表明，该方法在三种金属目标域上取得了平均绝对百分比误差12.41%、平均决定系数0.96的优异预测性能，显著优于无迁移学习的基线模型以及使用全部聚合物数据训练的迁移学习模型。

【方法概述 / Method】

该方法首先利用动态时间规整（DTW）算法在多个聚合物源域数据集中，为每个金属目标域筛选出最相似的最优单一聚合物数据集；随后基于选定的最优聚合物数据集训练长短期记忆（LSTM）网络，并将训练好的模型直接应用于金属目标域的应力-应变行为预测。这种"单源最优选择"策略有效降低了域间分布差异，提升了迁移学习的效率和效果。

【实验结果 / Results】

实验结果显示，Resin数据集被选为AlSi10Mg和Ti6Al4V的最优源域，而Nylon数据集则最适合碳钢目标域；DTW-TL模型在三种金属目标域上的平均MAPE为12.41%，平均RMSE为63.75，平均R²达0.96。与未使用迁移学习的原始LSTM模型以及使用全部四种聚合物数据训练的迁移学习模型相比，DTW-TL框架均展现出更优的预测性能，验证了源域选择策略的有效性。

【应用价值 / Applications】

该研究为航空航天、医疗器械等关键领域的金属增材制造零件质量鉴定提供了一种经济高效的替代方案，可显著降低对昂贵金属试样破坏性测试的依赖。同时，该框架具有良好的可扩展性，可推广至其他材料体系和增材制造工艺，为智能制造中的跨材料知识迁移和快速质量评估提供了通用方法论。
