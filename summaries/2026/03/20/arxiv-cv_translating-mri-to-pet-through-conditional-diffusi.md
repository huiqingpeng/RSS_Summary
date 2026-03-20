---
title: "Translating MRI to PET through Conditional Diffusion Models with Enhanced Pathology Awareness"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18896"
published: "2026-03-20"
summarized: "2026-03-20T15:17:29.575325"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为PASTA的新型图像翻译框架，基于条件扩散模型实现从MRI到PET的跨模态医学图像合成，特别增强了病理感知能力。该方法通过双分支交互架构和多模态条件融合，在保持结构信息的同时有效保留病理细节，并引入循环交换一致性和体素生成策略以提升3D PET图像质量。实验表明，合成PET在阿尔茨海默病诊断中较MRI提升4%性能，接近真实PET水平。

【方法概述 / Method】
PASTA采用条件扩散模型作为基础架构，设计了高度交互的双分支网络结构实现多模态条件信息融合；通过引入循环交换一致性损失（cycle exchange consistency）约束生成过程的一致性，并结合体素生成策略实现高质量三维PET图像合成。

【实验结果 / Results】
定性与定量评估均显示合成PET图像具有高质量和良好的病理感知特性；在阿尔茨海默病诊断任务中，合成PET相比原始MRI的诊断准确率提升4%，性能几乎与真实PET相当；该方法在多项指标上超越现有最优方法。

【应用价值 / Applications】
该研究为神经退行性疾病（如阿尔茨海默病）的诊断提供了一种低成本、无辐射的替代方案，可在临床实践中减少对昂贵且有创PET扫描的依赖；合成PET图像可用于辅助早期疾病筛查、治疗监测及多中心研究中的数据标准化。
