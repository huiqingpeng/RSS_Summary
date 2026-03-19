---
title: "On the Dynamic Regret of Following the Regularized Leader: Optimism with History Pruning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.22899"
published: "2026-03-19"
summarized: "2026-03-19T13:20:59.079621"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文重新审视了Follow the Regularized Leader (FTRL)框架在在线凸优化(OCO)中的动态遗憾(dynamic regret)保证问题。研究表明，通过乐观地组合未来成本并仔细线性化（甚至剪枝）过去成本，FTRL能够恢复已知的动态遗憾界，打破了此前认为FTRL在动态环境中因"惰性"迭代而受限的观点。该分析为在惰性更新与敏捷更新之间进行原则性插值提供了新方法，并带来了对遗憾项的精细控制、无循环依赖的乐观性以及类似AdaFTRL的最小递归正则化等优势。

【方法概述 / Method】

论文核心方法是将FTRL与乐观在线学习(optimistic online learning)相结合，通过对历史线性化成本进行"剪枝"(history pruning)来同步算法状态与迭代点。具体而言，作者采用乐观预测的未来成本与经过选择性剪枝的过去线性化成本相组合，使得FTRL的状态不再无界增长，同时允许在必要时灵活调整更新风格。

【实验结果 / Results】

（注：提供的论文摘要中未包含具体实验结果或性能指标数据，该论文主要为理论分析工作。）

【应用价值 / Applications】

该研究为在线凸优化中FTRL类算法的动态环境应用提供了理论基础和算法设计指导，特别适用于需要快速适应非平稳环境的在线决策场景，如在线广告竞价、动态资源分配和实时推荐系统等。通过历史剪枝机制，算法能够在保持计算效率的同时有效跟踪时变最优解，为实际系统中平衡稳定性与响应速度提供了可调参数。
