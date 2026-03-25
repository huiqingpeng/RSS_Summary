---
title: "Scaling Token Factory Revenue and AI Efficiency by Maximizing Performance per Watt"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/scaling-token-factory-revenue-and-ai-efficiency-by-maximizing-performance-per-watt/"
published: "2026-03-25"
summarized: "2026-03-26T07:05:08.150281"
ai_provider: "openai"
---

【是什么 / What it is】

本文阐述了在AI时代，电力成为AI基础设施的终极约束条件，NVIDIA通过全栈协同设计（从芯片制造、架构创新到系统冷却和软件优化）最大化"每瓦性能"（performance per watt），从而提升AI工厂的token产出效率和营收能力。文章详细介绍了从Hopper到Blackwell再到Vera Rubin的架构演进，以及cuLitho、cuEST等制造端创新如何实现代际间的效率跃升。

This article explains how power has become the ultimate constraint in the AI era, and how NVIDIA maximizes "performance per watt" through full-stack co-design—from chip manufacturing and architecture innovations to system cooling and software optimization—to boost token throughput and revenue for AI factories. It details the architectural evolution from Hopper to Blackwell to Vera Rubin, as well as manufacturing innovations like cuLitho and cuEST that enable generational efficiency leaps.

---

【为什么重要 / Why it matters】

"每瓦性能"正取代单纯算力指标，成为AI基础设施的核心竞争力——在固定电力预算下，效率直接决定token产出量和商业回报，这重塑了数据中心的投资逻辑和竞争格局。NVIDIA展示的100万倍推理效率提升（六代架构）表明，硬件-软件-系统协同优化可创造指数级价值，这对面临电力瓶颈的AI规模化部署具有决定性意义。同时，液冷、数字孪生等技术的普及标志着AI工厂正从"耗电设施"向"能源生态系统"转型。

"Performance per watt" is replacing raw compute metrics as the core competitive advantage for AI infrastructure—under fixed power budgets, efficiency directly determines token output and commercial returns, reshaping data center investment logic and competitive dynamics. NVIDIA's demonstrated 1,000,000x inference efficiency improvement across six architecture generations shows that hardware-software-system co-optimization can create exponential value, which is decisive for AI scale-out facing power bottlenecks. Meanwhile, the adoption of liquid cooling, digital twins, and other technologies signals AI factories' transformation from "power consumers" to "energy ecosystems."

---

【我能用什么 / How I can use it】

对于AI基础设施决策者：评估供应商时应重点关注全栈效率指标（PUE、token/瓦特、实际算力利用率），而非仅比较峰值算力；优先考虑支持液冷和动态功耗管理的系统设计。对于技术从业者：在模型选型和服务部署中引入"每token能耗"作为关键优化目标，结合推理效率工具（如TensorRT-LLM）降低推理成本。对于投资者和战略分析者：关注电力获取能力（土地、电网接入）与效率技术的组合，这将成为AI工厂差异化壁垒的核心来源。

For AI infrastructure decision-makers: evaluate suppliers based on full-stack efficiency metrics (PUE, tokens/watt, actual compute utilization) rather than peak compute comparisons alone; prioritize systems supporting liquid cooling and dynamic power management. For technical practitioners: introduce "energy per token" as a key optimization target in model selection and service deployment, leveraging inference efficiency tools (e.g., TensorRT-LLM) to reduce serving costs. For investors and strategic analysts: focus on the combination of power access capabilities (land, grid connectivity) and efficiency technologies, which will become the core source of differentiation for AI factories.
