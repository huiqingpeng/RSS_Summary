---
title: "Achievable DoF Bounds for Cache-Aided Asymmetric MIMO Communications"
source: "arXiv Information Theory"
url: "https://arxiv.org/abs/2603.18240"
published: "2026-03-20"
summarized: "2026-03-20T17:05:31.910866"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了缓存辅助的非对称MIMO通信系统，其中服务器配备L个发射天线，K个用户被划分为J组，每组用户具有不同的接收天线数G_j。论文提出了四种内容感知的MIMO-CC策略（min-G、Grouping、Super-grouping和Phantom），并在三种具有保证线性可解码性的对称CC放置-传输策略下进行了开发。分析和数值结果表明，所提策略在各种系统配置下均能实现显著的DoF提升，且策略组合可在DoF与子包化复杂度之间提供灵活的权衡。

【方法概述 / Method】

论文设计了四种针对非对称天线配置的MIMO-CC策略：min-G策略通过将所有用户强制对齐到最小天线数来实现对称化；Grouping策略优先最大化子集内的空间复用增益；Super-grouping策略先将用户聚类为具有相同有效接收复用增益的超级集合，再跨集合应用Grouping；Phantom策略则通过假设用户具有"虚拟"天线来重新分配空间资源，以桥接min-G和Grouping的性能差距。这些策略均在三种参考对称CC策略下实现：DoF最优策略、组合构造策略和线性循环低复杂度构造策略。

【实验结果 / Results】

实验结果表明，所提出的四种策略相比传统方法在不同系统配置下均实现了显著的DoF性能提升。其中，Super-grouping和Phantom策略在多数工作点展现出优于基础策略的性能，而线性循环策略在保持低复杂度的同时，其DoF性能在多种工作条件下接近最优策略和组合策略。策略与放置-传输策略的不同组合为系统设计者提供了DoF性能与子包化复杂度之间的灵活权衡选择。

【应用价值 / Applications】

该研究对5G/6G无线通信网络、边缘缓存系统和视频流服务等实际场景具有重要价值，能够有效支持具有异构设备能力（如智能手机、平板、IoT设备等不同天线配置）的多用户内容分发。所提策略的灵活性使其可适配不同的服务需求——高DoF策略适用于低延迟高清视频传输，而低复杂度策略则适合资源受限的实时应用，为实际部署提供了可扩展的解决方案。
