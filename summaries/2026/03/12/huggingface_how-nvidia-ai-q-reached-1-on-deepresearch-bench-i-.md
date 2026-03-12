---
title: "How NVIDIA AI-Q Reached \#1 on DeepResearch Bench I and II"
source: "Hugging Face Blog"
url: "https://huggingface.co/blog/nvidia/how-nvidia-won-deepresearch-bench"
published: "2026-03-12"
summarized: "2026-03-13T07:05:38.390564"
ai_provider: "openai"
---

【是什么 / What it is】

NVIDIA AI-Q 是一个开源的、模块化的 AI 智能体架构蓝图，用于构建能够对企业数据和网络数据进行推理并生成带引用来源回复的 AI 智能体。其"深度研究"工作流最近在 DeepResearch Bench I 和 II 两个主要基准测试中都获得了第一名，展示了开放、可移植的开发者可访问模型和工具可以达到最先进的智能体研究水平。

NVIDIA AI-Q is an open, modular blueprint for building AI agents that reason over enterprise and web data to deliver well-cited responses. Its "deep researcher" workflow recently achieved first place on both DeepResearch Bench I and II, the two primary benchmarks for evaluating deep research agents, demonstrating that developer-accessible open models and tooling can power state-of-the-art agentic research.

---

【为什么重要 / Why it matters】

这是开放、可移植的深度研究智能体的重要里程碑，证明了企业无需依赖封闭的黑盒系统即可获得顶尖性能。AI-Q 采用完全开放和模块化的架构，企业可以拥有、检查、定制和配置，解决了 AI 部署中的透明度、可控性和数据主权问题。同时在两个互补的基准测试中领先，意味着该系统既能生成结构优美的报告，又能确保底层检索和推理的准确性。

This marks a meaningful milestone for open, portable deep research agents, proving that enterprises can achieve top-tier performance without relying on closed black-box systems. AI-Q's fully open and modular architecture allows enterprises to own, inspect, customize, and configure it, addressing critical concerns around transparency, control, and data sovereignty in AI deployment. Leading on both complementary benchmarks means the system delivers both polished, well-structured narratives and granular factual correctness with analytical rigor.

---

【我能用什么 / How I can use it】

企业开发者可以基于 NVIDIA NeMo Agent Toolkit 和 LangChain DeepAgents 构建自己的深度研究智能体，使用微调的 Nemotron 3 模型或替换为其他 LLM。关键实践包括：采用多智能体架构（规划器-研究者-协调器）进行迭代式研究循环，实施基于证据的规划以确保信息可靠性，以及可选的集成层和报告优化器来提升最终质量。该架构特别适合需要长程可靠性、多源信息综合和带引用报告的企业研究场景。

Enterprise developers can build their own deep research agents using the NVIDIA NeMo Agent Toolkit and LangChain DeepAgents, with fine-tuned Nemotron 3 models or alternative LLMs. Key practices include: adopting a multi-agent architecture (planner-researcher-orchestrator) for iterative research loops, implementing evidence-grounded planning to ensure information reliability, and optionally adding an ensemble layer and report refiner for maximum quality. This architecture is particularly suited for enterprise research scenarios requiring long-horizon reliability, multi-source synthesis, and citation-backed reporting.
