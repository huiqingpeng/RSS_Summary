---
title: "Safe Reinforcement Learning with Preference-based Constraint Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23565"
published: "2026-03-26"
summarized: "2026-03-27T07:14:35.610869"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对安全强化学习中安全约束难以明确指定的问题，提出了一种基于偏好的约束推断方法。作者发现传统的Bradley-Terry模型无法捕捉安全成本的不对称性和重尾特性，导致风险低估。为此，论文提出了Preference-based Constrained RL (PbCRL)框架，引入"死区机制"建模偏好，并结合信噪比损失与两阶段训练策略，实现了更可靠的约束学习与策略优化。

【方法概述 / Method】

PbCRL采用三项核心技术：一是死区机制（dead zone），通过理论证明其能鼓励重尾成本分布，改善约束对齐；二是信噪比（SNR）损失，利用成本方差引导探索；三是两阶段训练策略，降低在线标注负担的同时自适应增强约束满足。该方法以人类偏好反馈替代昂贵的专家演示进行约束推断。

【实验结果 / Results】

实验表明，PbCRL在与真实安全需求的对齐程度上显著优于现有方法，同时在安全性和累积奖励两方面均超越当前最优基线。特别是死区机制有效解决了BT模型的风险低估问题，SNR损失也被验证有利于策略学习。

【应用价值 / Applications】

该研究为安全关键型决策系统（如自动驾驶、医疗机器人、工业控制）提供了一种数据高效且可靠的约束学习方式，无需大量专家演示即可学习复杂、主观的安全约束，具有广泛的实际应用潜力。
