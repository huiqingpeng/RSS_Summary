---
title: "Infinity-RoPE: Action-Controllable Infinite Video Generation Emerges From Autoregressive Self-Rollout"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.20649"
published: "2026-03-20"
summarized: "2026-03-20T16:15:20.152463"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 ∞-RoPE，一种统一的推理时框架，解决了自回归视频扩散模型的三大核心瓶颈：3D-RoPE 的有限时间范围、长序列生成中的细粒度动作控制延迟，以及无法实现非连续电影级转场。通过块相对论 RoPE、KV Flush 和 RoPE Cut 三个组件的协同设计，∞-RoPE 实现了无需训练的无限时长、可控且具备电影感的视频生成，并在 VBench 综合评测中持续超越现有自回归模型。

【方法概述 / Method】

∞-RoPE 包含三个核心组件：**Block-Relativistic RoPE** 将时间编码重构为移动局部参考系，使新生成的潜在块相对于基础模型的最大帧范围旋转，同时早期块向后旋转以保持相对时间几何；**KV Flush** 仅保留全局汇聚帧和最后生成帧来更新 KV 缓存，确保即时提示响应而无需重新编码；**RoPE Cut** 在时间 RoPE 坐标中引入可控间断，实现单次连续生成中的多切割场景转场。

【实验结果 / Results】

综合实验表明，∞-RoPE 在 VBench 整体评分上持续超越先前的自回归模型。该框架突破了基础模型的固定位置限制，实现了远超原始时间范围的连续视频生成，同时保持了细粒度的动作控制能力和电影级非连续转场效果。

【应用价值 / Applications】

∞-RoPE 为长视频内容创作、交互式视频生成和电影制作提供了强大的技术基础，特别适用于需要无限时长扩展、实时动作响应和复杂场景切换的应用场景。作为一种无需额外训练的推理时方法，它可直接部署于现有的自回归视频扩散模型，显著降低长视频生成的计算成本和使用门槛。
