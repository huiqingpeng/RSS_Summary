---
title: "NCCL EP: Towards a Unified Expert Parallel Communication API for NCCL"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.13606"
published: "2026-03-25"
summarized: "2026-03-26T07:08:13.479957"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了NCCL EP（Expert Parallelism），一个完全基于NCCL Device API构建的MoE通信库，为混合专家模型提供统一的ncclEpDispatch和ncclEpCombine原语。该库支持低延迟（LL）模式用于推理解码和高吞吐（HT）模式用于训练与推理预填充，通过GPU发起的RDMA通信优化MoE的dispatch和combine操作。在H100集群上的评估表明，NCCL EP在LL内核性能上具有竞争力，并能与vLLM集成实现端到端部署。

【方法概述 / Method】
NCCL EP基于NCCL Device API从头构建，提供C和Python双接口。LL模式针对小批量（1-128 tokens）采用直接all-to-all RDMA+NVLink网状拓扑和双缓冲通信实现dispatch与combine阶段重叠；HT模式针对大批量（4096+ tokens）采用分层通信，先在NVLink域内聚合token再进行跨节点RDMA传输。两种模式均利用Device API实现节点内外统一通信。

【实验结果 / Results】
论文在H100多节点集群上评估了NCCL EP，显示其LL内核性能与现有专用库（如DeepEP、Hybrid-EP）具有竞争力。通过与vLLM推理框架集成，验证了端到端的实用性，为当前及未来NVIDIA平台提供了受支持的专家并行路径。

【应用价值 / Applications】
NCCL EP为大语言模型的MoE架构提供了标准化、可维护的通信解决方案，适用于大规模训练和推理场景。作为NCCL原生组件，它降低了部署门槛，使研究者和工程师能够在NVIDIA硬件生态中更高效地实现和优化专家并行，特别有利于需要低延迟解码或高吞吐预填充的生产环境。
