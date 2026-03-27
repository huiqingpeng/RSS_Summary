---
title: "Lookalike3D: Seeing Double in 3D"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24713"
published: "2026-03-27"
summarized: "2026-03-28T07:15:35.466796"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了室内场景中"相似物体检测"（lookalike object detection）这一新任务，旨在利用重复和互补的视觉线索对成对物体进行"相同/相似/不同"的三分类。作者构建了包含76k人工标注对的3DTwins数据集，并开发了基于多视图图像Transformer的Lookalike3D方法，相比基线方法IoU提升104%。该研究展示了相似物体检测可显著提升联合3D物体重建与部件协同分割等下游任务的性能。

【方法概述 / Method】
Lookalike3D采用多视图图像Transformer架构，通过利用大规模图像基础模型的强语义先验来有效区分相同或近似的物体对。该方法以多视角图像作为输入，学习捕捉物体间的细微视觉差异与语义关联。

【实验结果 / Results】
在基于ScanNet++构建的3DTwins数据集上，Lookalike3D相比基线方法实现了104%的IoU性能提升。实验验证了该方法在下游任务中的有效性，包括联合3D物体重建和部件协同分割，证明重复与相似物体可作为一致高质量3D感知的强有力线索。

【应用价值 / Applications】
该研究可广泛应用于室内场景理解、机器人导航、AR/VR内容生成等领域，通过识别场景中的重复物体来增强3D重建的一致性和完整性。特别地，在智能家居、仓储物流等包含大量相同或相似物体的场景中，该方法可提升自动化系统的场景解析与物体操作能力。
