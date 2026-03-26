---
title: "Embracing Heteroscedasticity for Probabilistic Time Series Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24254"
published: "2026-03-26"
summarized: "2026-03-27T07:22:23.760551"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对概率时间序列预测（PTSF）中异方差性建模的关键挑战，提出了一种新的生成模型框架LSG-VAE。现有方法如TimeVAE和K²VAE依赖MSE训练目标，隐含同方差假设，无法捕捉时变条件方差；而LSG-VAE通过位置-尺度似然公式显式参数化预测均值和时变方差，有效建模异方差性偶然不确定性，并引入自适应衰减机制提升趋势预测鲁棒性。在九个基准数据集上的实验表明，LSG-VAE在保持高计算效率的同时，一致性地超越了十五个强基线模型。

【方法概述 / Method】
LSG-VAE采用变分自编码器架构，其核心创新在于使用位置-尺度（location-scale）似然函数替代传统的MSE损失，使解码器同时输出条件均值和时变标准差。该设计通过高斯分布的负对数似然进行训练，自然实现对高波动观测值的自适应降权，无需人工设计权重策略。

【实验结果 / Results】
实验在九个真实世界时间序列基准数据集上进行，涵盖能源、交通、经济等多个领域。LSG-VAE在概率预测指标（如CRPS、NLL）和点预测精度上均显著优于包括TimeVAE、K²VAE在内的十五个生成式基线模型，同时保持与非自回归方法相当的低延迟特性，适用于实时部署场景。

【应用价值 / Applications】
该研究对需要可靠不确定性量化的决策场景具有重要价值，如电力负荷预测、可再生能源调度、金融风险管理和供应链规划等。LSG-VAE的显式方差建模能力使系统能够识别高风险预测时段，辅助运营者制定更稳健的应对策略，其计算效率也满足工业级实时推理需求。
