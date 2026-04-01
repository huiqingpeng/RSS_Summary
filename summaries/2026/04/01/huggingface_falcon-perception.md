---
title: "Falcon Perception"
source: "Hugging Face Blog"
url: "https://huggingface.co/blog/tiiuae/falcon-perception"
published: "2026-04-01"
summarized: "2026-04-02T07:10:03.049918"
ai_provider: "openai"
---

【是什么 / What it is】

Falcon Perception 是一个 6 亿参数的**早期融合 Transformer 模型**，用于从自然语言提示中实现开放词汇的图像定位与分割。它采用混合注意力掩码将图像块和文本统一处理为单一序列，并通过"感知链"（Chain-of-Perception）结构——先预测坐标、再预测尺寸、最后生成分割掩码——来高效输出可变数量的实例。

Falcon Perception is a 0.6B-parameter **early-fusion Transformer** for open-vocabulary grounding and segmentation from natural language prompts. It processes image patches and text as a unified sequence using a hybrid attention mask, and efficiently produces variable numbers of instances through a "Chain-of-Perception" structure—predicting coordinates first, then size, then segmentation masks.

---

【为什么重要 / Why it matters】

该模型挑战了当前主流的"流水线式"感知架构（冻结视觉骨干 + 独立融合解码器），证明单一早期融合骨干网络即可同时处理感知和语言建模，大幅简化了系统复杂度。在 SA-1B 数据集上，它以 68.0 的 Macro-F1 超越 SAM 3（62.3），同时团队还发布了诊断性基准 PBench，首次将感知能力拆解为属性理解、OCR 引导、空间关系等维度，解决了传统基准饱和且难以定位失败原因的问题。

The model challenges the dominant "pipeline" perception paradigm (frozen vision backbone + separate fusion decoder), demonstrating that a single early-fusion backbone can handle both perception and language modeling, dramatically reducing system complexity. It achieves 68.0 Macro-F1 on SA-1B vs. SAM 3's 62.3, while the team also released PBench—a diagnostic benchmark that decomposes perception capabilities into attributes, OCR guidance, spatial relations, etc.—addressing the saturation and opaqueness of traditional benchmarks.

---

【我能用什么 / How I can use it】

开发者可将 Falcon Perception 用于需要**自然语言驱动的图像分割**场景，如智能标注、视觉问答、机器人指令执行等；其"感知链"设计思路也可迁移到其他需要**结构化稀疏输出**的密集预测任务。对于研究者，PBench 的分层评估框架提供了清晰的模型能力画像，可指导数据收集和训练课程设计；同时该模型的早期融合架构为多模态统一建模提供了可借鉴的技术路线。

Developers can apply Falcon Perception to **language-driven image segmentation** scenarios like intelligent annotation, visual question answering, and robotic instruction following; its "Chain-of-Perception" design is also transferable to other dense prediction tasks requiring **structured sparse outputs**. For researchers, PBench's tiered evaluation framework provides clear capability profiling to guide data collection and training curricula, while the model's early-fusion architecture offers a reference technical path toward unified multimodal modeling.
