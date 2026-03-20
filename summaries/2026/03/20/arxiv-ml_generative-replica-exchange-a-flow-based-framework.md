---
title: "Generative Replica-Exchange: A Flow-based Framework for Accelerating Replica Exchange Simulations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18076"
published: "2026-03-20"
summarized: "2026-03-20T13:08:13.684022"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了生成式副本交换（GREX）方法，将深度生成模型整合到副本交换（REX）分子模拟框架中，消除了传统方法对大量中间温度副本的需求。GREX利用训练好的标准化流模型按需生成高温构型，并通过势能约束将其直接映射到目标温度分布，无需目标温度训练数据。该方法将生产模拟简化为单一目标温度副本，同时通过Metropolis交换接受准则保持热力学严谨性，在三个复杂度递增的基准系统上验证了其优越效率和实用性。

【方法概述 / Method】
GREX借鉴储层副本交换（res-REX）思想，采用标准化流（normalizing flows）作为深度生成模型，学习高温构型的分布并支持高效采样；通过势能作为约束条件实现高温构型到目标温度分布的直接映射，利用Metropolis准则确保交换过程的热力学正确性。

【实验结果 / Results】
研究在三个复杂度递增的基准分子系统上验证了GREX方法，结果表明该方法在保持采样准确性的同时显著提升了计算效率；GREX成功将生产模拟压缩至单一目标温度副本，克服了传统REX对大量中间温度梯度的依赖。

【应用价值 / Applications】
GREX可广泛应用于生物大分子模拟、药物设计和材料科学等领域，大幅降低增强采样模拟的计算成本；该方法为复杂分子系统的自由能计算和构象探索提供了高效工具，有望推动计算化学和定量生物学研究的规模化应用。
