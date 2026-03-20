---
title: "Towards more holistic interpretability: A lightweight disentangled Concept Bottleneck Model"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.15770"
published: "2026-03-20"
summarized: "2026-03-20T14:17:21.251542"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了轻量级解耦概念瓶颈模型（LDCBM），通过引入滤波器分组损失和联合概念监督机制，自动将视觉特征分组为语义有意义的组件，无需区域标注。实验表明，LDCBM在三个多样化数据集上实现了更高的概念准确率和类别准确率，同时参数数量和FLOPs仅比标准CBM增加不到5%，在可解释性和分类性能上均优于现有CBM方法。

【方法概述 / Method】
LDCBM采用自动视觉特征分组策略，通过滤波器分组损失（filter grouping loss）和联合概念监督（joint concept supervision）来改善视觉模式与概念之间的对齐。该方法无需昂贵的区域级标注，即可将概念扎根于视觉证据，实现更透明和鲁棒的决策过程。

【实验结果 / Results】
在三个多样化数据集上的实验表明，LDCBM在概念准确率和类别准确率方面均超越先前CBM方法；复杂度分析显示其参数量和FLOPs较标准CBM增幅低于5%。背景掩码干预实验进一步验证了模型抑制无关图像区域的强大能力，证实了视觉-概念映射的高精度。

【应用价值 / Applications】
LDCBM适用于需要高可解释性和可控性的视觉识别场景，如医疗影像诊断、自动驾驶感知系统和安全关键型决策支持系统。其轻量级设计使其易于部署于资源受限环境，同时通过将概念与视觉证据对齐，增强了可解释AI的可靠性，支持人类对模型决策的信任与审查。
