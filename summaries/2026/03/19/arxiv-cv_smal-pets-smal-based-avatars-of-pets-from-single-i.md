---
title: "SMAL-pets: SMAL Based Avatars of Pets from Single Image"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17131"
published: "2026-03-19"
summarized: "2026-03-19T15:05:50.421667"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SMAL-pets框架，能够从单张图像生成高质量、可编辑的3D宠物化身。该方法通过混合架构弥合了重建与生成建模之间的差距，将3D高斯溅射与SMAL参数模型相结合，实现了视觉高保真且解剖学合理的表示。此外，作者还引入了多模态编辑套件，允许用户通过自然语言文本提示来优化外观并执行复杂动画，为动画和虚拟现实应用提供了灵活 robust 的工具。

【方法概述 / Method】
SMAL-pets采用混合架构，将3D高斯溅射（3D Gaussian Splatting）与SMAL（Skinned Multi-Animal Linear）参数化模型相结合，既保证了视觉质量又提供了解剖学基础。该框架还集成了多模态编辑功能，支持用户通过文本提示直接控制化身的外观美感和行为动作。

【实验结果 / Results】
论文指出当前动物重建方法在捕捉真实毛发纹理方面存在困难，而SMAL-pets能够有效生成高保真度的可动画化身。该方法通过自然语言控制实现了对美学和行为方面的双重调控，克服了传统方法需要繁琐手动网格操作和专业骨骼绑定的局限。

【应用价值 / Applications】
SMAL-pets可广泛应用于动画制作和虚拟现实领域，为创建数字宠物化身提供高效工具。其基于文本提示的编辑方式大幅降低了专业门槛，使非专业用户也能轻松生成和操控复杂的动物动画，在娱乐、游戏、虚拟宠物交互等场景具有重要价值。
