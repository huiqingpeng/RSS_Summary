---
title: "Regret Analysis of Sleeping Competing Bandits"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19700"
published: "2026-03-23"
summarized: "2026-03-24T07:21:31.004936"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了"Sleeping Competing Bandits"框架，将多臂老虎机在线学习与博弈论中的稳定匹配相结合，同时考虑了参与者和臂的可用性随时间任意变化的真实场景。作者扩展了现有竞争老虎机的遗憾定义，推导了新模型的遗憾上界和下界，并证明所提算法在臂数K远大于参与者数N的渐近情况下是最优的。

【方法概述 / Method】
论文将传统的Competing Bandits框架扩展为Sleeping Competing Bandits，允许参与者和臂的可用性随时间动态变化。作者提出了一个算法，通过自然扩展现有竞争老虎机的遗憾定义来分析该问题，并在合理假设下建立了理论保证。

【实验结果 / Results】
所提算法达到了$\mathrm{O}\left(NK\log T_{i}/\Delta^2\right)$的渐近遗憾上界，同时证明了$\mathrm{\Omega}\left( N(K-N+1)\log T_{i}/\Delta^2 \right)$的遗憾下界。当臂数K相对大于参与者数N时，该算法是渐近最优的。

【应用价值 / Applications】
该研究适用于参与者或资源可用性动态变化的在线匹配场景，如动态劳动力市场、云计算资源分配、在线广告竞价等。通过考虑"睡眠"（不可用）状态，模型更贴近现实世界中用户和资源间歇性可用的实际情况，为设计更鲁棒的在线学习系统提供了理论基础。
