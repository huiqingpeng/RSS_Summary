---
title: "An Improved Model-Free Decision-Estimation Coefficient with Applications in Adversarial MDPs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.08882"
published: "2026-03-20"
summarized: "2026-03-20T14:08:31.509665"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Dig-DEC（基于信息增益的决策-估计系数），一种无需乐观假设的模型自由DEC框架，通过纯粹的信息增益驱动探索。该框架将乐观DEC的适用范围从随机环境扩展到对抗环境，首次为具有随机转移和对抗奖励的混合MDP在bandit反馈下提供了模型自由的遗憾界，同时显著改进了在线函数估计的收敛速率，在Bellman-complete MDPs中首次实现了与乐观方法相匹配的√T遗憾界。

【方法概述 / Method】
Dig-DEC摒弃了传统乐观DEC中的乐观假设，转而采用信息增益作为探索驱动力，使其能够处理对抗性环境而无需显式的奖励估计器。该方法通过重新设计在线函数估计过程，针对平均估计误差最小化改进了估计器的集中性，针对平方误差最小化重新设计了双时间尺度过程。

【实验结果 / Results】
在在线函数估计方面，平均估计误差的遗憾界从T^(3/4)改进到T^(2/3)（on-policy）、从T^(5/6)改进到T^(7/9)（off-policy）；对于Bellman-complete MDPs中的平方误差最小化，遗憾界从T^(2/3)提升到√T，首次达到与乐观方法（Jin et al., 2021; Xie et al., 2023）相当的性能。

【应用价值 / Applications】
该研究为混合MDP（随机转移+对抗奖励）提供了首个模型自由理论保证，适用于强化学习中的对抗鲁棒决策场景，如在线推荐系统、动态定价和博弈对抗环境。改进的在线函数估计方法可广泛应用于需要高效探索-利用权衡的序列决策问题，特别是在模型未知且环境可能对抗的实际系统中。
