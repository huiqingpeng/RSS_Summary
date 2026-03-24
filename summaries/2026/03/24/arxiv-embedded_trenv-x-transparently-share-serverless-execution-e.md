---
title: "TrEnv-X: Transparently Share Serverless Execution Environments Across Different Functions and Nodes"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2509.09525"
published: "2026-03-24"
summarized: "2026-03-25T07:06:33.676516"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出TrEnv-X系统，通过将无服务器平台与操作系统及CXL/RDMA远程内存池协同设计，解决了无服务器计算中函数必须在本地专用环境运行导致的内存弹性受限问题。核心创新包括可复用的沙箱（支持跨函数共享以降低创建开销）和OS级内存模板（实现从远程内存池快速状态恢复）。该系统还扩展支持基于微VM的LLM智能体工作负载，并引入浏览器共享和页缓存绕过等新优化。实验表明，TrEnv-X在容器函数场景下P99延迟降低达7倍、内存节省48%；在LLM智能体场景下相比E2B等先进系统P99延迟降低58%、内存使用减少61%。

【方法概述 / Method】

TrEnv-X采用软硬件协同设计方法，将无服务器平台与操作系统深度集成，并基于CXL/RDMA技术构建远程内存池。关键技术包括：设计可复用的沙箱机制实现执行环境跨函数透明共享，以及OS级内存模板机制支持从远程内存快速恢复状态。针对微VM-based智能体工作负载，进一步扩展了浏览器共享和页缓存绕过等优化机制。

【实验结果 / Results】

在容器函数评估中，TrEnv-X实现P99延迟最高7倍降低和48%内存节省。在LLM智能体应用场景中，相比E2B等现有先进系统，P99延迟降低达58%，内存使用减少61%。

【应用价值 / Applications】

TrEnv-X适用于需要高弹性、低延迟的大规模无服务器计算场景，特别是容器化函数服务和LLM智能体执行环境。该研究通过提升内存弹性和执行效率，可降低云服务商基础设施成本，同时改善无服务器应用的响应性能和资源利用率，对下一代云计算和AI智能体平台具有重要实践意义。
