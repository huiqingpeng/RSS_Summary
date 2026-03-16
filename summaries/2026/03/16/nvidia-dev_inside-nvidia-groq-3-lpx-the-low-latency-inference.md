---
title: "Inside NVIDIA Groq 3 LPX: The Low-Latency Inference Accelerator for the NVIDIA Vera Rubin Platform"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/"
published: "2026-03-16"
summarized: "2026-03-17T07:07:18.499152"
ai_provider: "openai"
---

【是什么 / What it is】

NVIDIA Groq 3 LPX 是一款专为 NVIDIA Vera Rubin 平台设计的机架级低延迟推理加速器，与 Vera Rubin NVL72 协同设计，旨在满足 AI 智能体系统对低延迟和大上下文处理的需求。该系统基于 256 颗互联的 Groq 3 LPU 芯片构建，采用确定性执行架构和高片上 SRAM 带宽，专门优化快速、可预测的 token 生成，而 Vera Rubin NVL72 则继续承担训练和通用推理的灵活主力角色。

NVIDIA Groq 3 LPX is a rack-scale low-latency inference accelerator for the NVIDIA Vera Rubin platform, co-designed with Vera Rubin NVL72 to meet the demands of agentic AI systems requiring low latency and large context processing. Built around 256 interconnected Groq 3 LPU chips, it employs a deterministic execution architecture with high on-chip SRAM bandwidth specifically optimized for fast, predictable token generation, while Vera Rubin NVL72 remains the flexible workhorse for training and general-purpose inference.

---

【为什么重要 / Why it matters】

随着 AI 生成速度接近每秒 1000 token，模型正从对话速度交互迈向"思维速度计算"，使 AI 系统能够持续推理、模拟和响应，实现实时协作而非回合制聊天。这一转变将显著提升多智能体系统的能力上限——协调运作的智能体群体可通过集体智能完成远超个体的复杂任务，而 LPX 与 Vera Rubin NVL72 的异构组合正是支撑这一未来的关键基础设施，可在高吞吐量和低延迟之间取得平衡。

As AI generation speeds approach 1,000 tokens per second per user, models are evolving from conversational-speed interaction toward "speed of thought computing," enabling AI systems to reason, simulate, and respond continuously for real-time collaboration rather than turn-based chat. This shift dramatically raises the ceiling for multi-agent systems—coordinated groups of agents can accomplish far more through collective intelligence—and the heterogeneous combination of LPX and Vera Rubin NVL72 provides the essential infrastructure balancing high throughput with low latency to support this future.

---

【我能用什么 / How I can use it】

对于需要部署交互式 AI 应用的企业，可将 LPX 作为 Vera Rubin NVL72 的专用低延迟推理路径，专门加速解码循环中的延迟敏感部分（如 FFN 和 MoE 专家执行），同时保持 GPU 处理预填充和解码注意力的高吞吐能力。开发者应关注 LPX 的确定性执行特性，利用其编译器控制的显式数据移动和 320 字节向量工作单元来优化智能体系统的响应一致性；对于多智能体架构设计，可借助该系统的低抖动特性构建持续运行的协调智能体网络，探索实时协作、模拟推理等下一代 AI 应用场景。

For enterprises deploying interactive AI applications, LPX can serve as a dedicated low-latency inference path alongside Vera Rubin NVL72, specifically accelerating latency-sensitive portions of the decode loop (FFN and MoE expert execution) while GPUs handle prefill and decode attention at high throughput. Developers should leverage LPX's deterministic execution features, utilizing compiler-controlled explicit data movement and 320-byte vector work units to optimize response consistency for agentic systems; for multi-agent architectures, the system's low-jitter characteristics enable building continuously running coordinated agent networks, exploring next-generation AI applications such as real-time collaboration and simulated reasoning.
