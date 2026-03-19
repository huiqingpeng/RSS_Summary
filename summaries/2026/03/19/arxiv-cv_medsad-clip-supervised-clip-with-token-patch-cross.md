---
title: "MedSAD-CLIP: Supervised CLIP with Token-Patch Cross-Attention for Medical Anomaly Detection and Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17325"
published: "2026-03-19"
summarized: "2026-03-19T15:08:20.179236"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MedSAD-CLIP，一种针对医学异常检测与分割的监督式CLIP自适应方法。该研究突破了现有CLIP-based方法依赖全局表征和弱监督、导致定位粗放的局限，在有限标注异常数据的真实临床场景下，通过Token-Patch Cross-Attention机制融合细粒度文本-视觉线索，显著提升了病灶定位精度。在脑部、视网膜、肺部和乳腺四个多样化数据集上的实验表明，该方法在像素级分割和图像级分类任务上均优于现有最优方法，展现了监督式CLIP自适应作为统一可扩展范式的潜力。

【方法概述 / Method】
MedSAD-CLIP采用轻量级图像适配器和可学习提示令牌对预训练CLIP编码器进行高效医学域自适应，同时保持其丰富的语义对齐能力。核心创新在于Token-Patch Cross-Attention（TPCA）模块，该模块建立文本令牌与图像块之间的细粒度跨模态交互，实现精确的病变定位。此外，设计了基于边界的图像-文本对比损失（Margin-based Contrastive Loss），增强正常与异常表征的全局特征区分度。

【实验结果 / Results】
在Brain、Retina、Lung和Breast四个医学影像基准数据集上进行了广泛验证，MedSAD-CLIP在像素级异常分割和图像级异常分类两项任务上均取得最先进的性能。实验结果证明了该方法在多样化医学模态和解剖部位上的强泛化能力，有效克服了零样本/少样本CLIP方法定位粗糙、分割质量受限的问题。

【应用价值 / Applications】
该研究为临床诊断提供了统一的医学异常理解框架，可辅助放射科医生自动识别和定位CT、MRI、眼底照相、X光及乳腺钼靶等多种模态影像中的病理区域。其监督自适应策略在有限标注数据下即可实现高性能，降低了大规模医学数据标注成本，具有良好的临床部署前景和可扩展性。
