---
title: "Benchmarking CNN-based Models against Transformer-based Models for Abdominal Multi-Organ Segmentation on the RATIC Dataset"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18616"
published: "2026-03-20"
summarized: "2026-03-20T15:13:07.121748"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究在包含206例来自全球23家机构的异质性腹部CT扫描RATIC数据集上，系统对比了三种混合Transformer架构（UNETR、SwinUNETR、UNETR++）与CNN基线模型SegResNet的多器官分割性能。实验结果表明，在相同预处理与训练条件下，基于CNN的SegResNet在所有器官上均取得最优整体性能，而UNETR++在Transformer模型中表现最佳，UNETR则展现出更快的收敛速度。该研究提示，对于中小规模异质性医学数据集，优化良好的CNN架构仍具显著竞争力。

【方法概述 / Method】
研究采用Dice相似系数（DSC）作为主要评估指标，在统一的预处理流程和训练配置下对四种模型进行公平比较。实验涵盖肝脏、脾脏、左肾、右肾和主动脉五个腹部器官的体积分割任务，所有模型均在RATIC数据集的五折交叉验证框架下进行评估。

【实验结果 / Results】
SegResNet在所有器官分割任务中均优于三种混合Transformer模型，取得最高整体DSC分数。UNETR++在Transformer类模型中表现最为接近CNN基线，而UNETR虽最终性能略逊，但训练迭代次数显著减少、收敛速度最快。这一发现挑战了Transformer在医学图像分割领域必然优于CNN的普遍假设。

【应用价值 / Applications】
该研究为临床实践中多器官分割模型的选择提供了重要参考，特别是在数据规模有限且来源异质的真实医疗场景中。研究结果提示医疗机构在部署计算机辅助诊断系统时，应优先考虑计算效率与数据适应性更优的CNN架构，而非盲目追随Transformer技术趋势，有助于降低开发成本并提升诊断系统的临床实用性。
