---
title: "Symbolic--KAN: Kolmogorov-Arnold Networks with Discrete Symbolic Structure for Interpretable Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23854"
published: "2026-03-26"
summarized: "2026-03-27T07:17:51.658895"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了符号Kolmogorov-Arnold网络（Symbolic-KAN），一种将离散符号结构嵌入可训练深度网络的新型神经架构，旨在弥合符号回归的可解释性与神经网络可扩展性之间的长期权衡。Symbolic-KAN通过层级门控和符号正则化，将连续混合逐渐锐化为one-hot选择，使每个激活单元最终选定单一解析基元和投影方向，从而无需事后符号拟合即可生成紧凑的闭式表达式。该框架不仅能可靠恢复数据驱动回归和逆动力学系统中的正确基元项和 governing 结构，还可扩展至偏微分方程的正向与逆向物理信息学习，同时构建反映真实解析结构的紧凑符号表示。

【方法概述 / Method】

Symbolic-KAN 将多元函数表示为学习得到的单变量基元与学习得到的标量投影的组合，其训练过程由解析基元库、层级门控机制和符号正则化共同引导。符号正则化通过渐进式锐化策略，将连续的混合权重转化为离散的one-hot选择，实现网络内部结构的符号化离散。

【实验结果 / Results】

实验表明，Symbolic-KAN 能够在数据驱动回归和逆动力学系统中可靠地恢复正确的基元项和 governing 结构；在偏微分方程的正向与逆向物理信息学习任务中，该方法能够直接从 governing 约束产生精确解，并构建出与真实解析结构相符的紧凑符号表示。

【应用价值 / Applications】

Symbolic-KAN 可作为可扩展的基元发现机制，为稀疏方程学习方法识别最相关的解析组件并生成候选库，适用于科学发现、物理定律学习和可解释性要求高的工程建模场景。该研究为构建可扩展、可解释且基于机理的 governing 定律学习系统提供了重要进展。
