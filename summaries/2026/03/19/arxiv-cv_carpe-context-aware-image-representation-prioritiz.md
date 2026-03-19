---
title: "CARPE: Context-Aware Image Representation Prioritization via Ensemble for Large Vision-Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.13622"
published: "2026-03-19"
summarized: "2026-03-19T16:30:27.273926"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为CARPE（Context-Aware Image Representation Prioritization via Ensemble）的轻量级框架，旨在解决大型视觉-语言模型（LVLMs）因自回归语言建模目标导致视觉表征与语言空间对齐后、视觉中心能力下降的问题。CARPE通过视觉集成层和上下文感知集成机制，将原始视觉特征与对齐后的LLM表征相结合，使模型能够自适应地加权视觉和文本模态。大量实验表明，该方法在图像分类和多种视觉-语言基准测试上均取得了性能提升，揭示了模态平衡对自回归LVLMs多模态泛化的关键作用。

【方法概述 / Method】
CARPE采用双分支架构，一支提取未经语言对齐的原始视觉编码器特征，另一支使用标准的LVLM对齐视觉表征，通过可学习的视觉集成层将两者融合。核心创新在于上下文感知集成机制，该机制根据输入内容动态调整两种视觉表征的权重，实现模态间的自适应平衡。

【实验结果 / Results】
实验结果显示，CARPE在图像分类任务上显著优于基线LVLMs，甚至超过其基础视觉编码器的性能；同时在视觉问答、图像描述生成等多模态基准上保持或提升原有表现。该框架以极低的额外参数量（轻量级设计）实现了视觉能力与多模态推理的协同增强。

【应用价值 / Applications】
CARPE可广泛应用于需要强视觉感知能力的多模态系统，如医学影像分析、自动驾驶视觉理解、工业质检等视觉中心任务，同时保持对话和推理能力。该方法为现有LVLMs提供即插即用的增强方案，无需重新预训练即可提升模型在视觉密集型应用中的可靠性。
