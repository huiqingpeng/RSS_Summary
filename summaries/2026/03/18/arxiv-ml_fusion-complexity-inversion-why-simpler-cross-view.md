---
title: "Fusion Complexity Inversion: Why Simpler Cross View Modules Outperform SSMs and Cross View Attention Transformers for Pasture Biomass Regression"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.07819"
published: "2026-03-18"
summarized: "2026-03-18T17:14:52.393250"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究系统评估了视觉基础模型在农业回归任务中的适应性，在CSIRO牧场生物量基准数据集上测试了17种配置。研究发现了一个反直觉的"融合复杂度反转"原则：在稀缺的农业数据上，简单的两层门控深度卷积（R² = 0.903）优于跨视图注意力Transformer（0.833）、双向SSM（0.819）和完整Mamba（0.793）。研究还发现主干网络预训练规模单调主导所有架构选择，仅训练元数据会产生R² ≈ 0.829的通用上限。

【方法概述 / Method】
研究采用CSIRO牧场生物量基准数据集（357张双视图图像，含五种生物量目标的实验室验证真值），系统比较了四种主干网络（EfficientNet-B3至DINOv3-ViT-L）、五种跨视图融合机制及4×2元数据因子设计。融合机制涵盖从简单卷积到复杂的状态空间模型（SSM）和注意力Transformer，形成完整的消融实验框架。

【实验结果 / Results】
融合复杂度反转现象显著：最简单的门控深度卷积融合模块取得最高R²（0.903），而复杂的全局建模方法（SSM、Transformer）表现反而更差，甚至低于无融合基线。DINOv2升级到DINOv3单独带来+5.0 R²点的提升，证明主干预训练质量至关重要。元数据单独训练即可达到R² ~ 0.829，将8.4点的融合性能差距压缩至0.1点。

【应用价值 / Applications】
研究为稀疏农业基准测试提供了可操作的指导原则：优先提升主干网络质量而非融合复杂度、选用局部模块而非全局替代方案、排除推理时不可用的特征。这些发现对可持续畜牧业管理中的牧场生物量精准估算具有直接应用价值，可帮助研究者在数据受限的农业场景中做出更高效的模型设计决策。
