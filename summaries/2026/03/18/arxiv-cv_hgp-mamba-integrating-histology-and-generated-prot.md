---
title: "HGP-Mamba: Integrating Histology and Generated Protein Features for Mamba-based Multimodal Survival Risk Prediction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16421"
published: "2026-03-18"
summarized: "2026-03-18T18:12:47.231773"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了HGP-Mamba，一种基于Mamba架构的多模态框架，用于整合组织病理学图像与生成的蛋白质特征进行癌症生存风险预测。该框架通过蛋白质特征提取器（PFE）从全切片图像（WSIs）中生成高通量蛋白质嵌入，克服了蛋白质表达谱数据获取成本高、可用性有限的瓶颈。结合局部交互感知Mamba（LiAM）和全局交互增强Mamba（GiEM）模块，实现了细粒度特征交互与整体模态融合。在四个公共癌症数据集上的实验表明，该方法在保持优越计算效率的同时达到了最先进的性能。

【方法概述 / Method】

HGP-Mamba的核心方法包括：（1）蛋白质特征提取器（PFE），利用预训练基础模型直接从WSIs生成蛋白质嵌入，无需实际的蛋白质组学数据；（2）局部交互感知Mamba（LiAM），用于捕捉组织病理学嵌入与蛋白质嵌入之间的细粒度局部交互；（3）全局交互增强Mamba（GiEM），在切片级别促进两种模态的整体融合，捕获复杂的跨模态依赖关系。整个框架基于Mamba架构，具有线性计算复杂度的优势。

【实验结果 / Results】

在四个公共癌症数据集上的实验表明，HGP-Mamba在生存风险预测任务上达到了最先进的性能（state-of-the-art），同时相比现有方法具有显著更优的计算效率。具体而言，该方法通过生成的蛋白质特征有效补充了组织病理学信息，验证了多模态融合策略在提升预测准确性和效率方面的有效性。

【应用价值 / Applications】

HGP-Mamba的实际应用价值主要体现在：（1）为资源受限的临床环境提供了一种经济高效的癌症预后评估方案，无需昂贵的蛋白质组学检测即可利用分子层面信息；（2）可广泛应用于多种癌症类型的生存风险分层，辅助临床决策和个性化治疗方案制定；（3）该生成式蛋白质特征提取策略有望推广至其他需要多模态数据但面临数据稀缺问题的生物医学场景。
