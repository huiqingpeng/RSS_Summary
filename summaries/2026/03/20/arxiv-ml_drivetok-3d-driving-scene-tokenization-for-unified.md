---
title: "DriveTok: 3D Driving Scene Tokenization for Unified Multi-View Reconstruction and Understanding"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19219"
published: "2026-03-20"
summarized: "2026-03-20T13:21:40.179933"
ai_provider: "openai"
---

【论文摘要 / Abstract】
DriveTok 提出了一种面向自动驾驶场景的高效 3D 场景分词器，解决了现有 2D 单目分词器在多视图高分辨率驾驶场景中效率低下和视图不一致的问题。该方法通过 3D 可变形交叉注意力将视觉基础模型的语义特征转换为统一的场景 token，并采用多视图 transformer 解码器实现 RGB、深度和语义重建，同时直接在场景 token 上添加 3D 头进行语义占用预测。在 nuScenes 数据集上的实验表明，DriveTok 学习的统一场景 token 能够有效整合语义、几何和纹理信息，在图像重建、语义分割、深度预测和 3D 占用预测等多项任务上表现优异。

【方法概述 / Method】
DriveTok 首先利用视觉基础模型提取语义丰富的视觉特征，然后通过 3D 可变形交叉注意力机制将其转换为场景 token；解码阶段采用多视图 transformer 从场景 token 重建多视图特征，并通过多任务头输出 RGB、深度和语义信息，同时附加 3D 头直接进行 3D 语义占用预测。

【实验结果 / Results】
在 nuScenes 数据集上的大量实验验证了 DriveTok 的场景 token 在图像重建、语义分割、深度预测和 3D 语义占用预测等任务上的有效性，证明了统一场景 token 对多视图重建和理解任务的适用性。

【应用价值 / Applications】
DriveTok 可作为视觉-语言-动作模型和世界模型在自动驾驶系统中的视觉模态接口，为端到端自动驾驶提供高效、一致的多视图场景表示；其统一的 3D 场景 token 能够同时支持感知、预测和规划等多种下游任务，有助于提升自动驾驶系统的可扩展性和整体性能。
