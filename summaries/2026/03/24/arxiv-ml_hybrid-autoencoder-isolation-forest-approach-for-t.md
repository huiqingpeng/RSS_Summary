---
title: "Hybrid Autoencoder-Isolation Forest approach for time series anomaly detection in C70XP cyclotron operation data at ARRONAX"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20335"
published: "2026-03-24"
summarized: "2026-03-25T07:08:00.019661"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究针对ARRONAX机构C70XP回旋加速器（用于医疗和研究用放射性同位素生产）的复杂系统故障问题，提出了一种混合机器学习方法用于早期异常检测。研究将全连接自编码器（AE）与孤立森林（IF）相结合，利用AE重构传感器数据的平均立方误差（MCE）作为IF的输入，以克服传统IF因轴平行分割而难以检测靠近正常数据均值区域的细微异常的局限性。在质子束流强度时间序列数据上的验证表明，该方法显著提升了异常检测性能。

【方法概述 / Method】
该方法采用两阶段混合架构：首先使用全连接自编码器学习正常数据的低维表示并进行重构，计算原始输入与重构输出之间的平均立方误差（MCE）作为重构误差度量；随后将MCE序列输入孤立森林模型进行异常判定，通过自编码器的非线性特征提取能力增强IF对细微异常的敏感性。

【实验结果 / Results】
实验在ARRONAX C70XP回旋加速器的质子束流强度时间序列数据上进行验证，结果表明所提出的AE-IF混合方法相比传统孤立森林具有更优的检测性能，能够有效识别靠近正常数据分布中心的细微异常模式，实现了早期异常检测的目标。

【应用价值 / Applications】
该研究可直接应用于大型粒子加速器、核医学设备等复杂工业系统的预测性维护，通过实时监测传感器数据实现故障早期预警，减少非计划停机时间和维护成本；其混合架构思路亦可推广至其他高维时间序列异常检测场景，为关键基础设施的智能运维提供技术支撑。
