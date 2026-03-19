---
title: "CircuitBuilder: From Polynomials to Circuits via Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17075"
published: "2026-03-19"
summarized: "2026-03-19T12:07:25.158310"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了使用强化学习自动发现计算多项式的高效算术电路问题，这一问题与自动证明生成和Valiant的VP vs. VNP猜想密切相关。作者将电路构建形式化为单人游戏，并实现了AlphaZero风格的训练循环，比较了PPO+MCTS和SAC两种方法。实验表明SAC在两变量目标上成功率最高，而PPO+MCTS能扩展到三变量并在更难实例上持续改进，证明多项式电路合成是研究自改进搜索策略的紧凑且可验证的理想场景。

【方法概述 / Method】
作者将算术电路合成问题建模为单人游戏，其中RL智能体在固定操作次数内通过加法和乘法门构建电路。采用AlphaZero风格的训练框架，实现了两种强化学习方法：基于蒙特卡洛树搜索的近端策略优化（PPO+MCTS）和软演员-评论家算法（SAC）。

【实验结果 / Results】
SAC在两变量多项式目标上取得了最高的成功率；PPO+MCTS成功扩展到三变量问题，并在更具挑战性的实例上展现出稳定的性能提升。两种方法各有优势，SAC更适合低维问题，而PPO+MCTS具有更好的可扩展性。

【应用价值 / Applications】
该研究为自动证明生成提供了新工具，有助于推进计算复杂性理论中VP vs. VNP猜想的研究。所提出的强化学习框架可应用于自动化数学发现、优化编译器中的代数表达式求值，以及为科学计算设计更高效的专用硬件电路。
