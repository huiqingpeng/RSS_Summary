---
title: "FlowMotion: Training-Free Flow Guidance for Video Motion Transfer"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.06289"
published: "2026-03-18"
summarized: "2026-03-18T19:03:02.866929"
ai_provider: "openai"
---

【论文摘要 / Abstract】
FlowMotion 提出了一种无需训练的视频运动迁移框架，通过直接利用基于流的文本到视频（T2V）模型的预测输出来实现高效灵活的运动迁移。核心洞见在于早期潜在预测天然编码了丰富的时间信息，据此设计了流引导机制来提取运动表征以对齐源视频与生成视频的运动模式，并引入速度正则化策略稳定优化过程。该方法在计算效率和资源消耗上显著优于现有方案，同时保持了具有竞争力的性能。

【方法概述 / Method】
FlowMotion 基于流式 T2V 模型的早期潜在预测提取运动表征，构建流引导（flow guidance）机制来实现源视频与目标视频之间的运动模式对齐；同时引入速度正则化（velocity regularization）策略优化运动演化的平滑性和稳定性。整个框架完全在模型预测层面操作，无需额外训练或依赖中间输出的复杂计算。

【实验结果 / Results】
与现有无需训练的最先进方法相比，FlowMotion 在时间和资源效率上实现显著提升，同时生成质量具有竞争力；速度正则化有效稳定了优化过程并确保了运动的平滑演进。实验验证了流引导机制能够准确捕获和迁移复杂的运动模式。

【应用价值 / Applications】
FlowMotion 可广泛应用于视频内容创作、影视特效制作、虚拟现实及游戏动画等领域，使创作者能够快速将现有视频的运动风格迁移到新场景中；其训练无关特性大幅降低了部署门槛和计算成本，适用于实时或资源受限的创意生产环境。
