---
title: "Exploring the Underwater World Segmentation without Extra Training"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.07923"
published: "2026-03-18"
summarized: "2026-03-18T18:28:22.281703"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了首个大规模细粒度水下分割数据集AquaOV255（包含255个类别、超过2万张图像），并建立了首个水下开放词汇分割基准UOVSBench。作者设计了无需额外水下训练的Earth2Ocean框架，通过几何引导视觉掩码生成器（GMG）和类别-视觉语义对齐模块（CSA），将陆地视觉-语言模型迁移至水下领域，在UOVSBench上实现了显著的性能提升。

【方法概述 / Method】
Earth2Ocean框架包含两个核心组件：GMG利用自相似性几何先验细化视觉特征以增强局部结构感知；CSA通过多模态大语言模型推理和场景感知模板构建来增强文本嵌入，实现类别与视觉特征的语义对齐。整个框架无需任何水下数据训练即可完成迁移。

【实验结果 / Results】
在UOVSBench基准上的大量实验表明，Earth2Ocean在平均性能上实现了显著提升，同时保持了高效的推理速度。该框架有效克服了陆地模型在水下场景中的域差距问题，在开放词汇分割任务中展现出优越的泛化能力。

【应用价值 / Applications】
该研究可直接应用于海洋生物多样性监测、海洋生态系统评估和水下机器人视觉感知等领域。Earth2Ocean的训练自由特性使其能够快速部署到新的水下环境中，为海洋科学研究和海洋资源管理提供高效、低成本的智能分析工具。
