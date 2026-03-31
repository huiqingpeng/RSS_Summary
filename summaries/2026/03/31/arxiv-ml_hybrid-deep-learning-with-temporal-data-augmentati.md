---
title: "Hybrid Deep Learning with Temporal Data Augmentation for Accurate Remaining Useful Life Prediction of Lithium-Ion Batteries"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27186"
published: "2026-03-31"
summarized: "2026-04-01T07:22:39.401577"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究提出了一种名为CDFormer的混合深度学习模型，用于准确预测锂离子电池剩余使用寿命（RUL）。该模型整合了卷积神经网络、深度残差收缩网络和Transformer编码器，以从电压、电流和容量信号中提取多尺度时序特征。为增强预测可靠性，研究还提出了一种复合时序数据增强策略，包含高斯噪声、时间扭曲和时间重采样。实验结果表明，CDFormer在两个真实数据集上均优于传统的循环神经网络和Transformer基线模型。

【方法概述 / Method】
CDFormer采用三阶段混合架构：首先利用卷积神经网络提取局部特征，然后通过深度残差收缩网络进行噪声抑制和特征精炼，最后使用Transformer编码器捕获全局时序依赖关系。为应对数据稀缺问题，研究设计了复合时序数据增强策略，通过引入高斯噪声模拟测量误差、时间扭曲模拟操作条件变化、时间重采样模拟采样率差异，从而提升模型的泛化能力。

【实验结果 / Results】
CDFormer在两个真实世界电池数据集上进行了评估，在关键性能指标上 consistently 优于传统RNN和Transformer基线模型。实验结果证明了该模型在复杂运行条件下具有更强的鲁棒性和泛化能力，能够提供更准确的RUL预测。

【应用价值 / Applications】
该研究为电池健康监测和数据驱动的维护策略提供了可靠的技术支持，可应用于电动汽车、储能系统和便携式电子设备等领域的电池管理系统。通过提高RUL预测的准确性和可靠性，CDFormer有助于优化电池使用策略、降低维护成本、预防突发故障，从而提升整个电池生命周期的安全性和经济性。
