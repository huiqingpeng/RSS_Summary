---
title: "Can VLMs Reason Robustly? A Neuro-Symbolic Investigation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23867"
published: "2026-03-26"
summarized: "2026-03-27T07:18:18.138065"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了视觉-语言模型（VLMs）在分布偏移下的推理鲁棒性问题。研究发现，通过端到端梯度微调训练的VLMs虽然在分布内数据上表现优异，但在协变量偏移（covariate shifts）下泛化能力显著下降，表明微调并不能可靠地诱导出底层的推理函数。为此，作者提出了VLC（Vision-Language Circuits）方法，将VLM-based概念识别与基于电路的符号推理相结合，在三种视觉演绎推理任务上实现了对分布偏移的强鲁棒性。

【方法概述 / Method】
VLC采用神经-符号（neuro-symbolic）架构，将感知与推理解耦：使用VLM进行对象概念识别，同时将任务规则编译为符号电路（circuit-based symbolic program）来执行精确推理。这种设计避免了黑盒推理组件带来的不一致性问题，确保推理过程透明且可解释。

【实验结果 / Results】
在三种具有不同规则集的视觉演绎推理任务上，VLC在协变量偏移条件下始终保持强劲性能，显著优于端到端微调的VLMs和依赖黑盒推理组件的神经-符号基线方法。实验结果凸显了VLC支持鲁棒推理的能力，证明了显式符号推理在分布偏移场景下的优势。

【应用价值 / Applications】
该研究为高可靠性视觉推理系统的设计提供了重要思路，特别适用于自动驾驶、医疗影像诊断、工业质检等对鲁棒性要求严格的场景。VLC的模块化架构也为未来融合大型多模态模型与符号推理引擎的混合智能系统奠定了基础。
