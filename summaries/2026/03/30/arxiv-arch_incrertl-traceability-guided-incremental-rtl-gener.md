---
title: "IncreRTL: Traceability-Guided Incremental RTL Generation under Requirement Evolution"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.25769"
published: "2026-03-30"
summarized: "2026-03-31T07:17:15.993867"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了IncreRTL，一种面向需求演化的增量式RTL生成框架，解决了现有大语言模型方法在硬件设计需求变更时只能全量重生成、导致结构漂移和效率低下的问题。通过构建需求-代码可追溯性链接来定位受影响代码段并进行精准更新，IncreRTL在作者新构建的EvoRTL-Bench基准测试中显著提升了再生一致性和效率，推动LLM-based RTL生成向实际工程部署迈进。

【方法概述 / Method】
IncreRTL采用需求-代码可追溯性链接构建技术，建立自然语言需求与RTL代码之间的映射关系；当需求发生演化时，利用该链接定位受影响的代码片段，驱动大语言模型进行局部增量生成而非全量重写，从而保持设计结构的一致性。

【实验结果 / Results】
在EvoRTL-Bench基准测试上的评估表明，IncreRTL在再生一致性和效率方面均有显著提升；相比静态全量重生成方法，该方法有效避免了结构漂移问题，减少了不必要的代码改动，提高了RTL代码在需求演化场景下的维护性和可靠性。

【应用价值 / Applications】
IncreRTL可应用于工业级硬件设计流程中频繁发生需求变更的场景，如芯片设计规格迭代、功能扩展或约束调整等，帮助工程师高效维护RTL代码库；该框架降低了因需求演化导致的重设计成本，为LLM在硬件敏捷开发和持续集成中的实际落地提供了可行路径。
