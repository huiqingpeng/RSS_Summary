---
title: "Neural Galerkin Normalizing Flow for Transition Probability Density Functions of Diffusion Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18907"
published: "2026-03-20"
summarized: "2026-03-20T12:16:50.981606"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种神经Galerkin归一化流（Neural Galerkin Normalizing Flow）框架，用于通过求解Fokker-Planck方程来近似扩散过程的转移概率密度函数，该方程具有原子型初始分布，并对初始质量位置进行参数化处理。该方法利用归一化流将参考随机过程的转移概率密度函数进行变换来寻找解，确保近似结果保持结构特性，并自动满足正性和质量守恒约束。数值结果表明，该策略能够捕捉真实解的关键特征，并在离线训练完成后，在线评估成本显著低于从头求解偏微分方程。

【方法概述 / Method】
该方法将神经Galerkin方案扩展到归一化流的上下文中，推导出一组常微分方程来描述归一化流参数的时间演化。通过自适应采样策略在关键位置评估Fokker-Planck残差，以有效处理高维偏微分方程问题。核心思想是将解表示为参考过程概率密度的可逆变换，从而天然保持概率密度的物理约束。

【实验结果 / Results】
数值实验表明，该方法能够准确捕捉真实转移概率密度函数的关键特征，并强制建立初始数据与后续时刻密度函数之间的因果关系。在完成离线训练阶段后，在线评估的计算成本大幅降低，显著优于从头求解偏微分方程的传统方法。

【应用价值 / Applications】
该方法可作为高效的代理模型，适用于与随机微分方程相关的多查询问题，如贝叶斯推断、随机过程模拟和扩散桥生成等场景。其快速在线评估能力使其在需要反复求解不同初始条件下转移概率的任务中具有重要实用价值，为扩散模型和随机动力学的计算提供了新的高效工具。
