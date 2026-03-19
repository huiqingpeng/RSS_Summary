---
title: "Slow-Fast Policy Optimization: Reposition-Before-Update for LLM Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.04072"
published: "2026-03-19"
summarized: "2026-03-19T14:07:37.275825"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Slow-Fast Policy Optimization (SFPO)，一种用于大语言模型推理强化学习的新型训练框架，旨在解决GRPO等在线策略算法早期训练中因低质量rollout导致梯度噪声大、更新不稳定的问题。SFPO通过将每个训练步骤分解为"快速内步轨迹—重定位机制—慢速修正"三个阶段，在保持原有目标和rollout流程不变的前提下实现了与现有策略梯度管道的即插即用兼容。实验表明，SFPO在数学推理基准上平均比GRPO提升2.80分，同时实现最多4.93倍的rollout数量减少和4.19倍的墙钟时间缩短。

【方法概述 / Method】
SFPO采用"重定位-再更新"（reposition-before-update）的核心设计，将传统单步更新分解为三个子阶段：首先在相同批次上执行短时间的快速内步轨迹计算，然后通过重定位机制控制离策略漂移（off-policy drift），最后进行慢速修正更新。该方法完全保留了原始策略优化的目标函数和rollout采样过程，仅修改了优化器的内部更新逻辑，因此可与GRPO等现有RL训练流程无缝集成。

【实验结果 / Results】
在数学推理基准测试中，SFPO相比GRPO平均提升2.80分；在训练效率方面，SFPO达到与GRPO最佳精度相比，rollout数量减少最多达4.93倍，墙钟时间缩短最多达4.19倍。这些结果表明SFPO显著提升了推理强化学习训练的稳定性和收敛速度。

【应用价值 / Applications】
SFPO可直接应用于基于强化学习的大语言模型推理能力提升场景，如数学问题求解、代码生成等需要多步推理的任务。该框架的即插即用特性使其易于部署到现有的RLHF和推理训练管线中，帮助研究者和工程师在降低计算成本的同时加速模型收敛，对大规模语言模型的高效训练具有重要实践意义。
