---
title: "Scaling Autonomous AI Agents and Workloads with NVIDIA DGX Spark"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/scaling-autonomous-ai-agents-and-workloads-with-nvidia-dgx-spark/"
published: "2026-03-16"
summarized: "2026-03-17T07:08:06.866478"
ai_provider: "openai"
---

【是什么 / What it is】

本文介绍 NVIDIA DGX Spark 作为桌面级 AI 计算平台，专为运行自主 AI 智能体（Autonomous AI Agents）而设计。它搭载 NVIDIA Grace Blackwell Superchip，支持单机 128GB 显存，并可扩展至最多四节点（512GB 显存），配合 NVIDIA NeMoClaw 和 OpenShell 运行时，为本地部署大语言模型和多智能体工作负载提供安全高效的计算环境。

This article introduces NVIDIA DGX Spark as a desktop AI computing platform designed specifically for running autonomous AI agents. It features the NVIDIA Grace Blackwell Superchip with 128GB memory per node, scalable up to four nodes (512GB total), and integrates with NVIDIA NeMoClaw and OpenShell runtime to provide a secure and efficient local environment for deploying large language models and multi-agent workloads.

---

【为什么重要 / Why it matters】

自主 AI 智能体需要处理超长上下文（30K-250K tokens）、多通道通信和后台子进程，对本地算力提出极高要求。DGX Spark 通过低延迟 RoCE 互联和 Tensor 并行技术，实现了近乎线性的推理和微调扩展效率，填补了从原型开发到云端部署之间的关键缺口，使开发者能够在本地构建和测试复杂的智能体系统。

Autonomous AI agents demand extreme local compute for long contexts (30K-250K tokens), multi-channel communication, and background subprocesses. DGX Spark bridges the critical gap between prototyping and cloud deployment through low-latency RoCE interconnect and tensor parallelism, achieving near-linear scaling for inference and fine-tuning—enabling developers to build and test complex agent systems locally.

---

【我能用什么 / How I can use it】

开发者可利用 DGX Spark 单机运行 120B 参数模型的智能体推理，或通过多节点扩展支持 700B 参数模型；结合 TensorRT LLM、vLLM 或 SGLang 框架优化并发性能；使用 NeMoClaw 和 OpenShell 安全运行自演化智能体；并利用 Tile IR 和 cuTile Python 实现从本地开发到云端部署的无缝迁移。

Developers can use single DGX Spark nodes for agent inference up to 120B parameters, or scale to four nodes for 700B-parameter models; optimize concurrency with TensorRT LLM, vLLM, or SGLang frameworks; safely run self-evolving agents via NeMoClaw and OpenShell; and leverage Tile IR and cuTile Python for seamless workload portability from local development to cloud deployment.
