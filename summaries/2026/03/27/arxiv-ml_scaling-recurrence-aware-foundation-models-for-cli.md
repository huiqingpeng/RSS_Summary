---
title: "Scaling Recurrence-aware Foundation Models for Clinical Records via Next-Visit Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24562"
published: "2026-03-27"
summarized: "2026-03-28T07:11:49.797962"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了RAVEN，一种基于复发感知下一次就诊事件预测（Recurrence-Aware next-Visit EveNt prediction）的新型生成式预训练策略，用于结构化电子健康记录（EHR）数据。研究利用超过一百万独特个体的数据集，使模型能够基于患者历史自回归地生成下一次就诊的临床事件。作者揭示了EHR基础模型评估中的一个关键陷阱：重复事件标记会虚增性能指标，并首次实证研究了数据受限、计算饱和条件下的缩放行为，发现单纯增加模型规模而不相应增加数据量并非最优策略。

【方法概述 / Method】
RAVEN采用自回归生成框架，通过预测下一次就诊的临床事件进行预训练，并引入针对重复事件的正则化约束。该方法将临床记录标记化为离散事件序列，使模型学习患者健康状态的时序动态演变模式。

【实验结果 / Results】
在零样本疾病发病率预测任务中，RAVEN的性能与经过完全微调的基于表示的Transformer模型相当，并显著优于广泛使用的基于模拟的下一标记预测方法。此外，该模型无需额外参数更新即可泛化到外部患者队列，即使在存在临床代码映射损失和特征覆盖缺失的情况下仍保持鲁棒性。

【应用价值 / Applications】
RAVEN为医疗健康领域的大规模预训练模型开发提供了新范式，特别适用于疾病风险预测、患者轨迹模拟等临床决策支持场景。其复发感知设计和对外部数据的零样本泛化能力，使其能够跨医疗机构部署，助力精准医疗和人群健康管理。
