---
title: "Confidence Calibration under Ambiguous Ground Truth"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22879"
published: "2026-03-25"
summarized: "2026-03-26T07:17:46.108955"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文揭示了传统置信度校准方法在存在标注歧义时的结构性缺陷：基于多数投票标签的后验校准器虽在传统评估中表现良好，却严重低估了真实的标注者不确定性。研究证明了温度缩放（Temperature Scaling）会系统性偏向低估标注者不确定性的温度参数，且真实标签的错校准程度随标注熵单调递增。为此，作者提出了一系列无需重新训练模型的歧义感知后验校准方法，在四个真实或合成多标注者数据集上显著改善了校准质量。

【方法概述 / Method】
作者开发了三种渐进式降低标注数据需求的歧义感知校准方法：Dirichlet-Soft 直接利用完整标注者分布进行优化；Monte Carlo Temperature Scaling（MCTS S=1）仅需每个样本单一标注即可匹配完整分布的校准效果；Label-Smooth Temperature Scaling（LS-TS）则完全无需标注者数据，通过模型自身置信度构建数据驱动的伪软标签。所有方法均针对完整标签分布优化严格评分规则（proper scoring rules）。

【实验结果 / Results】
在 CIFAR-10H、ChaosNLI 及临床合成标注数据集（ISIC 2019、DermaMNIST）上的实验表明：Dirichlet-Soft 相比传统温度缩放将真实标签期望校准误差（ECE）降低 55-87%；MCTS S=1 在所有基准上达到与完整分布校准相当的性能，证明预聚合标签分布非必需；LS-TS 在无任何标注者数据条件下仍可将 ECE 降低 9-77%。

【应用价值 / Applications】
该研究对高 stakes 决策场景具有重要价值，如医学诊断（皮肤病、病理切片分类）、自然语言推理等存在固有标注歧义的领域。方法使模型能够准确反映真实的人类标注不确定性而非虚假自信，提升人机协作系统的可靠性与安全性，且后验校准特性使其可无缝部署于现有训练好的模型。
