---
title: "Beyond Attention Magnitude: Leveraging Inter-layer Rank Consistency for Efficient Vision-Language-Action Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24941"
published: "2026-03-27"
summarized: "2026-03-28T07:18:50.314398"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对视觉-语言-动作（VLA）模型因处理密集视觉token而导致推理延迟高的问题，挑战了传统基于注意力幅度的静态token选择方法，发现高注意力token具有任务依赖性甚至可能损害策略性能。为此，作者提出TIES（Tau-guided Inter-layer Efficient Selection）动态框架，通过利用层间token排名一致性自适应地平衡注意力幅度与排名一致性，实现无需额外训练的鲁棒token选择。在CogACT + SIMPLER基准上，TIES在减少78% token使用量的同时将平均成功率提升6%，并在多种解码器和基准上展现出强泛化能力。

【方法概述 / Method】
TIES的核心思想是通过分析相邻层间token排名的一致性（即哪些token在不同层中保持相似的相对重要性排序）来动态指导token选择，而非单纯依赖单层的注意力幅度。该方法引入"Tau"作为调节参数，自适应地融合注意力幅度信息和跨层排名一致性信息，从而识别出对任务真正重要的token子集。整个框架无需重新训练模型，可直接应用于预训练的VLA模型。

【实验结果 / Results】
在CogACT + SIMPLER机器人操作基准测试中，TIES实现了78%的token压缩率，同时将平均成功率提升6%，显著优于基于注意力幅度的静态基线方法。此外，TIES展现出强大的跨架构泛化能力，可有效迁移至不同的VLA解码器结构，并在多个基准测试上保持性能优势，证明了其作为即插即用模块的实用价值。

【应用价值 / Applications】
该研究为部署高效的VLA模型提供了关键技术支持，特别适用于对实时性要求高的机器人操控场景，如工业自动化装配、服务机器人交互等。TIES的免训练特性使其能够快速集成到现有的机器人学习系统中，大幅降低推理计算成本的同时提升策略可靠性，有助于推动VLA模型在资源受限的嵌入式平台上的实际部署。
