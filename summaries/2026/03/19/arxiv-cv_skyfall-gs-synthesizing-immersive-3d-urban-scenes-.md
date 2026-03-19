---
title: "Skyfall-GS: Synthesizing Immersive 3D Urban Scenes from Satellite Imagery"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.15869"
published: "2026-03-19"
summarized: "2026-03-19T16:26:53.625992"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Skyfall-GS，一种创新的混合框架，用于从卫星图像合成可沉浸式探索的城市街区规模3D城市场景。该方法通过结合卫星重建与扩散模型精修，无需昂贵的3D标注数据即可生成几何一致性强、纹理逼真的大规模3D场景，并支持实时沉浸式3D漫游。实验表明，该方法在跨视图几何一致性和纹理真实感方面优于现有最先进方法。

【方法概述 / Method】
Skyfall-GS采用卫星图像重建获取粗略几何结构，并利用开放域扩散模型合成高质量近景外观，形成混合生成流程。该方法设计了课程驱动的迭代精修策略，逐步提升几何完整性和照片级真实纹理，最终基于3D高斯溅射（3D Gaussian Splatting）实现高效渲染。

【实验结果 / Results】
实验结果表明，Skyfall-GS在跨视图几何一致性方面显著优于现有方法，同时生成更具照片真实感的纹理细节。该方法能够实时渲染城市街区规模的复杂城市场景，在沉浸式探索中保持稳定的视觉质量。

【应用价值 / Applications】
该技术可广泛应用于虚拟现实城市漫游、自动驾驶仿真训练、游戏开发及城市规划可视化等领域，为需要大规模真实3D城市场景但缺乏专业扫描设备的应用场景提供了低成本、高效率的解决方案。
