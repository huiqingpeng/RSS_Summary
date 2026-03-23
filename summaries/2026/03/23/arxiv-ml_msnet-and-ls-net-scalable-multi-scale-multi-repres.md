---
title: "MSNet and LS-Net: Scalable Multi-Scale Multi-Representation Networks for Time Series Classification"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19315"
published: "2026-03-23"
summarized: "2026-03-24T07:16:56.788400"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一个可扩展的多尺度卷积框架，用于单变量时间序列分类（TSC），通过系统性地整合结构化多表示输入来提升性能。作者引入了两个架构：MSNet（面向鲁棒性和校准的层次化多尺度网络）和LS-Net（面向高效部署的轻量级变体），并将多变量模型LiteMV适配到单变量多表示信号。在142个基准数据集上的评估表明，LiteMV达到最高平均准确率，MSNet具有最优的概率校准（最低NLL），而LS-Net实现了最佳的效率-准确率权衡，确立了多表示多尺度学习作为现代TSC的原则性实用方向。

【方法概述 / Method】
论文采用多尺度卷积框架，通过生成时间序列的多种结构化表示（如原始序列、统计特征、频域变换等）作为网络输入，实现跨表示交互。MSNet采用层次化多尺度卷积结构，LS-Net通过精简设计降低计算复杂度，而LiteMV则通过注意力机制实现多表示之间的信息融合。

【实验结果 / Results】
在142个基准数据集的统一实验协议下，Critical Difference分析证实了顶级模型间存在统计显著性差异：LiteMV平均准确率最高，MSNet的负对数似然（NLL）最低表明其概率校准最优，LS-Net在效率-准确率权衡上表现最佳。Pareto分析进一步证明多表示多尺度建模提供了灵活的设计空间，可针对不同需求进行调优。

【应用价值 / Applications】
该研究为时间序列分类提供了可扩展的实用解决方案，适用于资源受限的边缘设备部署（LS-Net）、高精度要求的决策系统（LiteMV）以及需要可靠概率预测的风险敏感场景（MSNet）。多表示多尺度框架的灵活性使其可根据具体应用需求在准确率、校准性能和计算效率之间进行针对性优化。
