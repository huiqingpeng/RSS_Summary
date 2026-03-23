---
title: "Agile TLB Prefetching and Prediction Replacement Policy"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2412.17203"
published: "2026-03-23"
summarized: "2026-03-24T07:14:35.836148"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Agile TLB Prefetcher (ATP)与SBFP集成的预取机制，通过利用页表局部性并在页表遍历期间动态识别关键的空闲PTE来优化性能。同时，论文提出了一种基于控制流历史的预测性替换策略CHiRP，用于L2 TLB中检测死块，相比传统LRU和现有高级策略（SRRIP、GHRP、SHiP等）进一步提升性能。这些集成技术共同解决了虚拟内存管理中的关键挑战，包括TLB未命中导致的昂贵页表遍历开销以及预取错误预测带来的额外负担。

【方法概述 / Method】
论文采用硬件与软件协同优化的方法，在软件层面设计Agile TLB Prefetcher与SBFP（可能为现有预取机制）集成，利用页表访问的局部性特征进行PTE预取；在替换策略层面，提出CHiRP（Control flow History-based Replacement Policy），利用控制流历史信息检测死块，并直接使用L2 TLB条目进行学习而非采样，实现更精准的预测性替换决策。

【实验结果 / Results】
（注：论文摘要中未提供具体的实验数据，仅提及CHiRP在L2 TLB上超越其他现有替换策略，ATP与SBFP的集成优化了整体性能。）

【应用价值 / Applications】
该研究可应用于现代处理器架构中的虚拟内存子系统设计，特别适用于大规模内存工作负载和数据中心服务器场景，通过降低TLB未命中率和页表遍历开销来提升系统整体性能；同时，其预测性替换策略和敏捷预取机制为操作系统与硬件协同优化虚拟内存管理提供了新的设计思路。
