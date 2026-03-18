---
title: "Guaranteeing Semantic and Performance Determinism in Flexible GPU Sharing"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.15042"
published: "2026-03-18"
summarized: "2026-03-18T14:52:10.721471"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DetShare，一种新型的GPU共享系统，旨在解决现有方法在粗粒度时间复用（导致交互式服务尾延迟激增）与细粒度空间分区（需要侵入式内核修改）之间的权衡问题。DetShare通过引入GPU协程这一新抽象，实现了逻辑执行上下文与物理GPU资源的解耦，从而在保证语义确定性（未修改内核产生相同结果）和性能确定性（可预测尾延迟）的同时，保持完全透明（零代码修改）。实验表明，DetShare在训练吞吐量上比时间共享提升79.2%，在共置场景下将P99尾延迟降低15.1%，并通过TPOT-First调度策略将平均推理延迟降低69.1%。

【方法概述 / Method】
DetShare的核心创新是GPU协程（GPU coroutines），它将逻辑执行上下文与物理GPU资源解耦，支持通过轻量级上下文迁移实现灵活、细粒度的资源分配。系统采用工作负载感知放置策略和TPOT-First调度策略，优化推理任务的延迟表现，同时无需对现有GPU内核进行任何修改。

【实验结果 / Results】
与纯时间共享相比，DetShare将训练吞吐量提升最高达79.2%；在训练与推理共置场景中，相比最先进基线方法，P99尾延迟降低15.1%且未牺牲吞吐量。针对大语言模型推理，DetShare的平均推理延迟降低69.1%，Time-Per-Output-Token（TPOT）SLO违规率减少21.2%。

【应用价值 / Applications】
DetShare适用于现代数据中心中GPU资源的高效共享场景，特别是需要同时运行训练任务和延迟敏感的交互式推理服务的环境。该研究为云计算平台和AI基础设施提供商提供了一种无需修改用户代码即可实现确定性性能保障的GPU虚拟化方案，有助于提升硬件利用率并改善服务质量。
