---
title: "VideoITG: Multimodal Video Understanding with Instructed Temporal Grounding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2507.13353"
published: "2026-03-18"
summarized: "2026-03-18T18:26:31.274301"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了VideoITG框架，旨在解决视频大语言模型（Video-LLMs）中如何根据用户指令自适应选择信息最丰富帧的关键挑战。现有方法在减少帧间冗余或无监督事件定位方面存在不足，难以处理复杂指令遵循任务和精确时间建模场景。为此，作者设计了VidThinker自动化标注流程，构建了包含40K视频和500K时间定位标注的VideoITG-40K数据集，并开发了即插即用的VideoITG模型，在多个多模态视频理解基准上取得一致性能提升。

【方法概述 / Method】

VideoITG采用指令驱动的时间定位策略，通过VidThinker管道实现自动化数据构建：首先生成指令条件化的视频描述，然后检索相关视频片段，最后选择关键帧以提供高效监督。该模型利用Video-LLMs的视觉-语言对齐和推理能力进行判别式帧选择，可根据不同用户指令自适应定制采样策略。

【实验结果 / Results】

VideoITG作为即插即用模块，在多个多模态视频理解基准上持续提升了性能，验证了其在语义对齐和时间推理方面的有效性。具体数值结果未在摘要中详细披露，但实验表明该方法在复杂指令遵循和精确时间建模场景下显著优于现有帧采样方法。

【应用价值 / Applications】

VideoITG可广泛应用于需要高效视频理解的场景，如长视频问答、视频摘要生成、指令驱动的视频检索等，特别是在计算资源受限或需要实时响应的系统中。该方法通过自适应帧采样显著降低视频处理开销，同时保持或提升理解精度，对构建更高效的多模态AI系统具有重要价值。
