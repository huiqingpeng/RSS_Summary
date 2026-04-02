---
title: "Lipschitz Dueling Bandits over Continuous Action Spaces"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00523"
published: "2026-04-02"
summarized: "2026-04-03T07:22:24.349482"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文首次研究了连续动作空间上具有Lipschitz结构的随机对决多臂老虎机问题，其中反馈仅包含比较信息。作者提出了首个针对Lipschitz对决老虎机的算法，该算法采用基于轮次的探索和由自适应参考臂引导的递归区域消除策略。研究证明了算法的遗憾界为$\tilde O\left(T^{\frac{d_z+1}{d_z+2}}\right)$，其中$d_z$为近优区域的缩放维度，且算法仅需对数级存储空间。

【方法概述 / Method】
该算法结合轮次式探索机制与递归区域消除技术，通过维护一个自适应参考臂来指导比较过程，从而在连续动作空间中有效定位最优动作。核心创新在于开发了适用于相对反馈的新型分析工具，以处理纯比较反馈下的Lipschitz结构学习问题。

【实验结果 / Results】
理论分析表明，算法达到了$\tilde O\left(T^{\frac{d_z+1}{d_z+2}}\right)$的累积遗憾上界，该结果依赖于近优区域的缩放维度$d_z$而非环境维度。此外，算法在空间复杂度上仅需$O(\log T)$的存储开销，这是连续动作空间老虎机算法所能达到的最优空间效率。

【应用价值 / Applications】
该研究适用于需要从成对比较反馈中学习最优决策的连续优化场景，如个性化推荐系统中的偏好学习、医疗治疗方案的对比优化、以及自动驾驶或机器人控制中的连续参数调优。其低空间复杂度特性使其特别适合资源受限的在线学习系统部署。
