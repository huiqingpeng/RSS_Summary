---
title: "DreamPartGen: Semantically Grounded Part-Level 3D Generation via Collaborative Latent Denoising"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19216"
published: "2026-03-20"
summarized: "2026-03-20T13:21:29.438061"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DreamPartGen，一个用于语义驱动的部件级文本到3D生成的框架。该框架通过引入双重部件隐变量（DPLs）联合建模每个部件的几何与外观，以及关系语义隐变量（RSLs）捕捉部件间的语言派生依赖关系，实现了同步协同去噪过程以确保几何与语义的一致性。实验表明，该方法在几何保真度和文本-形状对齐方面达到了最先进的性能。

【方法概述 / Method】
DreamPartGen的核心创新在于设计了两种新型隐变量表示：DPLs将每个部件的几何和外观信息统一编码，RSLs则从文本描述中提取并编码部件间的语义关系。通过协同去噪机制，系统在生成过程中同步优化部件的几何一致性和语义对齐性，确保生成的3D对象既符合文本描述又具有合理的部件结构。

【实验结果 / Results】
在多个基准数据集上的评估显示，DreamPartGen在几何保真度和文本-形状对齐度两个关键指标上均达到 state-of-the-art 水平。该方法能够生成具有清晰语义部件划分、且各部件与文本描述高度一致的3D对象，显著优于现有的部件感知生成方法。

【应用价值 / Applications】
该研究可广泛应用于需要结构化3D内容的场景，如工业设计原型生成、机器人操作规划中的部件识别、以及增强现实/虚拟现实中的可交互3D资产创建。其语义 grounding 特性使得生成的3D模型更易于人类理解和程序解析，有助于推动3D内容生成向更智能、更可解释的方向发展。
