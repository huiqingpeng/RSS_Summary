---
title: "Build Next-Gen Physical AI with Edge‑First LLMs for Autonomous Vehicles and Robotics"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/build-next-gen-physical-ai-with-edge%e2%80%91first-llms-for-autonomous-vehicles-and-robotics/"
published: "2026-03-12"
summarized: "2026-03-13T07:05:15.926804"
ai_provider: "openai"
---

【是什么 / What it is】

本文介绍 NVIDIA TensorRT Edge-LLM 的最新版本，这是一个专为嵌入式平台设计的高性能 C++ 推理运行时，支持在 NVIDIA DRIVE AGX Thor 和 Jetson Thor 等边缘设备上运行大型语言模型（LLM）和视觉语言模型（VLM）。该版本新增了对 MoE 架构、NVIDIA Cosmos Reason 2 物理 AI 规划模型、Nemotron 2 Nano 混合推理模型以及 Qwen3-TTS/ASR 语音处理模型的支持。

This article introduces the latest version of NVIDIA TensorRT Edge-LLM, a high-performance C++ inference runtime designed for embedded platforms, supporting Large Language Models (LLMs) and Vision Language Models (VLMs) on edge devices like NVIDIA DRIVE AGX Thor and Jetson Thor. This release adds support for MoE architectures, the NVIDIA Cosmos Reason 2 physical AI planning model, the Nemotron 2 Nano hybrid reasoning model, and Qwen3-TTS/ASR speech processing models.

---

【为什么重要 / Why it matters】

这标志着边缘 AI 从"能运行模型"向"高效复杂推理"的关键转变，使自动驾驶汽车和人形机器人能够在严格的功耗和延迟限制下实现实时多模态交互、轨迹规划和物理常识推理。通过 MoE 架构和混合 Mamba-Transformer 设计，开发者可在边缘设备上部署原本需要云端的大规模模型能力，推动物理 AI 的产业化落地。

This marks a critical shift in edge AI from "running models" to "efficient complex reasoning," enabling autonomous vehicles and humanoid robots to achieve real-time multimodal interaction, trajectory planning, and physical common-sense reasoning within strict power and latency constraints. Through MoE architectures and hybrid Mamba-Transformer designs, developers can deploy large-scale model capabilities previously requiring cloud infrastructure directly on edge devices, accelerating the industrialization of physical AI.

---

【我能用什么 / How I can use it】

开发者可利用 TensorRT Edge-LLM 构建下一代自主系统：在车载场景中部署支持 /think 和 /no_think 模式切换的智能座舱助手，实现深度推理与即时对话的灵活平衡；在机器人领域集成 Cosmos Reason 2 进行 3D 空间理解和物理常识推理；或采用 Qwen3-TTS/ASR 端到端语音方案替代传统级联流水线，显著降低语音交互延迟。同时可关注即将发布的 Alpamayo 1 工作流，将 System 2 理性思维蒸馏至边缘端用于端到端轨迹规划。

Developers can leverage TensorRT Edge-LLM to build next-generation autonomous systems: deploy in-cabin assistants with /think and /no_think mode switching for flexible balance between deep reasoning and instant conversation in automotive scenarios; integrate Cosmos Reason 2 for 3D spatial understanding and physical common-sense reasoning in robotics; or adopt Qwen3-TTS/ASR end-to-end speech solutions to replace traditional cascaded pipelines and significantly reduce voice interaction latency. Also watch for the upcoming Alpamayo 1 workflow, which distills System 2 rational thinking to the edge for end-to-end trajectory planning.
