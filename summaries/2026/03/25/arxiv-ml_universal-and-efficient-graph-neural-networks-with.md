---
title: "Universal and efficient graph neural networks with dynamic attention for machine learning interatomic potentials"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22810"
published: "2026-03-25"
summarized: "2026-03-26T07:17:28.920271"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MLANet，一种高效且鲁棒的图神经网络框架，用于机器学习原子间势（MLIPs）。该框架创新性地引入了双路径动态注意力机制进行几何感知消息传递，并结合多视角池化策略构建全面的系统表征。实验表明，MLANet在保持与主流等变模型相当预测精度的同时，计算成本显著降低，并能实现稳定的长时分子动力学模拟。

【方法概述 / Method】
MLANet采用双路径动态注意力机制，使模型能够根据原子间的几何关系动态调整消息传递过程，实现对原子环境的精确建模。同时，通过多视角池化策略整合不同层次的结构信息，构建完整的系统表征，兼顾了模型的表达能力与计算效率。

【实验结果 / Results】
MLANet在多个多样化数据集上进行了验证，包括有机分子（QM7、MD17）、周期性无机材料（含锂晶体）、二维材料（双层石墨烯、黑磷）、表面催化反应（甲酸分解）及带电体系。结果表明，该模型在预测精度上具有竞争力，而计算成本明显低于主流等变模型，且支持稳定的长时分子动力学模拟。

【应用价值 / Applications】
MLANet为大规模、高精度的原子模拟提供了实用工具，可广泛应用于材料科学、催化化学和能源材料等领域。其高效性使得以往受限于计算资源的复杂体系模拟成为可能，有望加速新材料发现和反应机理研究，推动机器学习势函数在实际科研和工业应用中的普及。
