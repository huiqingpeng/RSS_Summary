---
title: "Context-Nav: Context-Driven Exploration and Viewpoint-Aware 3D Spatial Reasoning for Instance Navigation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.09506"
published: "2026-03-19"
summarized: "2026-03-19T16:32:07.586851"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 Context-Nav，一种用于文本目标实例导航（TGIN）的新方法。该方法将长文本描述从局部匹配线索提升为全局探索先验，并通过3D空间推理验证候选目标。Context-Nav 无需任务特定训练或微调，在 InstanceNav 和 CoIN-Bench 基准上达到了最先进的性能，证明了基于几何的空间推理可作为精细实例消歧的可扩展替代方案。

【方法概述 / Method】

Context-Nav 包含两个核心组件：（1）基于密集文本-图像对齐的价值地图，用于对边界前沿进行排序，引导智能体向与完整描述一致的区域探索；（2）视角感知的关系验证机制，智能体采样合理的观察姿态，对齐局部坐标系，仅当空间关系能从至少一个视角满足时才接受目标。

【实验结果 / Results】

消融实验表明，将完整标题编码到价值地图中可避免无效运动，而显式的视角感知3D验证能防止语义合理但错误的停止。该方法在 InstanceNav 和 CoIN-Bench 上取得最优性能，且无需任何任务特定的训练或微调。

【应用价值 / Applications】

该研究适用于家庭服务机器人、智能仓储物流等需要在复杂3D场景中进行精细目标导航的应用，为减少对大模型策略训练或人工交互依赖的实例导航提供了实用解决方案，具有部署便捷、泛化性强的优势。
