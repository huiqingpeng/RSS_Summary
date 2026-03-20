---
title: "MultihopSpatial: Multi-hop Compositional Spatial Reasoning Benchmark for Vision-Language Model"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18892"
published: "2026-03-20"
summarized: "2026-03-20T15:17:20.730179"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MultihopSpatial，首个针对多跳组合空间推理的综合性基准测试，用于评估视觉语言模型（VLMs）在复杂空间关系推理中的能力。该基准包含1至3跳的复杂查询，涵盖多样化空间视角，并引入Acc@50IoU指标同时评估推理能力与精确视觉定位。此外，作者构建了大规模训练语料库MultihopSpatial-Train，并通过强化学习后训练显著提升了模型的空间推理能力及下游具身操作性能。

【方法概述 / Method】
本研究设计了一套系统化的数据构建流程，生成包含多跳组合空间关系的查询-图像-答案三元组，覆盖相对位置、视角变换等复杂场景。提出Acc@50IoU评估指标，要求模型不仅选择正确答案，还需预测IoU≥50%的精确边界框，以联合评估推理与定位能力。采用强化学习对VLM进行后训练，利用MultihopSpatial-Train语料库增强模型的空间智能。

【实验结果 / Results】
对37个最先进VLMs的广泛评估揭示了八个关键发现，表明组合空间推理仍是重大挑战：现有模型在多跳查询上的性能显著下降，且推理与定位能力存在明显差距。强化学习后训练在MultihopSpatial-Train上使模型在本基准及下游具身操作任务中均取得性能提升，验证了该训练语料的有效性。

【应用价值 / Applications】
该研究直接服务于视觉语言-动作（VLA）智能体的实际部署，为机器人导航、物体操作等物理环境交互任务提供可靠的空间推理能力评估与改进方案。所提出的基准和训练资源可推动VLMs在自动驾驶、智能家居、工业自动化等需要精确空间理解的应用场景中的发展，缩小模拟环境与真实世界之间的性能差距。
