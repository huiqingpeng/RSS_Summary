---
title: "Bi-Level Policy Optimization with Nystr\"om Hypergradients"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.11714"
published: "2026-03-19"
summarized: "2026-03-19T13:20:20.540654"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文将Actor-Critic强化学习重新诠释为双层优化（Bilevel Optimization）问题，指出演员（Actor）对评论家（Critic）的依赖关系符合Stackelberg博弈结构。基于此视角，作者提出BLPO算法：一方面通过嵌套更新使评论家学习对演员策略的最优响应，另一方面利用Nyström方法计算超梯度以稳定处理Hessian逆矩阵向量积。理论证明该算法在线性参数化假设下能以多项式时间高概率收敛到局部强Stackelberg均衡，实验表明其在离散与连续控制任务上性能达到或超越PPO。

【方法概述 / Method】

BLPO的核心技术包含两个层面：在算法架构上采用嵌套优化结构，将评论家的更新作为内层优化问题，使其收敛到当前演员策略下的最优价值估计；在梯度计算上引入Nyström低秩近似方法，通过随机采样构建Hessian矩阵的近似分解，从而高效稳定地计算超梯度，避免直接求逆带来的数值不稳定性。

【实验结果 / Results】

实验在多种离散和连续控制基准环境（如MuJoCo任务）上进行对比评估，结果显示BLPO在样本效率与最终回报上均达到或超过PPO的性能水平。消融实验验证了Nyström近似在保持计算效率的同时能够有效近似精确超梯度，且嵌套更新结构对收敛稳定性具有关键作用。

【应用价值 / Applications】

该研究为Actor-Critic类算法的理论分析与算法设计提供了新的双层优化视角，可广泛应用于机器人控制、游戏AI及自动驾驶等需要稳定策略学习的场景。Nyström超梯度计算技术尤其适用于高维连续控制问题，为大规模强化学习系统中的高效二阶优化方法开发提供了可行路径。
