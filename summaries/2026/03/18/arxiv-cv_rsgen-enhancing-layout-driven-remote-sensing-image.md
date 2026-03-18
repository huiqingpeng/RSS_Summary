---
title: "RSGen: Enhancing Layout-Driven Remote Sensing Image Generation with Diverse Edge Guidance"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15484"
published: "2026-03-18"
summarized: "2026-03-18T19:05:26.224394"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了RSGen，一种即插即用的框架，通过多样化边缘引导来增强布局驱动的遥感图像生成。针对现有Layout-to-Image（L2I）方法在细粒度控制和边界框约束遵守方面的不足，RSGen采用渐进式增强策略：首先通过图像到图像生成丰富检索训练实例合成的边缘图多样性，然后将这些多样化的边缘图作为条件输入现有L2I模型，实现边界框内的像素级控制。实验表明，RSGen能显著提升现有L2I模型的性能，例如在DOTA数据集上使用CC-Diff时，YOLOScore mAP50/mAP50-95分别提升9.8和12.0，下游检测任务mAP提升1.6。

【方法概述 / Method】
RSGen采用两阶段渐进增强策略：第一阶段利用图像到图像扩散模型对从训练集中检索实例合成的边缘图进行多样性增强，生成多样化的边缘条件；第二阶段将这些边缘图作为额外条件输入现有L2I扩散模型，通过像素级边缘引导强制生成实例严格遵循布局约束，实现即插即用的增强。

【实验结果 / Results】
在三个基线模型（CC-Diff、DiffusionInst、LayoutDiffusion）上的广泛实验验证了RSGen的有效性。以CC-Diff在DOTA数据集上的定向目标检测为例，RSGen带来YOLOScore mAP50提升9.8、YOLOScore mAP50-95提升12.0，以及下游检测任务mAP提升1.6的显著性能增益。

【应用价值 / Applications】
RSGen可应用于遥感领域的合成数据增强，缓解标注数据稀缺问题，提升目标检测等下游任务的性能。其即插即用的特性使其能够无缝集成到现有L2I生成流程中，为城市规划、环境监测、农业管理等需要精确布局控制的遥感应用提供高质量的图像生成解决方案。
