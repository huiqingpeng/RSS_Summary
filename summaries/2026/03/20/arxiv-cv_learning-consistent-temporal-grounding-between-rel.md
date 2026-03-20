---
title: "Learning Consistent Temporal Grounding between Related Tasks in Sports Coaching"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18453"
published: "2026-03-20"
summarized: "2026-03-20T15:09:08.389641"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对体育教练任务中视频大语言模型（Video-LLMs）关注无关帧的问题，提出了一种无需额外标注的自一致性训练方法。核心观察是：相关任务（如生成与验证）必须关注相同的视频帧，通过约束这些紧密相关任务的视觉注意力图一致性，显著提升了时间定位精度。在VidDiffBench基准上的三个体育教练任务（Exact、FitnessQA、ExpertAF）中，该方法相比监督微调分别取得+3.0%、+14.1%的准确率和+0.9的BERTScore提升，甚至超越了闭源模型。

【方法概述 / Method】
作者设计了一种自一致性目标函数，强制紧密相关任务（如答案生成与答案验证）的视觉注意力图在关键帧上保持一致。该方法无需帧级人工标注或其他模型的不可靠监督，仅利用任务间的内在关联性约束注意力分配，从而改善模型对视频关键时间点的定位能力。

【实验结果 / Results】
在VidDiffBench基准（含真实关键帧标注）上的验证表明，注意力错配是性能瓶颈；应用自一致性训练后，Exact任务准确率提升3.0%，FitnessQA提升14.1%，ExpertAF的BERTScore提升0.9。这些增益均显著优于监督微调基线，且模型表现超过闭源商业模型。

【应用价值 / Applications】
该研究可直接应用于智能体育教练系统、动作分析与反馈生成等场景，帮助AI精准定位视频中的关键技术动作时刻。方法无需昂贵标注即可提升时间 grounding 精度，为其他需要细粒度时间理解的多模态任务（如教学视频分析、医疗动作评估）提供了可迁移的技术框架。
