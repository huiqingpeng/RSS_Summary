---
title: "PulmoVec: A Two-Stage Stacking Meta-Learning Architecture Built on the HeAR Foundation Model for Multi-Task Classification of Pediatric Respiratory Sounds"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15688"
published: "2026-03-18"
summarized: "2026-03-18T16:06:58.619743"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究开发了PulmoVec，一种基于HeAR（Health Acoustic Representations）基础模型的多任务堆叠元学习架构，用于儿童呼吸音的分类。该框架整合了事件级声学表型分析与患者级临床分类，解决了现有AI方法受限于小数据集和单任务设计的问题。研究在24,808个事件级标注片段上验证，显示出优异的筛查和分类性能，为儿科呼吸医学中的数字听诊提供了新思路。

【方法概述 / Method】
PulmoVec采用两阶段堆叠元学习架构：第一阶段训练三个任务特定的分类器，分别用于筛查（正常/异常）、声音模式识别（啰音、喘鸣等）和疾病组预测；第二阶段将这些分类器的交叉验证概率输出与人口统计学元数据结合，输入LightGBM元模型进行整合学习。事件级预测通过集成投票聚合到患者级。

【实验结果 / Results】
事件级任务中，筛查模型ROC-AUC达0.96，声音模式识别宏ROC-AUC为0.96，疾病组预测宏ROC-AUC为0.94。患者级疾病组分类准确率为0.74，加权F1分数0.73，宏ROC-AUC达0.91。堆叠元学习相比单一基模型在所有任务上均提升了性能。

【应用价值 / Applications】
PulmoVec可应用于儿科呼吸系统疾病的自动化筛查与辅助诊断，降低传统听诊的主观性和听诊者间差异，特别适用于医疗资源匮乏地区。该框架支持从原始呼吸音到临床决策的多层级分析，为开发可部署的数字听诊工具奠定了基础，但需进一步开展多中心外部验证以评估跨设备和真实环境表现。
