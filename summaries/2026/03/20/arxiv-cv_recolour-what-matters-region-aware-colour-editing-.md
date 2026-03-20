---
title: "Recolour What Matters: Region-Aware Colour Editing via Token-Level Diffusion"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18466"
published: "2026-03-20"
summarized: "2026-03-20T15:09:45.855392"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ColourCrafter，一种统一的扩散框架，将图像颜色编辑从全局色调转移转变为结构化、区域感知的生成过程。该方法通过在潜在空间中对RGB颜色token和图像token进行token级融合，实现颜色信息向语义相关区域的选择性传播，同时保持结构保真度。此外，研究构建了ColourfulSet大规模数据集，包含高质量、连续多样颜色变化的图像对。实验表明，ColourCrafter在细粒度颜色编辑中达到了最先进的颜色准确性、可控性和感知保真度。

【方法概述 / Method】
ColourCrafter采用token级扩散机制，在潜在空间中将RGB颜色token与图像token融合，实现区域感知的颜色编辑。该方法引入感知Lab空间损失函数，通过解耦亮度和色度并约束编辑在掩码区域内，增强像素级精度。整体框架将连续颜色变化表示为可学习的token嵌入，克服了传统文本驱动方法中离散语言描述无法准确表达连续色度变化的局限。

【实验结果 / Results】
大量实验验证了ColourCrafter在细粒度颜色编辑任务上的优越性能，在颜色准确性、可控性和感知保真度方面均达到当前最优水平。所构建的ColourfulSet数据集为训练和评估连续颜色变化提供了高质量基准，支持模型学习多样化的颜色转换模式。

【应用价值 / Applications】
该研究可广泛应用于图像编辑软件、数字内容创作和影视后期制作等领域，使用户能够精确控制图像中特定区域的颜色属性。其连续颜色控制能力特别适用于需要精细色彩调整的专业设计场景，如产品摄影、时尚设计和广告制作，显著提升视觉内容创作的效率和灵活性。
