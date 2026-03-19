---
title: "DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive Architecture"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.17354"
published: "2026-03-19"
summarized: "2026-03-19T16:27:57.304595"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了DSeq-JEPA，一种判别式序列联合嵌入预测架构，旨在改进I-JEPA并行预测所有目标区域的局限性。该方法受人类视觉感知启发，通过注意力机制生成显著性图来识别主要判别区域，并按判别重要性顺序依次预测后续区域，从而在预训练中实现从主要到次要线索的课程式语义递进。实验表明，DSeq-JEPA在图像分类、细粒度视觉分类、检测/分割及低级推理等多项任务上均优于I-JEPA变体，学习到更具判别性和泛化能力的表征。

【方法概述 / Method】

DSeq-JEPA的核心方法是将判别式有序序列过程与JEPA风格的潜在空间预测目标相结合。具体而言，该方法首先利用注意力派生的显著性图作为视觉重要性的代理，识别图像中的主要判别区域；然后以判别重要性为顺序，自回归地预测后续区域，使模型在预训练阶段遵循从显著到次要的语义学习路径。

【实验结果 / Results】

论文在多个基准任务上进行了广泛验证：ImageNet图像分类、iNaturalist21/CUB/Stanford Cars细粒度分类、MS-COCO/ADE20K检测与分割，以及CLEVR低级推理任务。实验结果表明，DSeq-JEPA在所有这些任务上均一致地超越了I-JEPA变体，展现出更强的判别性和泛化能力。

【应用价值 / Applications】

DSeq-JEPA可广泛应用于需要高质量视觉表征的下游任务，包括通用图像识别、细粒度物种/车型分类、目标检测与语义分割等视觉感知任务，以及视觉推理等需要结构化理解场景的研究领域。该方法通过模拟人类注意力机制的有序感知过程，为自监督预训练提供了更具生物合理性的新范式，有望提升模型在实际复杂视觉环境中的适应性和可解释性。
