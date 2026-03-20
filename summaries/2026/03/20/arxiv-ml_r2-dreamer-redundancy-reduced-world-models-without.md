---
title: "R2-Dreamer: Redundancy-Reduced World Models without Decoders or Augmentation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18202"
published: "2026-03-20"
summarized: "2026-03-20T12:08:48.996020"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了R2-Dreamer，一种无需解码器和数据增强的基于图像的模型强化学习（MBRL）框架。该框架通过引入受Barlow Twins启发的冗余减少目标函数作为内部正则化器，有效防止表征崩溃，避免了传统重建方法在任务无关区域浪费容量的问题，也摆脱了对数据增强等外部正则化器的依赖。实验表明，R2-Dreamer在DeepMind Control Suite和Meta-World上与DreamerV3和TD-MPC2等强基线方法性能相当，同时训练速度提升1.59倍，并在包含微小任务相关对象的DMC-Subtle任务上取得显著优势。

【方法概述 / Method】
R2-Dreamer采用解码器自由的架构设计，核心创新是将冗余减少（redundancy-reduction）目标函数整合到世界模型学习中，通过最小化表征向量各维度之间的相关性来实现自监督学习。该方法可直接嵌入现有MBRL框架，无需额外的解码器重建或数据增强操作。

【实验结果 / Results】
在标准基准测试DeepMind Control Suite和Meta-World上，R2-Dreamer达到与DreamerV3和TD-MPC2相当的性能水平，同时训练速度比DreamerV3快1.59倍。在专门设计的DMC-Subtle任务（包含微小且难以察觉的任务相关对象）上，该方法展现出显著的性能提升，验证了其在处理细微视觉线索时的优势。

【应用价值 / Applications】
R2-Dreamer适用于需要高效视觉表征学习的机器人控制和自主决策场景，特别是在计算资源受限或需要快速训练的实际部署环境中。该方法为开发更通用、更高效的基于视觉的强化学习系统提供了新思路，有望推动MBRL在真实世界复杂视觉任务中的应用。
