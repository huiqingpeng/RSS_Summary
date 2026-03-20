---
title: "Fourier Learning Machines: Nonharmonic Fourier-Based Neural Networks for Scientific Machine Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.08759"
published: "2026-03-20"
summarized: "2026-03-20T14:07:22.570797"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了傅里叶学习机（Fourier Learning Machine, FLM），一种能够表示多维非谐波傅里叶级数的神经网络架构。FLM采用简单的前馈结构配合余弦激活函数，将频率、振幅和相位偏移作为可训练参数进行学习，从而构建问题特定的谱基，适用于周期性和非周期函数。该架构首次实现了用标准多层感知机结构完整表示多维傅里叶级数的可分离基函数形式，并在偏微分方程和最优控制问题上展现出与SIREN等成熟架构相当甚至更优的性能。

【方法概述 / Method】
FLM的核心设计是使用余弦激活函数的前馈网络，通过可训练参数直接学习非谐波傅里叶级数的频率、振幅和相位偏移。该方法建立了傅里叶系数与振幅-相位形式之间的一一对应关系，实现了完整可分离基与余弦相移形式之间的等价转换，同时保持了标准MLP的简洁架构。

【实验结果 / Results】
计算实验表明，FLM在多个科学计算基准测试（包括偏微分方程和最优控制问题）上的性能与SIREN及普通前馈神经网络相当，且经常表现更优。FLM能够自适应地学习目标函数的问题特定谱基，有效处理周期性和非周期函数。

【应用价值 / Applications】
FLM为科学机器学习（Scientific Machine Learning）提供了新的神经网络架构选择，特别适用于物理信息神经网络（PINNs）、偏微分方程求解和最优控制问题等领域。其可解释的谱学习能力和简洁的MLP结构使其成为现有傅里叶神经算子方法的有力替代方案，在需要高效频域表示的科学计算任务中具有重要应用价值。
