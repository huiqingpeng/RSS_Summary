---
title: "Simulation Distillation: Pretraining World Models in Simulation for Rapid Real-World Adaptation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15759"
published: "2026-03-18"
summarized: "2026-03-18T16:07:42.547804"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出Simulation Distillation (SimDist)，一种sim-to-real迁移框架，通过将模拟器中的结构先验蒸馏到潜在世界模型中，实现快速的真实世界适应。该方法直接从模拟中迁移奖励和价值模型，在部署时无需进行价值学习即可提供密集的规划信号，将真实世界适应简化为短程系统识别问题。在精确操作和四足机器人运动任务中，SimDist在数据效率、稳定性和最终性能方面均显著优于现有方法。

【方法概述 / Method】
SimDist采用两阶段方法：首先在模拟中预训练潜在世界模型、奖励模型和价值模型，然后将这些模型蒸馏到真实世界部署中；在真实世界适应阶段，通过在线规划和监督式动力学微调进行短程系统识别，避免长程信用分配问题。

【实验结果 / Results】
SimDist在精确操作（如插销插入）和四足机器人运动任务上进行了验证，相比现有sim-to-real微调方法，实现了更高的数据效率、更稳定的训练过程和更优的最终性能；该方法仅需少量真实世界数据即可完成快速适应。

【应用价值 / Applications】
SimDist可广泛应用于机器人sim-to-real迁移场景，特别适用于真实世界数据采集成本高昂的低数据环境；其快速稳定适应的特性使其适合工业自动化、服务机器人等需要快速部署和持续适应真实环境动态的应用领域。
