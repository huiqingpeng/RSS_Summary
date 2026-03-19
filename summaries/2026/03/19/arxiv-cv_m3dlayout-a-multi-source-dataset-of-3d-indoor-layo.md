---
title: "M3DLayout: A Multi-Source Dataset of 3D Indoor Layouts and Structured Descriptions for 3D Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.23728"
published: "2026-03-19"
summarized: "2026-03-19T16:26:04.550246"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了M3DLayout，一个大规模、多源的3D室内布局数据集，用于文本驱动的3D场景生成。该数据集包含21,367个布局和超过433k个物体实例，整合了真实扫描、专业CAD设计和程序化生成三种来源，每个布局配有结构化的文本描述。实验表明，该数据集的多源组成增强了多样性，特别是Inf3DLayout子集提供了丰富的小物体信息，能够生成更复杂详细的场景。

【方法概述 / Method】
M3DLayout通过整合三种不同来源的数据（真实世界扫描、专业CAD设计和程序化生成场景）来构建数据集，并为每个布局提供全局场景摘要、大型家具关系放置和小型物品精细布局的结构化文本描述。为评估数据集潜力，研究者建立了基于文本条件扩散模型和自回归模型的基准测试。

【实验结果 / Results】
实验结果表明M3DLayout为布局生成模型训练提供了坚实基础，其多源组成显著增强了数据多样性；特别是Inf3DLayout子集通过提供丰富的小物体信息，使模型能够生成更复杂和详细的室内场景，验证了数据集在提升生成质量方面的有效性。

【应用价值 / Applications】
该数据集可广泛应用于文本驱动的3D室内场景合成、智能室内设计、虚拟现实环境构建等领域，为研究人员提供高质量的训练资源；同时支持语义可控性和交互式编辑，有助于开发更智能的3D内容创作工具和游戏/元宇宙场景生成系统。
