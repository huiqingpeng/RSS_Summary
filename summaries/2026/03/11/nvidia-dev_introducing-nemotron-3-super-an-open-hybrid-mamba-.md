---
title: "Introducing Nemotron 3 Super: An Open Hybrid Mamba-Transformer MoE for Agentic Reasoning"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/introducing-nemotron-3-super-an-open-hybrid-mamba-transformer-moe-for-agentic-reasoning/"
published: "2026-03-11"
summarized: "2026-03-12T07:04:56.253792"
ai_provider: "openai"
---

【是什么 / What it is】

Nemotron 3 Super 是 NVIDIA 发布的一款 120B 总参数、12B 激活参数的开源混合架构大语言模型，采用 Mamba-Transformer 混合骨干网络与潜变量 MoE（Latent MoE）架构，专为多智能体 AI 系统的复杂推理任务设计，原生支持 100 万 token 的上下文窗口。

Nemotron 3 Super is a 120B total / 12B active-parameter open-source hybrid LLM released by NVIDIA, featuring a Mamba-Transformer backbone with Latent MoE architecture, designed specifically for complex reasoning tasks in multi-agent AI systems with native 1M-token context window support.

---

【为什么重要 / Why it matters】

多智能体系统面临"上下文爆炸"（token 量达标准对话的 15 倍）和"思考税"（为每个子任务调用巨型推理模型成本过高）两大瓶颈，Nemotron 3 Super 通过架构创新在效率与精度之间取得突破，吞吐量提升 5 倍以上，为自主智能体的规模化部署提供了经济可行的技术基础。

Multi-agent systems face dual bottlenecks of "context explosion" (15x token volume vs. standard chats) and "thinking tax" (prohibitive costs of invoking massive reasoning models per sub-task); Nemotron 3 Super breaks through the efficiency-accuracy tradeoff with 5x+ throughput improvement, providing an economically viable foundation for scaled deployment of autonomous agents.

---

【我能用什么 / How I can use it】

开发者可利用其开源权重、数据集和训练配方，在自有基础设施上定制部署，特别适合软件工程、网络安全分析等需要长上下文记忆的多智能体场景；同时可借助其多 token 预测（MTP）和潜变量 MoE 技术，优化现有模型的推理速度与专家路由策略。

Developers can leverage its open weights, datasets, and training recipes for customized deployment on private infrastructure, ideal for multi-agent scenarios requiring long-context memory such as software engineering and cybersecurity analysis; additionally, its MTP and Latent MoE techniques can be adapted to optimize inference speed and expert routing strategies for existing models.
