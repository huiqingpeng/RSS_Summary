---
title: "Scalable Object Relation Encoding for Better 3D Spatial Reasoning in Large Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24721"
published: "2026-03-27"
summarized: "2026-03-28T07:15:50.296203"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对大型语言模型（LLMs）在3D空间推理任务中的局限性，提出了QuatRoPE——一种可扩展的位置编码方法，用于解决现有方法在绝对位置编码难以提取空间关系与显式编码所有空间关系导致输入长度二次增长之间的权衡问题。该方法通过四元数表示3D坐标，使输入长度与物体数量呈线性关系，并在注意力层通过点积显式计算成对空间关系。同时引入的IGRE机制有效隔离了新位置编码对LLM原有能力的干扰，实验验证了该方法在3D空间推理任务上的有效性。

【方法概述 / Method】
QuatRoPE采用四元数（quaternion）对3D坐标进行整体向量编码，将每个物体的位置和朝向信息编码为固定长度的向量表示，使输入序列长度与物体数量N保持O(N)线性关系而非O(N²)。在Transformer的注意力计算中，通过查询-键向量的点积自然推导出物体间的相对空间关系，无需显式生成所有配对关系作为输入。IGRE（Isolated Gated RoPE Extension）通过门控机制将QuatRoPE的作用范围限制在物体相关token上，避免干扰LLM原有的文本位置编码。

【实验结果 / Results】
论文通过大量实验验证了QuatRoPE的有效性，在3D空间推理基准测试中展现出优于绝对位置编码方法和显式关系编码方法的性能。该方法在保持较高空间一致性的同时实现了良好的可扩展性，能够处理包含更多物体的复杂3D场景。具体定量结果虽未在摘要中详述，但实验表明QuatRoPE在维持LLM原有语言能力的同时显著提升了空间推理表现。

【应用价值 / Applications】
该研究对具身智能（embodied AI）和机器人领域具有重要价值，可应用于智能机器人在复杂3D环境中的导航、物体操控和任务规划等场景。QuatRoPE的线性复杂度特性使其能够扩展到大规模真实环境，支持智能家居助手、自动驾驶感知与决策、以及虚拟现实/增强现实中的自然语言交互等应用，为开发具备强空间理解能力的通用智能体提供了有效技术路径。
