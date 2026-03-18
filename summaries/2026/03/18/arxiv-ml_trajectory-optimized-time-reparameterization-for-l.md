---
title: "Trajectory-Optimized Time Reparameterization for Learning-Compatible Reduced-Order Modeling of Stiff Dynamical Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16583"
published: "2026-03-18"
summarized: "2026-03-18T15:45:43.650637"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对刚性动力系统（stiff dynamical systems）在机器学习降阶模型（ML-ROMs）中的训练难题，提出了一种轨迹优化的时间重参数化方法（TOTR）。传统显式时间积分在刚性区域不稳定，而隐式积分计算成本高昂且降低训练效率；时间重参数化通过拉伸时间坐标来平滑快速瞬态，但现有方法对学习效果的影响尚不明确。TOTR将时间重参数化建模为弧长坐标下的优化问题，通过惩罚拉伸时间中的加速度来优化遍历速度曲线，从而生成更平滑、更易学习的重参数化轨迹。在三个刚性系统上的实验表明，该方法相比基准算法可将损失降低1-2个数量级。

【方法概述 / Method】

TOTR将时间重参数化转化为以弧长为坐标的优化问题，其中优化变量为遍历速度曲线（traversal-speed profile），目标函数惩罚拉伸时间坐标下的轨迹加速度。该优化框架直接针对训练动力学的平滑性进行设计，使得重参数化后的轨迹具有更好的条件数和可学习性，避免了启发式时间重参数化方法的局限性。

【实验结果 / Results】

作者在三个刚性问题上验证了TOTR：参数化刚性线性系统、van der Pol振子和HIRES化学反应动力学模型。实验结果表明，在相同训练配置下，TOTR生成的重参数化轨迹比其他方法更平滑，物理时间预测精度更高；定量结果显示损失函数值相比基准算法降低1-2个数量级，显著提升了神经ODE降阶模型的训练效果。

【应用价值 / Applications】

该方法适用于多尺度刚性动力系统的机器学习降阶建模，如化学反应动力学、电路仿真、流体力学等领域中同时包含快慢时间尺度的复杂系统。TOTR通过优化驱动的时间重参数化实现了稳定高效的显式积分，为计算昂贵的隐式方法提供了实用替代方案，有望加速数字孪生、实时仿真和参数化设计优化等应用场景。
