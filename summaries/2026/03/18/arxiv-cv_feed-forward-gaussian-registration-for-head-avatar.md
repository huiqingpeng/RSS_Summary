---
title: "Feed-forward Gaussian Registration for Head Avatar Creation and Editing"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15811"
published: "2026-03-18"
summarized: "2026-03-18T17:18:45.157640"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MATCH（Multi-view Avatars from Topologically Corresponding Heads），一种基于多视图高斯配准的高质量头部化身创建与编辑方法。与现有方法需要耗时数小时的头部追踪和昂贵的化身优化不同，MATCH仅需0.5秒即可直接从校准的多视图图像中预测对应的高斯 splat 纹理，无需数据预处理。该方法通过学习的帧内对应关系实现快速个性化化身创建，并通过跨主体对应关系支持表情迁移、免优化追踪、语义编辑和身份插值等应用。

【方法概述 / Method】
MATCH采用基于Transformer的端到端模型，在固定UV布局的模板网格上预测高斯 splat 纹理。核心创新是引入配准引导的注意力块，其中每个UV图token仅关注描绘其对应网格区域的图像token，而非密集跨视图注意力，从而提升效率与性能。

【实验结果 / Results】
MATCH在新视角合成、几何配准和头部化身生成方面均优于现有方法，同时使化身创建速度比最接近的竞争基线快10倍。该方法仅需0.5秒即可完成每帧处理，而传统方法通常需要超过一天的总创建时间。

【应用价值 / Applications】
该研究可广泛应用于实时虚拟化身生成、数字人内容创作、视频会议和VR/AR应用。其免优化特性支持即时个性化头像创建，而跨主体对应能力实现了表情迁移、语义编辑和身份混合等高级编辑功能，为交互式数字人应用提供了高效解决方案。
