---
title: "Building NVIDIA Nemotron 3 Agents for Reasoning, Multimodal RAG, Voice, and Safety"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/building-nvidia-nemotron-3-agents-for-reasoning-multimodal-rag-voice-and-safety/"
published: "2026-03-24"
summarized: "2026-03-25T07:05:55.350065"
ai_provider: "openai"
---

【是什么 / What it is】

NVIDIA于2025年GTC大会发布了Nemotron 3系列模型，这是一个专为Agentic AI设计的统一技术栈，包含用于长上下文推理的Super模型、即将推出的Ultra模型、多模态内容安全审核模型、端到端语音对话模型VoiceChat、企业级多模态理解模型Nano Omni，以及支持图像和文本嵌入与重排序的RAG模型。该系列采用开放权重、开放数据和开放训练配方，配合NVIDIA NeMo工具链，为开发者提供构建生产级智能体系统的完整工具包。

At GTC 2025, NVIDIA introduced the Nemotron 3 family of models as a unified agentic stack, including Super for long-context reasoning, upcoming Ultra for highest accuracy, Content Safety for multimodal moderation, VoiceChat for end-to-end speech conversations, upcoming Nano Omni for enterprise multimodal understanding, and RAG models for image-text embeddings and reranking. With open weights, data, training recipes, and NeMo tooling, this ecosystem provides developers an end-to-end toolkit for building production-grade agentic AI systems.

【为什么重要 / Why it matters】

Agentic AI正从单文本模态向多模态、多智能体协作演进，但面临上下文爆炸、推理成本高昂、安全审核复杂、语音交互延迟高等核心挑战。Nemotron 3系列通过MoE架构降低推理成本（每次仅激活12B参数）、NVFP4精度提升5倍吞吐量、端到端语音模型消除级联延迟、原生多模态安全模型覆盖23类风险，为大规模商业化部署提供了性能与效率兼顾的解决方案，特别是在金融、医疗、网络安全等合规敏感行业。

Agentic AI is evolving from single-text to multimodal multi-agent systems, yet faces critical challenges: context explosion, high reasoning costs, complex safety guardrailing, and voice latency. The Nemotron 3 family addresses these through MoE architecture (activating only 12B parameters per pass), 5x throughput gains via NVFP4 precision, end-to-end speech eliminating cascaded delays, and native multimodal safety covering 23 risk categories—enabling scalable commercial deployment in compliance-sensitive industries like finance, healthcare, and cybersecurity.

【我能用什么 / How I can use it】

开发者可基于具体场景选择模型组合：使用Nemotron 3 Super构建多智能体系统并通过"思考预算"控制成本；部署Content Safety实现生产流水线中的实时内容审核；采用VoiceChat开发低延迟全双工语音助手替代传统ASR-LLM-TTS级联方案；利用Nano Omni处理视频、音频、文档、UI屏幕的跨模态理解；通过Embed VL和Rerank VL优化多模态RAG检索效果。建议结合NVIDIA NeMo框架进行微调、评估和优化，并关注即将发布的Ultra和Nano Omni模型以获取更强能力。

Developers can select model combinations for specific scenarios: use Nemotron 3 Super for multi-agent systems with configurable "thinking budgets" to control costs; deploy Content Safety for real-time moderation in production pipelines; adopt VoiceChat for low-latency full-duplex voice assistants replacing cascaded ASR-LLM-TTS stacks; leverage Nano Omni for cross-modal understanding of video, audio, documents, and UI screens; and optimize multimodal RAG with Embed VL and Rerank VL. Combine with NVIDIA NeMo for fine-tuning, evaluation, and optimization, and watch for upcoming Ultra and Nano Omni releases for enhanced capabilities.
