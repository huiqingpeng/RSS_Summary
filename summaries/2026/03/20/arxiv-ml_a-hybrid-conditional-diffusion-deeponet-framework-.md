---
title: "A Hybrid Conditional Diffusion-DeepONet Framework for High-Fidelity Stress Prediction in Hyperelastic Materials"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18225"
published: "2026-03-20"
summarized: "2026-03-20T13:10:45.448007"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种混合代理框架cDDPM-DeepONet，用于解决超弹性材料中应力场预测的挑战。该框架将应力形态与幅度解耦：基于UNet的条件去噪扩散概率模型(cDDPM)生成归一化的von Mises应力场，同时改进的DeepONet预测全局缩放参数（最小和最大应力）。实验表明，该模型在单孔和多孔超弹性数据集上比UNet、DeepONet和独立cDDPM基线方法优一到两个数量级，并在所有波数上与有限元解保持良好的一致性。

【方法概述 / Method】

该研究采用"分而治之"的策略，将应力预测任务分解为形态生成和幅度缩放两个子任务。具体而言，cDDPM负责在归一化空间中生成应力场的空间结构，而DeepONet分支则学习从几何和载荷条件到全局应力范围的映射，最终通过反归一化重建物理尺度的完整应力场。

【实验结果 / Results】

cDDPM-DeepONet在具有复杂微结构的非线性超弹性数据集上实现了显著的性能提升，误差比现有基线方法降低1-2个数量级。频谱分析表明，该框架能够有效捕捉从低频全局行为到高频局部应力集中的全频谱特征，克服了传统卷积网络的过度平滑问题和神经算子的谱偏置问题。

【应用价值 / Applications】

该研究为超弹性材料（如橡胶、生物组织等）的快速应力分析提供了高精度代理模型，可显著加速工程设计和优化迭代。其解耦架构思想也可推广至其他具有多尺度动态范围的物理场预测问题，如流体力学、热传导等领域的高保真仿真。
