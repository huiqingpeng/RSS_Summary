---
title: "Evolution Strategies for Deep RL pretraining"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00066"
published: "2026-04-02"
summarized: "2026-04-03T07:16:35.564607"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究探讨了进化策略（Evolution Strategies, ES）作为深度强化学习（Deep RL, DRL）预训练方法的可行性。尽管ES具有计算成本低、无需梯度计算、部署简单等优势，但其性能通常不及DRL。实验结果表明，ES并未比DRL训练得更快；当用作DRL的预训练步骤时，ES仅在简单环境（Flappy Bird）中带来收益，而在更复杂的任务（Breakout和MuJoCo Walker）中几乎无改进，甚至无法提升训练效率或稳定性。

【方法概述 / Method】

研究系统比较了ES与DRL在多种难度任务上的性能，涵盖简单游戏（Flappy Bird）、中等复杂度游戏（Breakout）以及连续控制任务（MuJoCo Walker）。此外，作者设计了ES预训练+DRL微调的混合训练方案，以验证ES作为预训练初始化是否能加速或稳定DRL后续训练。

【实验结果 / Results】

核心发现包括：（1）ES整体训练速度并未优于DRL；（2）ES预训练仅在简单环境中对DRL有正向迁移效果；（3）在复杂任务中，ES预训练未能提升DRL的训练效率或稳定性，不同参数设置下改善甚微。这些结果对ES作为通用DRL预训练工具的有效性提出了质疑。

【应用价值 / Applications】

该研究为RL算法选择提供了实证依据：对于资源受限的简单决策任务，ES可作为轻量级替代方案；但对于复杂场景，直接采用DRL更为可靠。同时，该工作警示了预训练方法迁移性的环境依赖性，有助于避免在工业RL应用中盲目采用ES预训练策略而浪费计算资源。
