---
title: "R&D: Balancing Reliability and Diversity in Synthetic Data Augmentation for Semantic Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18427"
published: "2026-03-20"
summarized: "2026-03-20T15:08:36.712654"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种用于语义分割的合成数据增强新框架R&D，通过整合可控扩散模型来平衡合成数据的多样性与可靠性。该方法采用类别感知提示和视觉先验混合技术，确保生成图像与分割标签的精确对齐。在PASCAL VOC和BDD100K等基准数据集上的实验表明，该方法在数据稀缺场景下显著提升语义分割性能，并增强了模型在真实世界应用中的鲁棒性。

【方法概述 / Method】
论文采用基于可控扩散模型的合成数据增强流程，通过类别感知提示（class-aware prompting）实现对生成内容的精细控制，并引入视觉先验混合（visual prior blending）技术进一步提升图像质量。该方法核心在于平衡数据的多样性（diversity）与可靠性（reliability），有效缩小合成数据与真实数据之间的域差距。

【实验结果 / Results】
在PASCAL VOC和BDD100K等标准语义分割基准数据集上的评估显示，R&D方法显著提升了语义分割性能，尤其在训练数据有限的场景下效果更为明显。实验同时验证了该方法能够增强模型在真实世界应用中的鲁棒性，表明合成数据增强在提升模型泛化能力方面的有效性。

【应用价值 / Applications】
该研究为像素级语义分割任务提供了一种高效的低成本数据增强方案，可广泛应用于自动驾驶（如BDD100K场景）、医学图像分割等标注成本高昂的领域。通过减少对大规模人工标注数据的依赖，该方法有助于加速语义分割模型在资源受限环境下的部署，并提升模型面对真实世界复杂场景的适应能力。
