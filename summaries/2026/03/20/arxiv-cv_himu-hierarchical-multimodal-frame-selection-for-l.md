---
title: "HiMu: Hierarchical Multimodal Frame Selection for Long Video Question Answering"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18558"
published: "2026-03-20"
summarized: "2026-03-20T15:11:50.955064"
ai_provider: "openai"
---

【论文摘要 / Abstract】
HiMu 提出了一种无需训练的层次化多模态帧选择框架，用于解决长视频问答中的帧选择难题。该方法通过单次纯文本 LLM 调用将查询分解为层次化逻辑树，并将原子谓词路由至轻量级视觉和音频专家，最终通过模糊逻辑算子自底向上组合生成连续满足度曲线。实验表明，HiMu 在效率-准确率帕累托前沿上取得突破：使用 Qwen3-VL 8B 时以 16 帧超越所有竞争选择器，使用 GPT-4o 时以约 10 倍更少的 FLOPs 超越 32-512 帧的代理系统。

【方法概述 / Method】
HiMu 采用三层架构：首先利用纯文本 LLM 将复杂查询解析为层次化逻辑树，叶节点为原子谓词；然后为每个谓词分配轻量级专家（CLIP、开放词汇检测、OCR、ASR、CLAP 等）提取多模态信号；最后对信号归一化、时序平滑后，通过模糊逻辑算子（含时序顺序与邻接约束）自底向上组合，输出连续帧满足度评分。

【实验结果 / Results】
在 Video-MME、LongVideoBench 和 HERBench-Lite 三个基准上，HiMu 显著推进了效率-准确率权衡边界。具体而言，HiMu 配合 Qwen3-VL 8B 以仅 16 帧输入即超越所有对比帧选择方法；配合 GPT-4o 时，在帧数减少 2-32 倍的情况下，性能仍优于需要 32-512 帧的代理式系统，且计算量降低约 10 倍。

【应用价值 / Applications】
HiMu 可广泛应用于长视频理解场景，如教育视频智能答疑、监控录像时序分析、影视内容检索与摘要生成等。其训练无关特性与低计算开销使其特别适合资源受限的实时应用，同时层次化推理结构为可解释性 AI 提供了新范式，有助于提升复杂视频问答系统的透明度与可靠性。
