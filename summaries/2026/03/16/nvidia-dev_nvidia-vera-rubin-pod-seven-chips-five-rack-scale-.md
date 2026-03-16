---
title: "NVIDIA Vera Rubin POD: Seven Chips, Five Rack-Scale Systems, One AI Supercomputer"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/nvidia-vera-rubin-pod-seven-chips-five-rack-scale-systems-one-ai-supercomputer/"
published: "2026-03-16"
summarized: "2026-03-17T07:09:25.966036"
ai_provider: "openai"
---

【是什么 / What it is】

NVIDIA Vera Rubin POD 是 NVIDIA 推出的第三代 MGX 机架级 AI 超级计算机，由五种专用机架系统组成，整合七种协同设计的芯片（包括 GPU、CPU、网络及存储芯片），专为"代理式 AI"（Agentic AI）时代设计。该系统包含 40 个机架、1,152 颗 Rubin GPU、60 exaflops 算力，通过 NVLink 和新型 ETL 连接技术将多个机架整合为单一连贯系统。

The NVIDIA Vera Rubin POD is a third-generation MGX rack-scale AI supercomputer comprising five specialized rack systems built on seven co-designed chips (GPUs, CPUs, networking, and storage). Designed for the agentic AI era, it features 40 racks, 1,152 Rubin GPUs, 60 exaflops of compute, and integrates multiple racks into one coherent system via NVLink and new ETL connectivity.

---

【为什么重要 / Why it matters】

AI 正从"人机交互"转向"AI 与 AI 交互"的新纪元，token 年消耗量已突破 10 千万亿且持续倍增；代理式系统需要多步骤推理、工具调用和沙盒验证，对低延迟、高吞吐、大上下文内存提出极致要求。Vera Rubin POD 通过机架级协同设计，实现每瓦特训练性能提升 4 倍、推理性能提升 10 倍、token 成本降至 1/10，重新定义 AI 工厂的能效与经济性标准。

AI is shifting from human-AI to AI-AI interaction, with annual token consumption exceeding 10 quadrillion and growing multifold; agentic systems demand extreme low-latency, high-throughput, and massive context memory for multi-step reasoning and sandbox validation. Through rack-scale co-design, Vera Rubin POD achieves 4× training performance, 10× inference performance per watt, and 1/10 token cost versus Blackwell, redefining energy efficiency and economics for AI factories.

---

【我能用什么 / How I can use it】

若从事大模型推理服务，可关注 NVL72 + Groq 3 LPX 的组合方案，在万亿参数模型上实现 35 倍 token 吞吐提升；若构建 agentic 应用，可利用 Vera CPU 机架部署超 22,500 个并发 RL/沙盒环境进行结果验证；基础设施规划者应评估 MGX 统一机架设计（共享供电、散热、机械规格）以简化供应链和快速部署，并关注 CMX 上下文内存存储对长上下文推理的加速潜力。

For LLM inference services, consider the NVL72 + Groq 3 LPX combination for 35× token throughput on trillion-parameter models; for agentic applications, leverage Vera CPU racks to deploy 22,500+ concurrent RL/sandbox environments for result validation; infrastructure planners should evaluate the unified MGX rack design (shared power, cooling, mechanical envelopes) to streamline supply chains and accelerate deployment, while exploring CMX context memory storage for long-context inference acceleration.
