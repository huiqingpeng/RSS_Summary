---
title: "The Phasor Transformer: Resolving Attention Bottlenecks on the Unit Circle"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17433"
published: "2026-03-19"
summarized: "2026-03-19T12:11:50.598738"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Phasor Transformer，一种基于单位圆流形$S^1$的相位原生替代方案，用于解决标准Transformer中点积自注意力在长序列时间序列建模中的二次复杂度瓶颈。该架构通过可学习的轻量级相移与无参数的离散傅里叶变换(DFT)实现全局$O(N\log N)$的token混合，构建了Large Phasor Model (LPM)。实验表明，在紧凑参数预算下，LPM能够学习稳定的全局动态，并在自回归时间序列预测任务上取得与传统自注意力基线相当的表现，为振荡域的可扩展时间建模提供了新路径。

【方法概述 / Method】
Phasor Transformer将序列状态表示在单位圆流形上，每个模块结合可训练的轻量级相移操作与无参数的DFT进行token耦合，完全摒弃显式的注意力图计算。通过堆叠这些模块构建LPM架构，利用相位运算的几何约束实现确定性的全局信息交互。

【实验结果 / Results】
在合成多频率基准测试的自回归时间序列预测任务上，LPM以高度紧凑的参数预算实现了与传统自注意力基线可比的预测性能。模型展现出稳定的全局动态学习能力，确立了明确的效率-性能前沿，证明大模型缩放可从几何约束的相位计算中涌现。

【应用价值 / Applications】
该研究为长上下文时间序列建模（如金融预测、气候模拟、信号处理等振荡域应用）提供了计算高效的可扩展方案。其$O(N\log N)$复杂度特性使其特别适用于需要处理极长序列的实时系统，同时确定性全局耦合机制为需要可解释性和稳定性的科学计算场景提供了实用工具。
