---
title: "The Spectral Edge Thesis: A Mathematical Framework for Intra-Signal Phase Transitions in Neural Network Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.28964"
published: "2026-04-01"
summarized: "2026-04-02T07:14:13.260281"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了"谱边缘论题"(Spectral Edge Thesis)，为神经网络训练中的相变现象（如grokking、能力跃升、损失平台期）建立了统一的数学框架。核心发现是这些相变由参数更新的滚动窗口Gram矩阵的谱间隙控制，而非传统的BBP检测阈值。作者从三条公理出发，推导出谱间隙动力学方程、谱损失分解以及"间隙最大性原理"，并引入绝热参数$\mathcal{A}$来刻画电路稳定性。在六种模型家族（150K-124M参数）上的实验验证了该框架的预测能力，24/24的grokking事件前均出现间隙动态变化，且19/20的定量预测得到确认。

【方法概述 / Method】

论文采用极端纵横比 regime（参数$P\sim 10^8$，窗口$W\sim 10$）下的随机矩阵理论分析方法，关注主导模式与次主导模式之间的"信号内间隙"(intra-signal gap)。通过三条公理建立数学框架：推导Dyson型常微分方程描述间隙动力学（包含曲率不对称性、阻尼和梯度驱动项），利用Davis-Kahan稳定性系数建立谱损失分解，并提出间隙最大性原理说明$k^*$位置的动态特权性。实验覆盖六种模型架构，对比了不同优化器（Muon、AdamW）和正则化策略的影响。

【实验结果 / Results】

关键实验发现包括：谱间隙动态变化先于所有grokking事件发生（带权重衰减时24/24，无权重衰减时0/24）；间隙位置$k^*$具有优化器依赖性（相同模型上Muon为$k^*=1$，AdamW为$k^*=2$）；绝热参数$\mathcal{A}$有效区分三种训练状态——$\mathcal{A}\ll 1$对应平台期，$\mathcal{A}\sim 1$对应相变，$\mathcal{A}\gg 1$对应遗忘。框架的19/20定量预测得到实验验证，且与边缘稳定性、Tensor Programs、Dyson布朗运动、彩票假说及神经标度律等现有理论一致。

【应用价值 / Applications】

该框架为理解和预测神经网络训练中的关键相变现象提供了可量化的数学工具，可指导超参数调优（特别是权重衰减和优化器选择）以诱导或避免特定相变。间隙最大性原理和绝热参数$\mathcal{A}$为设计更稳定的训练动态、防止灾难性遗忘提供了理论依据。此外，该工作与彩票假说和神经标度律的兼容性表明其可能促进高效模型压缩和大规模训练策略的开发。
