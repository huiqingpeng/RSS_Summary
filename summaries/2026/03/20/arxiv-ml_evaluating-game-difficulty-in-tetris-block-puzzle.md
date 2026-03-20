---
title: "Evaluating Game Difficulty in Tetris Block Puzzle"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18994"
published: "2026-03-20"
summarized: "2026-03-20T13:18:45.340092"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了Tetris Block Puzzle（一种在8×8网格上放置方块完成连线的单人随机益智游戏）的游戏难度评估问题。作者采用Stochastic Gumbel AlphaZero（SGAZ）作为评估工具，系统分析了多种规则变体（包括hold块h、预览hold块p以及额外Tetris方块变体）对游戏难度的影响。研究发现增加h和p会降低难度，而添加更多Tetris方块变体（尤其是T-pentomino）会增加难度。该工作为随机益智游戏的设计提供了可复现的评估框架和参考基准。

【方法概述 / Method】
本文采用Stochastic Gumbel AlphaZero（SGAZ）作为核心评估方法，这是一种适用于随机环境的预算感知规划智能体。通过设定有限的模拟预算，SGAZ能够在计算资源受限的情况下实现高效且可复现的规则集比较，克服了传统方法需要大量计算资源的局限。

【实验结果 / Results】
实验结果表明，增加hold块数量（h）和预览hold块（p）会显著降低游戏难度，表现为更高的训练奖励和更快的收敛迭代次数；相反，引入更多Tetris方块变体会增加难度，其中T-pentomino变体导致的收敛速度下降最为明显。SGAZ在小模拟预算下仍能实现强劲的对弈表现。

【应用价值 / Applications】
该研究为游戏设计师提供了系统评估随机益智游戏难度的量化工具和方法，可用于优化游戏规则平衡性和玩家体验。SGAZ的高效评估能力使其适用于快速迭代的游戏开发流程，同时为未来随机益智游戏的人工智能辅助设计建立了可复现的基准参考。
