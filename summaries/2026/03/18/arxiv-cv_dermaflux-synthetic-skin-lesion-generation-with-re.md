---
title: "DermaFlux: Synthetic Skin Lesion Generation with Rectified Flows for Enhanced Image Classification"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16392"
published: "2026-03-18"
summarized: "2026-03-18T18:12:26.663591"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DermaFlux，一种基于校正流（rectified flow）的文本到图像生成框架，用于合成具有临床依据的皮肤病变图像。该框架通过低秩适应（LoRA）对Flux.1进行参数高效微调，并利用Llama 3.2生成符合皮肤病学标准的文本描述。实验表明，DermaFlux生成的合成数据可将小样本真实数据集的二分类性能提升高达6%，相比基于扩散模型的合成数据提升高达9%，仅用2,500张真实图像和4,375张合成样本即可达到78.04%的准确率和0.859的AUC。

【方法概述 / Method】
DermaFlux采用Flux.1作为基础架构，通过LoRA进行参数高效微调，以合成皮肤病变图像。研究构建了大规模图像-文本对数据集，其中文本描述由Llama 3.2根据皮肤病学标准（包括不对称性、边界不规则性和颜色变化等）生成，实现从自然语言描述到临床相关图像的生成。

【实验结果 / Results】
DermaFlux生成的合成图像在数据增强场景下将二分类性能提升6%，当完全使用合成数据训练时比扩散模型方法提升9%。最优配置（ImageNet预训练ViT + 2,500真实图像 + 4,375合成样本）达到78.04%准确率和0.859 AUC，超越现有最优皮肤病学模型8%。

【应用价值 / Applications】
该研究为医学影像领域的数据稀缺问题提供了解决方案，可广泛应用于皮肤病变分类系统的训练数据增强，改善类别不平衡导致的泛化性能下降问题。其方法可推广至其他医学影像模态，为开发更鲁棒的临床辅助诊断系统提供支持，同时降低对大规模标注临床数据的依赖。
