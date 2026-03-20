---
title: "Remove360: Benchmarking Residuals After Object Removal in 3D Gaussian Splatting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2508.11431"
published: "2026-03-20"
summarized: "2026-03-20T16:12:36.453168"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了首个针对3D高斯泼溅（3D Gaussian Splatting）中物体移除后语义残差（semantic residuals）的基准测试与评估框架。研究发现，即使物体在视觉上被移除，现代视觉基础模型仍能从残留线索中推断出原本存在的物体，且即使结合图像修复（inpainting）技术，语义信息仍可能被恢复。作者还发布了Remove360真实世界数据集，包含复杂 cluttered 场景的移除前后RGB图像及物体级掩码，直接评估语义消除效果。

【方法概述 / Method】

论文构建了一个系统化的评估框架，通过对比移除前后的真实图像（ground-truth post-removal images），量化分析几何移除与语义擦除之间的差距。该框架利用视觉基础模型检测移除区域是否仍存在可恢复的语义信息，并引入Remove360数据集——该数据集包含360度全景捕获的室内外复杂场景，涵盖物体移除前后的配对数据，突破了以往数据集仅关注孤立物体实例的局限。

【实验结果 / Results】

实验表明，当前主流的3D编辑方法在物体移除后普遍保留了语义残差，即使结合2D图像修复技术也无法完全消除可恢复的线索。视觉基础模型能够持续检测到这些残留语义信息，揭示了几何移除与真正语义隐私保护之间的系统性差距。结果凸显了现有3D高斯泼溅编辑流程在隐私安全方面的关键缺陷。

【应用价值 / Applications】

该研究对隐私敏感场景（如虚拟现实、数字孪生、自动驾驶模拟）具有重要价值，推动开发真正"遗忘"敏感信息的3D编辑技术。Remove360数据集为社区提供了标准化的评估工具，促进隐私感知（privacy-aware）的物体移除方法研究，在内容审核、数据脱敏和可信AI系统构建等领域具有广泛应用前景。
