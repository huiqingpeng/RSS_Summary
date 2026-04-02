---
title: "Predicting Wave Reflection and Transmission in Heterogeneous Media via Fourier Operator-Based Transformer Modeling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00132"
published: "2026-04-02"
summarized: "2026-04-03T07:17:34.946844"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文开发了一种基于机器学习的代理模型，用于近似求解一维麦克斯韦方程组，特别关注电磁波在材料界面处的反射和透射现象。该模型采用基于视觉Transformer的框架，通过自回归方式学习物理和频率嵌入，并在隐空间引入傅里叶变换以匹配波数谱。实验表明，尽管存在材料不连续性和未知材料特性，该模型在75个时间步以上的滚动预测中仍能保持10%以下的相对误差。

【方法概述 / Method】
研究采用有限体积（FV）高保真仿真生成训练数据，涵盖初始条件变化和材料光速变化。核心架构为视觉Transformer，通过自回归机制联合学习物理嵌入和频率嵌入，并在隐空间执行傅里叶变换以显式建模波数谱特征。

【实验结果 / Results】
预测误差随时间近似线性增长，在材料界面处出现急剧上升。测试结果显示，在超过75个时间步的自回归预测中，机器学习解的相对误差低于10%，表明模型对不连续界面和未知材料参数具有较好的泛化能力。

【应用价值 / Applications】
该研究为计算电磁学提供了高效的数据驱动替代方案，可加速异质介质中波传播问题的求解，适用于材料设计、电磁仿真优化及实时波动物理预测等场景，显著降低传统数值方法的高计算成本。
