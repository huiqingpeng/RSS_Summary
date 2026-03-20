---
title: "What's New in Mellea 0.4.0 + Granite Libraries Release"
source: "Hugging Face Blog"
url: "https://huggingface.co/blog/ibm-granite/granite-libraries"
published: "2026-03-20"
summarized: "2026-03-20T23:16:50.292710"
ai_provider: "openai"
---

【是什么 / What it is】

Mellea 0.4.0 是 IBM Research 开发的开源 Python 库，用于构建结构化、可验证的生成式 AI 工作流，通过约束解码替代概率性提示行为。此次发布同时推出了三个 Granite 库（granitelib-core、granitelib-rag、granitelib-guardian），它们是专为特定任务微调的小型 LoRA 适配器集合，用于查询重写、幻觉检测和策略合规等场景。

Mellea 0.4.0 is an open-source Python library developed by IBM Research for building structured, verifiable generative AI workflows that replace probabilistic prompt behavior with constrained decoding. The release includes three Granite Libraries (granitelib-core, granitelib-rag, granitelib-guardian)—collections of small, task-specific LoRA adapters fine-tuned for operations like query rewriting, hallucination detection, and policy compliance.

---

【为什么重要 / Why it matters】

这一发布代表了从"提示工程"向"可编程生成系统"的重要转变，通过专用小型模型和结构化修复循环提升 AI 输出的可靠性和可维护性。对于企业级 AI 应用而言，这种模块化、可观测的安全优先架构解决了 LLM 在生产环境中难以控制的根本痛点。

This release marks a significant shift from "prompt engineering" to "programmable generative systems," improving AI output reliability and maintainability through specialized small models and structured repair loops. For enterprise AI applications, this modular, observable, safety-first architecture addresses fundamental pain points of deploying LLMs in production environments where control and predictability are critical.

---

【我能用什么 / How I can use it】

开发者可将 Mellea 与 Granite 库结合，在 RAG 管道中实现检索前查询重写、检索后相关性验证和生成后事实性检查的分层质量控制。建议从 Hugging Face 获取 Granite 库适配器，利用 Mellea 的 instruct-validate-repair 模式和事件钩子构建具有完整可观测性的生产级 AI 工作流。

Developers can combine Mellea with Granite Libraries to implement layered quality control in RAG pipelines—covering pre-retrieval query rewriting, post-retrieval relevance validation, and post-generation fact-checking. Start by fetching Granite Library adapters from Hugging Face, then leverage Mellea's instruct-validate-repair pattern and event hooks to build production-grade AI workflows with full observability.
