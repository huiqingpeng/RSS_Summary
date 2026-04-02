---
title: "Welcome Gemma 4: Frontier multimodal intelligence on device"
source: "Hugging Face Blog"
url: "https://huggingface.co/blog/gemma4"
published: "2026-04-02"
summarized: "2026-04-03T07:14:33.493529"
ai_provider: "openai"
---

【是什么 / What it is】

Gemma 4 是 Google 最新发布的开源多模态 AI 模型系列，采用 Apache 2.0 许可证，支持文本、图像和音频输入，提供从 2.3B 到 31B 参数的四种尺寸，可在本地设备上运行。该系列在架构上融合了交替局部/全局注意力、Per-Layer Embeddings (PLE) 和共享 KV 缓存等创新设计，实现了长上下文处理与高效推理的平衡。

Gemma 4 is Google's latest open-source multimodal AI model family released under Apache 2.0 license, supporting text, image, and audio inputs with four sizes ranging from 2.3B to 31B parameters that can run on-device. The series incorporates architectural innovations including alternating local/global attention, Per-Layer Embeddings (PLE), and shared KV cache to balance long-context processing with efficient inference.

---

【为什么重要 / Why it matters】

Gemma 4 代表了"真正开放"的前沿模型趋势——不仅开源权重，更在 LMArena 基准上达到 SOTA 水平（31B 模型 1452 分，26B MoE 仅 4B 激活参数达 1441 分），同时保持设备端可部署性。其原生多模态能力（OCR、目标检测、语音转文本、GUI 自动化）开箱即用，大幅降低多模态应用开发门槛，挑战了"高性能必须依赖云端 API"的行业假设。

Gemma 4 represents the trend of "truly open" frontier models—not just open weights but SOTA-level LMArena scores (1452 for 31B, 1441 for 26B MoE with only 4B active parameters) while remaining deployable on-device. Its native multimodal capabilities (OCR, object detection, speech-to-text, GUI automation) work out-of-the-box, significantly lowering barriers for multimodal app development and challenging the industry assumption that high performance requires cloud APIs.

---

【我能用什么 / How I can use it】

开发者可立即通过 transformers、llama.cpp、MLX 等主流框架部署 Gemma 4，利用其 JSON 原生输出的目标检测能力构建视觉自动化工具，或结合 thinking 模式与 function calling 开发多模态智能体。建议优先测试 E2B/E4B 小模型在边缘设备的实时音频-视觉场景，以及 31B/26B MoE 在本地长文档分析、代码生成等需要大上下文的任务。

Developers can deploy Gemma 4 immediately via transformers, llama.cpp, MLX and other mainstream frameworks, leveraging its native JSON output for object detection to build visual automation tools, or combining thinking mode with function calling for multimodal agents. Recommended starting points: test E2B/E4B small models for real-time audio-visual scenarios on edge devices, and 31B/26B MoE for local long-document analysis and code generation tasks requiring large context windows.
