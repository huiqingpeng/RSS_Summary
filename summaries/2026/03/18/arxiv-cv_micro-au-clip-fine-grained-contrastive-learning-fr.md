---
title: "Micro-AU CLIP: Fine-Grained Contrastive Learning from Local Independence to Global Dependency for Micro-Expression Action Unit Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16302"
published: "2026-03-18"
summarized: "2026-03-18T18:10:47.158503"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对微表情动作单元（Micro-AU）检测任务，提出了一种新颖的对比学习框架Micro-AU CLIP。该框架创新性地将AU检测过程分解为局部语义独立建模（LSI）和全局语义依赖建模（GSD）两个阶段，分别捕捉AU的局部肌肉运动特性和AU间的内在依赖关系。此外，针对CLIP在微语义对齐方面的局限性，设计了微AU对比损失（MiAUCL）以实现视觉-文本特征的细粒度对齐。实验表明，该方法在Micro-AU检测和微表情识别任务上均达到了最先进的性能。

【方法概述 / Method】
本文提出的Micro-AU CLIP框架包含三个核心组件：在LSI阶段，设计Patch Token Attention（PTA）机制将AU区域内的多个局部特征映射到同一特征空间；在GSD阶段，通过Global Dependency Attention（GDA）和Global Dependency Loss（GDLoss）建模不同AU间的全局依赖关系；同时设计Micro-AU Contrastive Loss（MiAUCL）弥补CLIP在微语义对齐上的不足，实现视觉与文本特征的细粒度对齐。

【实验结果 / Results】
实验结果表明，Micro-AU CLIP能够充分学习细粒度的微AU特征，在Micro-AU检测任务上取得了最先进的性能。此外，该方法还可有效应用于无情绪标签的微表情识别任务，验证了所学AU特征的判别性和泛化能力。

【应用价值 / Applications】
该研究在情感计算和安全监控领域具有重要应用价值：一方面，Micro-AU检测为客观、细粒度的真实情感分析提供了可靠线索，可应用于测谎、临床心理评估等场景；另一方面，该方法支持无情绪标签的微表情识别，降低了对大量标注数据的依赖，提升了实际部署的便捷性和可扩展性。
