---
title: "Unlocking 3D Affordance Segmentation with 2D Semantic Knowledge"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.08316"
published: "2026-03-18"
summarized: "2026-03-18T18:27:33.746657"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种利用大规模2D视觉基础模型（VFMs）语义知识来增强3D可供性分割的新方法。针对现有3D方法在几何线索模糊时功能信息不足的问题，作者设计了跨模态亲和迁移（CMAT）预训练策略，通过跨模态对齐机制将2D语义结构迁移到3D表示学习中。实验表明，该方法在准确性和效率上均显著优于现有最先进方法。

【方法概述 / Method】
核心方法为Cross-Modal Affinity Transfer（CMAT），通过亲和度对齐目标强制3D编码器与提升后的2D特征语义结构对齐，辅以几何重建和特征多样性两个辅助损失。在此基础上，采用轻量级可供性分割器，通过高效交叉注意力接口将文本或视觉提示注入学习到的3D空间，实现密集且提示感知的可供性预测。

【实验结果 / Results】
论文通过大量实验验证了CMAT预训练策略的有效性，在3D可供性分割任务上相比先前最优方法取得了持续的准确率提升，同时保持了较高的计算效率。具体量化指标未在摘要中详述，但强调了"consistent improvements over previous state-of-the-art methods in both accuracy and efficiency"。

【应用价值 / Applications】
该研究可应用于机器人操作规划、人机交互和增强现实等领域，使智能系统能够理解物体部件的功能属性而非仅识别几何形状。通过结合2D语义知识与3D几何信息，该方法有望提升机器人在复杂环境中进行功能性物体交互的能力，推动具身智能的发展。
