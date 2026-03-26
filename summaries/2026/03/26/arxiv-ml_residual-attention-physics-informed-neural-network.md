---
title: "Residual Attention Physics-Informed Neural Networks for Robust Multiphysics Simulation of Steady-State Electrothermal Energy Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23578"
published: "2026-03-26"
summarized: "2026-03-27T07:15:37.348522"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了残差注意力物理信息神经网络（RA-PINN）框架，用于求解电-热耦合多物理场稳态问题中的速度场、压力场、电势场和温度场。该架构通过统一五场算子公式、残差连接特征传播和注意力引导通道调制，有效捕捉局部耦合结构和陡峭梯度。在四个具有代表性的能源相关基准测试中，RA-PINN相比纯MLP、LSTM-PINN和pLSTM-PINN实现了最优的精度表现，在界面主导和变系数场景中保持了高结构保真度。

【方法概述 / Method】
RA-PINN采用统一五场算子公式将速度、压力、电势、温度及辅助场耦合求解，核心创新在于引入残差连接实现深层特征的高效传播，并结合注意力机制进行通道级特征调制。该方法通过自适应地增强关键物理量的表征能力，有效处理强非线性场耦合、温度依赖系数变化及复杂界面动力学等挑战。

【实验结果 / Results】
在常系数耦合、间接压力规范约束、温度依赖输运和斜界面一致性四类基准测试中，RA-PINN在所有场景下均取得最低的均方误差（MSE）、均方根误差（RMSE）和相对L₂误差。特别是在传统PINN骨干网络经常失效的界面主导区域和变系数设置中，RA-PINN展现出卓越的结构保真度和鲁棒性。

【应用价值 / Applications】
该研究为先进能源系统（包括电流体动力学输运、微流体能收集器和电驱动热调节器）的高效热管理和精确场预测提供了高保真计算框架。RA-PINN可支撑可持续能源应用中复杂电热多物理系统的建模与优化，对提升能源转换效率和设备可靠性具有重要工程价值。
