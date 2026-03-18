---
title: "Electrodermal Activity as a Unimodal Signal for Aerobic Exercise Detection in Wearable Sensors"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15880"
published: "2026-03-18"
summarized: "2026-03-18T15:36:41.257469"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究探讨了皮肤电活动（EDA）作为单一模态信号在可穿戴设备中区分持续有氧运动与静息状态的可行性。研究使用30名健康受试者的公开数据集，采用留一受试者交叉验证（LOSO）评估多种机器学习模型，发现仅基于EDA特征的分类器在中等程度上实现了受试者独立的有氧运动检测。研究明确了EDA单独作为可穿戴活动状态推断输入的判别能力边界，而非主张其替代多模态传感方案。

【方法概述 / Method】
研究从公开数据集中提取EDA信号特征，包括时相性动态（phasic temporal dynamics）和事件时间特征，并采用留一受试者交叉验证（LOSO）确保受试者独立性。评估了多种基准机器学习模型对有氧运动与静息状态的二分类性能。

【实验结果 / Results】
EDA单模态分类器在受试者独立评估中取得了中等水平的分类性能，其中时相性时间动态特征和事件时间特征对类别分离贡献显著。研究未报告具体准确率数值，但强调性能明显低于多模态方法，证实了EDA单独使用的局限性。

【应用价值 / Applications】
该研究为可穿戴设备设计提供了重要参考：当心率或加速度计等传感器不可用或功耗受限时，EDA可作为备用或补充信号进行活动状态推断。研究结果有助于理解各生理信号的贡献边界，指导低功耗、简约型可穿戴系统的算法优化与传感器配置决策。
