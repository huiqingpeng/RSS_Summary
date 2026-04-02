---
title: "Bringing AI Closer to the Edge and On-Device with Gemma 4"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/bringing-ai-closer-to-the-edge-and-on-device-with-gemma-4/"
published: "2026-04-02"
summarized: "2026-04-03T07:14:09.474587"
ai_provider: "openai"
---

【是什么 / What it is】

Google 发布了 Gemma 4 系列开源模型，这是 Gemma 模型家族的最新一代，包含四个变体（31B、26B-A4B、E4B、E2B），覆盖从数据中心到边缘设备的完整部署场景，并首次引入 MoE 架构和原生多模态能力。Google has released the Gemma 4 family of open models, the latest generation in the Gemma series featuring four variants (31B, 26B-A4B, E4B, E2B) designed for full-spectrum deployment from data centers to edge devices, with the first MoE architecture and native multimodal capabilities.

【为什么重要 / Why it matters】

这标志着开源 AI 模型首次实现"云端到终端"的无缝扩展，支持 35+ 语言和文本/图像/音频/视频多模态输入，同时满足医疗、金融等受监管行业对数据隐私和低延迟的严格要求。This marks the first time open-source AI models achieve seamless "cloud-to-edge" scalability, supporting 35+ languages and text/image/audio/video multimodal inputs while meeting strict data privacy and low-latency requirements for regulated industries like healthcare and finance.

【我能用什么 / How I can use it】

开发者可根据场景选择部署方案：DGX Spark 用于本地原型开发与微调，Jetson 用于机器人/边缘 AI，RTX GPU 用于桌面应用；通过 vLLM、Ollama、llama.cpp 或 NVIDIA NIM 快速启动，并用 NeMo Automodel 进行领域定制。Developers can choose deployment scenarios based on needs: DGX Spark for local prototyping and fine-tuning, Jetson for robotics/edge AI, RTX GPUs for desktop apps; launch quickly via vLLM, Ollama, llama.cpp, or NVIDIA NIM, and customize with NeMo Automodel for domain-specific applications.
