---
title: "GTAvatar: Bridging Gaussian Splatting and Texture Mapping for Relightable and Editable Gaussian Avatars"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.09162"
published: "2026-03-20"
summarized: "2026-03-20T16:16:11.273839"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了GTAvatar方法，将高斯溅射（Gaussian Splatting）的渲染精度与UV纹理映射的直观可编辑性相结合，实现了从单目视频重建可重光照、可编辑的人头化身。通过将规范高斯基元的局部帧嵌入到模板网格的UV空间中，该方法在常规UV域上重建连续可编辑的材质纹理，并利用高效的物理基础反射模型实现内在材质图的重光照和编辑。实验表明，该方法在重建精度、重光照质量和纹理编辑便利性方面均达到先进水平。

【方法概述 / Method】

GTAvatar的核心是将3D高斯基元与2D UV纹理空间桥接：每个高斯基元的局部坐标系被嵌入到模板网格UV空间的一个patch中，使得高斯参数可通过UV纹理进行存储和编辑。该方法采用高效的物理基础渲染（PBR）模型，将外观解耦为漫反射、镜面反射和法线等内在材质属性，支持在UV域上直接进行材质编辑而无需额外优化。

【实验结果 / Results】

与现有最先进方法的大量对比实验表明，GTAvatar在重建精度上达到或超越纯高斯溅射方法，同时实现了高质量的重光照效果。该方法能够从单目视频生成连续可编辑的材质纹理，并支持通过标准图像编辑工具直接修改UV纹理来改变化身外观和几何，无需重新训练或优化。

【应用价值 / Applications】

GTAvatar可广泛应用于视觉特效制作、视频会议和虚拟现实等领域，特别适用于需要实时渲染和直观编辑的数字人应用场景。该方法使艺术家和用户能够使用熟悉的纹理编辑工作流程来修改化身外观，降低了高保真数字人内容创作的技术门槛，为可重光照、可驱动的虚拟化身提供了实用解决方案。
