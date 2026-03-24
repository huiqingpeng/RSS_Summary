---
title: "JointFM-0.1: A Foundation Model for Multi-Target Joint Distributional Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20266"
published: "2026-03-24"
summarized: "2026-03-25T07:06:58.118312"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了JointFM-0.1，这是首个用于多目标联合分布预测的基础模型。该模型颠覆了传统的随机微分方程（SDE）建模范式，不再将SDE拟合到数据，而是通过采样无限流的合成SDE来训练一个通用模型，直接预测未来的联合概率分布。在纯零样本设置下，JointFM在恢复未见合成SDE生成的oracle联合分布时，相比最强基线将能量损失降低了14.2%，且无需任务特定的校准或微调。

【方法概述 / Method】

JointFM采用"逆向范式"训练策略，通过生成无限流的合成SDE数据来训练基础模型，使其学习直接预测联合概率分布而非拟合特定SDE参数。该模型专门针对耦合时间序列的联合分布预测进行设计，实现了任务无关的通用分布预测能力。

【实验结果 / Results】

在零样本（zero-shot）设置下，JointFM在恢复oracle联合分布任务上表现优异，能量损失相比最强基线降低14.2%。实验表明该模型无需针对特定任务进行校准或微调，即可有效处理未见过的合成SDE生成的分布预测任务。

【应用价值 / Applications】

JointFM为复杂系统的不确定性建模提供了高效替代方案，可应用于金融风险管理、气候预测、多变量时间序列预测等需要联合分布推断的场景。该模型显著降低了传统SDE方法的高建模风险、脆弱校准和高计算成本等实际部署障碍。
