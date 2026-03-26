---
title: "LMetric: Simple is Better - Multiplication May Be All You Need for LLM Request Scheduling"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.15202"
published: "2026-03-26"
summarized: "2026-03-27T07:12:36.950291"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出LMetric，一种极简的LLM请求调度方法，通过简单地将两个关键指标（KV缓存感知的新prefill token数和负载均衡感知的当前batch size）相乘作为调度分数，同时实现KV缓存复用和负载均衡两大目标。该方法无需任何超参数调优，避免了现有复杂组合器（如线性组合）带来的调优开销和次优性能。在真实工作负载上的实验表明，相比vLLM-v1和生产级调度器，LMetric可将TTFT分别降低92%和52%，TPOT分别降低21%和20%。

【方法概述 / Method】
LMetric的核心创新是采用乘法而非加法来组合两个调度指标：新prefill token数（衡量KV缓存复用潜力）和当前batch size（衡量实例负载）。乘法组合的关键优势在于原始超参数在比较过程中自然抵消，从而消除了调参需求。指标选择基于对LLM特性的深入分析，确保乘法能有效平衡两个目标。

【实验结果 / Results】
在覆盖聊天机器人、API调用和编程代理的真实工作负载上，LMetric相比vLLM-v1实现TTFT降低92%、TPOT降低21%；相比某生产级调度器实现TTFT降低52%、TPOT降低20%。作者还数学推导了乘法可能失效的条件，发现这些条件在实践中极为罕见且可被预先检测和缓解。

【应用价值 / Applications】
LMetric可广泛应用于大规模LLM服务部署，特别是需要同时优化首token延迟（TTFT）和每token延迟（TPOT）的多租户场景。其无需调参的特性显著降低了部署门槛，使云服务商和企业能够快速部署高性能调度系统，适用于聊天机器人、API服务和AI编程助手等多样化负载。
