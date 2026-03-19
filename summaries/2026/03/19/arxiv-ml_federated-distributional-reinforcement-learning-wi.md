---
title: "Federated Distributional Reinforcement Learning with Distributional Critic Regularization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17820"
published: "2026-03-19"
summarized: "2026-03-19T12:16:56.124561"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了联邦分布式强化学习（FedDistRL）框架，解决了传统联邦强化学习中参数平均导致分布多模态和尾部信息丢失的问题。作者进一步提出TR-FedDistRL方法，通过构建基于Wasserstein重心（barycenter）的分布信任区域来约束参数平均过程。理论分析证明了该方法的收缩性和非扩张性，实验表明其在安全性关键指标上显著优于基线方法。

【方法概述 / Method】
该方法采用分位数价值函数作为客户端的critic网络，仅联邦化这些网络参数。TR-FedDistRL在每个客户端维护一个时间缓冲区，构建风险感知的Wasserstein重心作为参考区域，并通过"收缩-挤压"（shrink-squash）步骤实现分布信任区域约束，防止联邦过程中的分布信息被平均抹除。

【实验结果 / Results】
实验在赌博机、多智能体网格世界和连续高速公路环境中进行，结果显示该方法有效减少了均值抹除（mean-smearing）现象，显著降低了灾难/事故率等安全代理指标，同时critic和策略的漂移程度也低于面向均值的基线方法和非联邦基线。

【应用价值 / Applications】
该研究适用于自动驾驶、机器人控制等安全关键场景，能够在保护数据隐私的联邦学习框架下准确捕捉回报分布的尾部风险。其分布感知特性使其特别适合需要风险评估和鲁棒决策的分布式多智能体系统。
