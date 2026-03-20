---
title: "A Multicenter Benchmark of Multiple Instance Learning Models for Lymphoma Subtyping from HE-stained Whole Slide Images"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.14640"
published: "2026-03-20"
summarized: "2026-03-20T16:16:21.773073"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究首次建立了多中心淋巴瘤亚型分类基准，涵盖四种常见淋巴瘤亚型及健康对照组织。研究系统评估了五种公开病理基础模型（H-optimus-1、H0-mini、Virchow2、UNI2、Titan）结合两种多实例学习聚合器（AB-MIL和TransMIL）在三种放大倍数（10x、20x、40x）下的性能。结果表明，在分布内测试集上模型多类平衡准确率超过80%，但分布外测试集性能显著下降至约60%，揭示了泛化挑战。

【方法概述 / Method】
研究采用多实例学习（MIL）框架，将全切片图像（WSI）分割为多个图像块（patches），使用预训练病理基础模型提取特征，再通过注意力机制（AB-MIL）或Transformer架构（TransMIL）聚合实例级特征进行全局分类。实验设计包含三种放大倍数（10x、20x、40x）的系统对比，以及跨中心的数据划分以评估模型泛化能力。

【实验结果 / Results】
在分布内测试集上，所有模型配置均取得超过80%的多类平衡准确率，不同基础模型和聚合方法性能相近；40x分辨率足以达到最佳性能，更高分辨率或跨倍数聚合未带来额外增益。然而，在分布外测试集上，模型性能大幅降至约60%，表明跨中心泛化仍是重大挑战。

【应用价值 / Applications】
该研究为淋巴瘤病理诊断提供了首个多中心基准，证明了深度学习从常规HE染色切片辅助亚型分类的可行性，有望减少对传统免疫组化、流式细胞术等昂贵检测的依赖，加速诊断流程。研究团队还开源了自动化基准测试流程，为未来更大规模、覆盖更多罕见亚型的多中心研究奠定基础。
