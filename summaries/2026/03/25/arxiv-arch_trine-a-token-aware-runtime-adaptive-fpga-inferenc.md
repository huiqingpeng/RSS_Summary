---
title: "TRINE: A Token-Aware, Runtime-Adaptive FPGA Inference Engine for Multimodal AI"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.22867"
published: "2026-03-25"
summarized: "2026-03-26T07:07:11.238995"
ai_provider: "openai"
---

【论文摘要 / Abstract】

TRINE是一种针对多模态AI设计的FPGA推理引擎，能够在单一比特流配置下无需重新配置即可执行端到端的多模态推理。该引擎将ViT、CNN、GNN和Transformer NLP等异构计算层统一为DDMM/SDDMM/SpMM操作，并通过运行时模式切换在共享PE阵列上动态切换权重/输出驻留脉动阵列、1xCS SIMD和可路由加法树三种计算模式。结合流内token剪枝和依赖感知层卸载技术，TRINE在Alveo U50和ZCU104平台上实现了相比RTX 4090最高22.57倍、相比Jetson Orin Nano最高6.86倍的延迟降低，同时保持20-21W低功耗和低于2.5%的精度损失。

【方法概述 / Method】

TRINE采用统一算子抽象策略，将多模态网络中的各类层映射为三种稀疏/稠密矩阵乘法原语（DDMM/SDDMM/SpMM）。其核心硬件架构是一个可模式切换的处理单元阵列，支持三种计算范式动态切换：权重/输出驻留脉动阵列用于规则计算、1xCS SIMD处理稀疏模式、可路由加法树（RADT）处理归约操作。此外，设计了宽度匹配的两阶段top-k单元实现流内token剪枝，以及依赖感知层卸载（DALO）调度器实现跨处理单元的内核级并行。

【实验结果 / Results】

在Alveo U50和ZCU104平台上的评估显示，TRINE以20-21W功耗实现：相比RTX 4090延迟降低最高达22.57倍，相比Jetson Orin Nano降低6.86倍；其中token剪枝技术单独为ViT重载流水线带来最高7.8倍加速，DALO技术贡献最高79%的吞吐量提升。采用int8量化后，代表性任务上的精度损失均控制在2.5%以内，在统一处理视觉、语言和图任务方面达到当前最优的延迟和能效水平。

【应用价值 / Applications】

TRINE适用于资源受限的嵌入式边缘平台，如自动驾驶、机器人感知和智能物联网设备等需要硬实时响应的多模态AI场景。其单比特流免重构特性显著降低了部署复杂度，而运行时自适应能力使其能够高效处理动态变化的多模态工作负载。该研究为在功耗严格受限条件下实现高性能多模态推理提供了可行的硬件-软件协同设计方案。
