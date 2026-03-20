---
title: "Inst4DGS: Instance-Decomposed 4D Gaussian Splatting with Multi-Video Label Permutation Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18402"
published: "2026-03-20"
summarized: "2026-03-20T15:08:11.438014"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Inst4DGS，一种实例分解的4D高斯溅射方法，能够实现长时域的逐高斯轨迹建模。针对多视角视频中实例标签不一致导致的关联难题，作者引入可微分Sinkhorn层学习跨视频实例匹配，实现了显式标签对齐和时序稳定的身份保持。此外，该方法还提出了实例分解的运动支架结构，为长时域轨迹优化提供低维运动基。实验表明，该方法在Panoptic Studio和Neural3DV数据集上同时支持跟踪与实例分解，达到了最先进的渲染和分割质量。

【方法概述 / Method】
Inst4DGS的核心方法是引入逐视频的标签置换隐变量，通过可微分Sinkhorn层学习跨视频的实例匹配关系，从而将独立分割的多视角视频进行标签对齐。同时，该方法设计了实例分解的运动支架（motion scaffolds），为每个物体提供低维运动基，以高效优化长时域的高斯轨迹。

【实验结果 / Results】
在Panoptic Studio数据集上，Inst4DGS相比最强基线将PSNR从26.10提升至28.36，实例mIoU从0.6310大幅提升至0.9129。该方法在Neural3DV数据集上也取得了优异表现，证明了其在渲染质量和实例分割精度上的双重优势。

【应用价值 / Applications】
Inst4DGS可应用于动态场景的4D重建、多目标跟踪与实例分割等任务，适用于虚拟现实、增强现实、自动驾驶感知以及运动分析等领域。该方法通过显式的实例分解和稳定的身份保持，为需要精确物体级理解的下游应用提供了可靠的技术基础。
