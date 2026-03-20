---
title: "Stable Deep Reinforcement Learning via Isotropic Gaussian Representations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.19373"
published: "2026-03-20"
summarized: "2026-03-20T14:11:14.865654"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了深度强化学习中的训练不稳定性问题，指出非平稳目标下各向同性高斯嵌入具有理论优势：能够实现线性读出对时变目标的稳定跟踪、在固定方差预算下达到最大熵、并鼓励表征维度的均衡使用。基于这一洞察，作者提出了"草图化各向同性高斯正则化"（Sketched Isotropic Gaussian Regularization）方法，通过实验验证了该方法能在多种领域中提升非平稳环境下的性能，同时减少表征崩溃、神经元休眠和训练不稳定现象。

【方法概述 / Method】
论文核心方法是Sketched Isotropic Gaussian Regularization（SIGR），该技术通过随机投影（sketching）将高维表征映射到低维空间，在该空间中施加各向同性高斯分布约束。具体实现上，该方法计算表征的协方差矩阵，并通过正则化项鼓励其趋近单位矩阵，从而塑造表征分布，且计算开销较低。

【实验结果 / Results】
实验在多个强化学习基准环境（包括Atari游戏和连续控制任务）上进行，结果表明SIGR显著提升了智能体在非平稳条件下的学习稳定性和最终性能。具体而言，该方法有效缓解了表征崩溃（representation collapse）和神经元休眠（neuron dormancy）问题，同时降低了训练过程中的方差和发散风险。

【应用价值 / Applications】
该研究对需要长期稳定训练的深度强化学习系统具有重要价值，尤其适用于非平稳环境如多智能体博弈、持续学习（continual learning）和真实世界机器人控制等场景。SIGR方法简单且计算高效，易于集成到现有深度RL算法中，为提升AI系统的可靠性和适应性提供了实用工具。
