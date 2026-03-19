---
title: "Rel-Zero: Harnessing Patch-Pair Invariance for Robust Zero-Watermarking Against AI Editing"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17531"
published: "2026-03-19"
summarized: "2026-03-19T15:13:07.334890"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对基于扩散模型的AI图像编辑对数字内容真实性的威胁，提出了一种新型零水印框架Rel-Zero。核心发现是：AI编辑虽然会显著改变单个图像块，但块对之间的相对距离关系保持相对稳定。基于这一观察，Rel-Zero无需修改原始图像，仅从图像内部固有的结构一致性中提取水印，在多种编辑模型和操纵方式下均显著优于现有零水印方法。

【方法概述 / Method】
Rel-Zero利用"块对不变性"（patch-pair invariance）作为核心机制，通过量化图像块之间的相对距离关系而非绝对外观特征来生成零水印。该方法将水印锚定在图像的内在结构一致性上，避免了传统嵌入式水印的视觉失真问题，同时克服了基于全局特征的零水印方法对复杂编辑的脆弱性。

【实验结果 / Results】
实验表明，Rel-Zero在多种主流扩散编辑模型（如Stable Diffusion、InstructPix2Pix等）和多样化图像操纵下展现出显著增强的鲁棒性。与现有零水印方法相比，该方法在保持零嵌入扰动的同时，实现了对AI编辑攻击的更高检测准确率和更低误检率。

【应用价值 / Applications】
Rel-Zero可广泛应用于AIGC内容溯源、深度伪造检测、数字版权保护等场景，特别适用于对视觉质量要求严格的领域（如专业摄影、医学影像、卫星图像）。其非侵入式特性使其能够在不损害原始内容的前提下，为AI生成和编辑内容的可信认证提供技术支撑。
