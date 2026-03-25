---
title: "Maximize AI Infrastructure Throughput by Consolidating Underutilized GPU Workloads"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/maximize-ai-infrastructure-throughput-by-consolidating-underutilized-gpu-workloads/"
published: "2026-03-25"
summarized: "2026-03-26T07:04:10.284382"
ai_provider: "openai"
---

【是什么 / What it is】

本文探讨了在Kubernetes生产环境中如何通过GPU分区策略（NVIDIA MIG和时间切片）解决AI推理工作负载的资源碎片化问题。文章以语音AI流水线（ASR+TTS+LLM）为测试场景，对比了专用GPU、软件共享和硬件隔离三种部署模式下的吞吐量与延迟表现。

This article explores how to address GPU resource fragmentation in production Kubernetes environments through GPU partitioning strategies—specifically NVIDIA Multi-Instance GPU (MIG) and time-slicing. Using a voice AI pipeline (ASR+TTS+LLM) as the testbed, it compares throughput and latency across three deployment modes: dedicated GPUs, software-based sharing, and hardware-level isolation.

---

【为什么重要 / Why it matters】

当前AI基础设施普遍存在"大GPU配小模型"的错配浪费：轻量级模型（如ASR/TTS）仅占10GB显存却独占整卡，导致GPU利用率低至0-10%。通过合理分区可在保证>99%可靠性和严格延迟SLA的前提下，将硬件ROI提升50%以上，同时减少集群节点膨胀和扩展摩擦。

Current AI infrastructure suffers from "large GPU, small model" mismatch: lightweight models like ASR/TTS using only 10GB VRAM yet occupying entire GPUs, resulting in 0-10% utilization. Proper partitioning can improve hardware ROI by 50%+ while maintaining >99% reliability and strict latency SLAs, reducing cluster bloat and scaling friction.

---

【我能用什么 / How I can use it】

**混合部署策略**：对延迟敏感的LLM使用专用GPU或MIG硬分区，轻量级支持模型（ASR/TTS/Embedding）采用时间切片共享GPU；**生产选型原则**：优先MIG保障故障隔离满足企业SLA，牺牲部分弹性换取稳定性；**实施路径**：通过NVIDIA GPU Operator配置timeSlicing或mig-configs，结合NIM Operator实现模型级弹性调度。

**Hybrid deployment**: Use dedicated GPUs or MIG hard partitioning for latency-sensitive LLMs, while sharing GPUs via time-slicing for lightweight support models (ASR/TTS/Embedding). **Production selection principle**: Prioritize MIG for fault isolation to meet enterprise SLAs, trading elasticity for stability. **Implementation path**: Configure timeSlicing or mig-configs via NVIDIA GPU Operator, combined with NIM Operator for model-level elastic scheduling.
