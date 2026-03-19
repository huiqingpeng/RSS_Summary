---
title: "DiffVP: Differential Visual Semantic Prompting for LLM-Based CT Report Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17718"
published: "2026-03-19"
summarized: "2026-03-19T15:16:50.273224"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为 DiffVP（Differential Visual Prompting）的新方法，用于基于大语言模型（LLM）的 CT 报告生成。该方法受放射学认知减法启发，通过显式建模扫描图像与参考图像之间的高层语义差异，而非仅依赖绝对视觉特征，来生成诊断报告。DiffVP 在多个大规模基准数据集上显著优于现有方法，BLEU 分数平均提升 4.36-10.98，并在 RadGenome-ChestCT 上取得 0.421 的 F1 分数，展现出优异的临床有效性。

【方法概述 / Method】
DiffVP 包含两个核心组件：层次化差异提取器（hierarchical difference extractor）和差异到提示生成器（difference-to-prompt generator）。前者通过全局和局部两个尺度捕获扫描图像与参考图像之间的语义差异，并将其映射到共享潜在空间；后者将这些差异信号转换为可学习的视觉前缀 token，作为 LLM 的条件输入，从而隐式抑制不变解剖结构、放大诊断相关视觉证据。

【实验结果 / Results】
在 two large-scale benchmarks 上，DiffVP 较之前方法平均 BLEU-1-4 分别提升 +10.98 和 +4.36；在 RadGenome-ChestCT 数据集上，F1 分数达到 0.421，验证了其在临床指标上的有效性。实验结果表明，该方法无需显式病灶定位即可实现准确的报告生成。

【应用价值 / Applications】
DiffVP 可广泛应用于医院放射科的自动化 CT 报告生成系统，辅助放射科医生提高诊断效率和一致性，减少漏诊风险。其"差异驱动"的设计理念还可迁移至其他医学影像分析任务（如 MRI、X-ray 报告生成），为医学影像-语言大模型的研发提供新的技术范式。
