---
title: "Homogeneous and Heterogeneous Consistency progressive Re-ranking for Visible-Infrared Person Re-identification"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16165"
published: "2026-03-18"
summarized: "2026-03-18T18:07:41.037920"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对可见光-红外行人重识别（Visible-Infrared Person Re-identification）中跨模态差异和模态内变化难以同时处理的挑战，提出了一种渐进式模态关系重排序方法HHCR（异构与同构一致性重排序）。该方法包含两个核心模块：异构一致性重排序模块探索查询集与候选集之间的跨模态关系，同构一致性重排序模块挖掘测试集内各模态的内在关系。基于此，作者还提出了跨模态行人重识别基线网络CRI（一致性重排序推理网络），实验表明所提重排序方法具有良好的泛化性，且重排序模块与基线网络均达到了最先进的性能。

【方法概述 / Method】
HHCR方法采用渐进式两阶段重排序策略：第一阶段异构一致性重排序（Heterogeneous Consistency Re-ranking）建立查询样本与候选库之间的跨模态关联约束；第二阶段同构一致性重排序（Homogeneous Consistency Re-ranking）进一步利用各模态内部的结构一致性信息优化排序结果。CRI基线网络则作为特征提取与初始检索的基础架构，为重排序提供可靠的初始排名列表。

【实验结果 / Results】
论文通过大量实验验证了所提方法的有效性和泛化能力，HHCR重排序方法与CRI基线网络在可见光-红外行人重识别任务上均取得了 state-of-the-art 的性能表现。实验结果表明，该渐进式重排序策略能够同时有效缓解跨模态差异和模态内变化带来的匹配困难，显著提升了识别准确率。

【应用价值 / Applications】
该研究在智能视频监控、夜间安防追踪、跨时段行人检索等实际场景中具有重要应用价值，特别是在光照条件剧烈变化（白天可见光/夜间红外）环境下实现行人身份的连续追踪与识别。所提重排序方法具有良好的通用性，可推广至其他跨模态重识别任务，为构建鲁棒的跨模态智能视觉系统提供了技术支撑。
