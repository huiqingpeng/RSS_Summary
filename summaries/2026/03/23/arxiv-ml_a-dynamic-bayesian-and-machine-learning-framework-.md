---
title: "A Dynamic Bayesian and Machine Learning Framework for Quantitative Evaluation and Prediction of Operator Situation Awareness in Nuclear Power Plants"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19298"
published: "2026-03-23"
summarized: "2026-03-24T07:15:55.072440"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究针对核电站控制室中操作员情境意识（Situation Awareness, SA）评估的局限性，提出了动态贝叶斯机器学习框架（DBML SA）。该框架融合概率推理与数据驱动智能，实现了对情境意识的定量、可解释和预测性建模。基于2007-2021年间212份运行事件报告，研究重建了11个绩效形成因子（PSFs）在多认知层级的因果时序结构，识别出培训质量和压力动态是情境意识退化的主要驱动因素，为下一代数字主控室的智能人机可靠性管理奠定了基础。

【方法概述 / Method】
DBML SA框架由两部分组成：贝叶斯组件利用动态贝叶斯网络实现不确定性下情境意识可靠性的时序推理；神经网络组件则建立从绩效形成因子到SART评分的非线性预测映射。该框架通过整合概率图模型与机器学习方法，克服了传统SAGAT和SART等静态、回顾性评估方法的不足。

【实验结果 / Results】
神经网络预测组件实现了13.8%的平均绝对百分比误差（MAPE），且与主观评估结果具有统计一致性（p > 0.05）。敏感性分析表明，培训质量和压力动态是情境意识退化的首要影响因素。该框架能够进行实时认知监测、敏感性分析和早期预警预测，显著超越了传统的问卷式评估方法。

【应用价值 / Applications】
DBML SA框架可部署于下一代核电站数字主控室，实现操作员认知状态的实时监测与预警，提升人机系统的整体可靠性。该研究为高风险工业环境中的人类可靠性分析（HRA）提供了智能化工具，可推广至航空、化工等其他复杂人机交互领域的情境意识评估与风险管理。
