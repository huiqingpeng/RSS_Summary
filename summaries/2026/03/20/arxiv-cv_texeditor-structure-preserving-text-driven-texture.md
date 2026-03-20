---
title: "TexEditor: Structure-Preserving Text-Driven Texture Editing"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18488"
published: "2026-03-20"
summarized: "2026-03-20T15:10:00.852184"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对文本引导纹理编辑中结构保持的挑战，提出了TexEditor模型。作者发现即使最先进的编辑模型在纯外观修改时也难以保持几何结构一致性，因此从数据和训练两个角度联合增强结构保持能力。研究还构建了TexBench真实世界基准测试，实验表明TexEditor在现有Blender基准和TexBench上均显著优于Nano Banana Pro等强基线模型。

【方法概述 / Method】
TexEditor基于Qwen-Image-Edit-2509构建，采用两阶段训练策略：首先构建TexBlender高质量监督微调数据集，利用Blender生成提供强结构先验的合成数据；其次提出StructureNFT强化学习方法，将监督学习阶段获得的结构先验迁移到真实场景，通过集成结构保持损失函数实现结构一致性优化。

【实验结果 / Results】
TexEditor在Blender合成纹理基准和自建的TexBench真实世界基准上均一致超越Nano Banana Pro等强基线模型。此外，在通用图像编辑基准ImgEdit上的评估验证了模型的泛化能力，证明该方法不仅在纹理编辑任务表现优异，也具备良好的通用编辑能力。

【应用价值 / Applications】
该研究可广泛应用于数字内容创作、游戏资产制作、电商产品展示等领域，使设计师能通过自然语言指令精确修改物体外观而保持几何结构稳定。TexBench基准的建立也为后续纹理编辑研究提供了更贴近真实场景的评估标准，推动该领域向实用化发展。
