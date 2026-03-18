---
title: "Spectral Edge Dynamics of Training Trajectories: Signal--Noise Geometry Across Scales"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15678"
published: "2026-03-18"
summarized: "2026-03-18T15:33:47.452161"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了**谱边缘动力学（Spectral Edge Dynamics, SED）**框架，用于量化Transformer训练轨迹的低维结构：通过滑动窗口SVD分析参数更新，识别出"谱边缘"——即连贯优化方向与随机噪声之间的尖锐边界。研究发现该边缘呈现普遍的三阶段模式（上升-平台-崩溃），信号秩随任务复杂度自适应调整，且谱几何与验证损失的定向耦合存在窗口尺度依赖的"滞后翻转"现象。该方法可经Johnson-Lindenstrauss投影高效扩展到任意规模模型，并在相关工作中成功预测grokking现象的发生。

【方法概述 / Method】

SED核心方法是对训练过程中的参数更新进行滚动窗口奇异值分解（SVD），以最大连续奇异值比σ_k/σ_{k+1}作为谱边缘的识别指标，区分信号子空间与噪声子空间。为提升可扩展性，采用Johnson-Lindenstrauss随机投影将高维参数空间降至d=10W维度（W为窗口大小），在保持谱间隙5.7%精度损失的同时实现计算效率。

【实验结果 / Results】

在51M参数的TinyStories模型（4个随机种子）和124M参数的GPT-2分布迁移任务上，谱边缘均呈现"上升-平台-崩溃"的三阶段普适模式，且有效信号秩随模型规模增加（k*=2→k*=3）。关键发现是谱几何与验证损失的相关性方向随窗口大小发生反转——小窗口呈正相关，大窗口呈负相关，揭示训练轨迹整合的时间尺度效应。投影降维后SED框架保持有效性，验证了跨尺度适用性。

【应用价值 / Applications】

SED为神经网络训练动态提供了可解释的低维分析工具，可实时监控优化过程的有效维度与噪声水平，指导学习率调度和早停策略。在配套工作中，该谱几何框架已成功用于预测grokking现象（在模运算、Dyck语言和SCAN基准上提前600-1700步预警泛化发生），为理解深度学习的隐式正则化和泛化机制开辟了新途径，适用于大规模语言模型的训练诊断与效率优化。
