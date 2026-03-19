---
title: "Rewarding DINO: Predicting Dense Rewards with Vision Foundation Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16978"
published: "2026-03-19"
summarized: "2026-03-19T13:07:59.982229"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Rewarding DINO，一种基于视觉基础模型的语言条件密集奖励建模方法。该方法能够从相机图像中推断任务状态信息，学习通用的奖励函数而非特定轨迹，解决了传统方法依赖专家演示且泛化能力不足的问题。实验表明，该模型在24个Meta-World+任务上训练后，在训练集任务中表现优异，并能泛化到仿真和真实世界的新场景，同时可直接与现成的强化学习算法结合使用。

【方法概述 / Method】
Rewarding DINO采用紧凑的视觉模型架构，通过基于排名的损失函数（rank-based loss）在从Meta-World+任务采样的数据上进行训练。该方法以语言指令为条件，从视觉输入中预测密集奖励，而非直接模仿专家轨迹，从而学习真正的任务语义而非特定解决方案。

【实验结果 / Results】
实验评估了模型的成对准确率（pairwise accuracy）、排名相关性（rank correlation）和校准度（calibration），结果显示其在训练任务上具有竞争力。更重要的是，模型成功泛化到仿真和真实世界的新环境设置，证明了其对任务语义的学习能力。此外，该模型可直接替代分析型奖励函数，与现成的强化学习算法结合完成训练任务。

【应用价值 / Applications】
该研究为机器人操作任务提供了实用的密集奖励预测方案，特别适用于真实世界场景——传统方法依赖的特权状态信息往往无法获取。Rewarding DINO的低计算开销使其可直接部署于实际机器人系统，支持语言条件控制，有望简化机器人技能学习流程，降低奖励工程的人力成本。
