---
title: "Benchmarking Reinforcement Learning via Stochastic Converse Optimality: Generating Systems with Known Optimal Policies"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17631"
published: "2026-03-19"
summarized: "2026-03-19T12:15:07.701913"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对强化学习（RL）算法客观比较困难的问题，提出了一种严格的基准测试框架。该框架通过将逆最优性理论扩展到离散时间、控制仿射、非线性随机系统，建立了使预设值函数和策略成为最优解的充要条件。基于此，研究者能够系统性地生成具有已知最优策略的基准环境族，为RL算法的可控且全面的评估提供了可复现的基础。

【方法概述 / Method】
论文采用随机逆最优性（stochastic converse optimality）方法，构造满足特定最优性条件的控制系统。通过同伦变体（homotopy variations）和随机化参数，自动生成多样化的测试环境，确保每个环境都有理论上的最优策略作为评估基准。

【实验结果 / Results】
该框架成功实现了多样化环境的自动构建，并用于对标准RL算法进行系统性评估。实验展示了框架在控制条件下全面比较不同算法性能的能力，验证了其作为严格RL基准测试工具的有效性。

【应用价值 / Applications】
该研究为RL算法开发者和研究者提供了可复现、有理论保障的评估工具，解决了传统基准测试中因环境设计、奖励结构和随机性导致的比较偏差问题。适用于算法选型、超参数调优和新方法验证等场景，推动RL领域的科学化和标准化发展。
