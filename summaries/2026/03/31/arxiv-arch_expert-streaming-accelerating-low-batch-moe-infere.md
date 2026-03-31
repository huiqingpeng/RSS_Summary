---
title: "Expert Streaming: Accelerating Low-Batch MoE Inference via Multi-chiplet Architecture and Dynamic Expert Trajectory Scheduling"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.27624"
published: "2026-03-31"
summarized: "2026-04-01T07:16:02.963908"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对边缘AI场景下低批次MoE（混合专家模型）推理的挑战，提出了全分片专家数据并行（FSE-DP）架构。该架构利用高带宽芯粒间互连技术，通过动态专家轨迹调度实现细粒度计算-通信重叠和负载均衡，解决了片上内存受限、工作负载不均衡以及片外内存访问瓶颈等问题。实验表明，该方法相比现有最优基线可实现1.22至2.00倍的加速，并节省高达78.8%的片上内存。

【方法概述 / Method】
论文采用多芯粒架构结合动态专家轨迹调度策略，设计了FSE-DP并行范式。该方法通过高带宽D2D（Die-to-Die）链路编排细粒度互补专家流，实现自适应的计算与通信重叠；同时引入极简的硬件友好型虚拟化规则和轻量级调度算法来管理复杂的数据流。

【实验结果 / Results】
FSE-DP在低批次MoE推理场景下相比SOTA基线取得1.22-2.00倍的性能提升，片上内存占用降低78.8%。实验验证了该方法在解决工作负载不均衡和内存瓶颈方面的有效性，同时保持了较低的调度开销。

【应用价值 / Applications】
该研究适用于资源受限的边缘AI设备部署大规模MoE模型，如智能手机、物联网设备和边缘服务器等场景。通过多芯粒协同和动态调度技术，可在不牺牲推理效率的前提下显著降低硬件成本，推动稀疏大模型在端侧的实际应用。
