---
title: "Characterizing CPU-Induced Slowdowns in Multi-GPU LLM Inference"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.22774"
published: "2026-03-25"
summarized: "2026-03-26T07:06:41.196464"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文系统分析了多GPU大语言模型（LLM）推理中CPU导致的性能瓶颈问题。研究发现，多GPU系统性能下降往往源于CPU无法及时调度GPU工作，而非GPU资源饱和，表现为内核启动延迟、通信阻塞和分词延迟增加等症状。即使在采用进程级分离和CUDA Graphs等现代优化的服务栈中，这些瓶颈依然存在。实验表明，适当增加CPU核心数可在成本增加极小的情况下显著提升性能和稳定性，将首token时间（TTFT）延迟降低1.36-5.40倍。

【方法概述 / Method】

本研究采用系统性的实验分析方法，对现代LLM推理和服务工作负载进行详细剖析。研究团队在受控条件下测试了不同CPU资源配置下的多GPU推理性能，并考察了进程级分离和CUDA Graphs等现有优化技术对CPU瓶颈的缓解效果。通过对比CPU受限配置与充足CPU配置的性能差异，量化CPU资源对GPU利用率和端到端延迟的影响。

【实验结果 / Results】

实验结果显示，在中等服务负载下，CPU资源不足的配置频繁出现超时，而提供充足CPU资源可恢复系统响应性。增加CPU核心数使首token时间（TTFT）延迟降低1.36-5.40倍，且无需额外GPU即可实现。由于CPU核心的边际成本相对于GPU实例价格极低，这种配置优化具有显著的成本效益优势，能有效避免控制面瓶颈导致的GPU利用率低下问题。

【应用价值 / Applications】

本研究对大规模LLM推理服务的系统配置具有重要指导意义，帮助云服务商和企业优化多GPU实例的CPU-GPU配比，避免因CPU瓶颈造成的GPU资源浪费。研究结果可用于改进自动扩缩容策略、优化Kubernetes等容器编排平台的资源调度，以及指导GPU实例类型的选择决策，从而在控制成本的同时提升服务质量和用户体验。
