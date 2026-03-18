---
title: "From Geometric Mimicry to Comprehensive Generation: A Context-Informed Multimodal Diffusion Model for Urban Morphology Synthesis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2409.17049"
published: "2026-03-18"
summarized: "2026-03-18T18:24:52.903670"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究提出ControlCity，一种基于多模态扩散模型的城市形态综合生成方法，突破了传统方法将城市形态生成简化为几何问题的局限。研究构建了包含图像-文本-元数据-建筑轮廓的四重数据集，通过增强型ControlNet融合空间约束、语义指导和地理上下文信息，实现了从"几何模仿"到"综合生成"的范式转变。实验表明该方法在形态保真度上显著优于单模态基线，并具备跨城市风格迁移和零样本生成能力。

【方法概述 / Method】

ControlCity采用多模态信息融合策略，以扩散模型为核心架构：图像数据通过增强型ControlNet编码为空间约束条件，文本描述提供语义指导，元数据注入地理上下文信息，三者共同引导城市形态生成。该方法基于全球22个城市构建的四重数据集进行训练，实现了对城市形态的多维度控制。

【实验结果 / Results】

与单模态基线相比，ControlCity在形态保真度指标上取得显著提升：FID分数降低71.01%至50.94（视觉误差更小），MIoU提升38.46%至0.36（空间重叠度更高）。消融实验揭示了图像、文本和元数据在生成过程中的各自作用，验证了多模态融合的有效性。模型还展现出强大的知识泛化能力和可控性。

【应用价值 / Applications】

该研究为城市规划设计提供了智能化生成工具，支持跨城市风格迁移和未知城市的零样本生成，可辅助快速城市形态方案比选与决策。多模态融合范式为城市形态研究开辟了新方向，在智慧城市、历史风貌保护、新区开发等场景具有广泛应用潜力，有助于提升城市功能性与活力的科学预判能力。
