---
title: "One-for-All: A Lightweight Stabilized and Parameter-Efficient Pre-trained LLM for Time Series Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29756"
published: "2026-04-01"
summarized: "2026-04-02T07:19:59.825190"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了One-for-All，一种轻量级、稳定且参数高效的时间序列预测预训练大语言模型。该研究通过引入高斯秩稳定低秩适配器（rsLoRA）解决了预训练LLM在多变量时间序列分析中计算和内存需求过高的问题，实现了在冻结LLM上的参数高效微调。rsLoRA首次从数学上证明了低秩情况下的梯度稳定性，相比现有SOTA模型，训练参数量减少6.8-21倍，内存占用降低168-1,776倍（仅2.2MiB），同时在六个时间序列任务上保持了领先的准确率。

【方法概述 / Method】
One-for-All采用rsLoRA技术，在位置嵌入和输出层注入可训练的秩分解矩阵（秩为16），同时保持自注意力权重冻结。rsLoRA的核心创新在于引入数学上严格的秩稳定机制，通过高斯分布约束确保低秩适配时的梯度稳定性，这是以往参数高效微调（PEFT）方法所不具备的理论保证。

【实验结果 / Results】
在ETT、Weather、M3、M4等多个数据集的预测任务中，One-for-All在96-720步的多样化预测跨度上表现稳定。具体而言，该模型以MSE=0.33的预测精度匹敌TimesNet和GPT4TS，但参数效率分别提升5.5倍和21倍（MSE=5.50）；相比传统Transformer，参数量减少98.3%，实现了效率与精度的最优权衡。

【应用价值 / Applications】
One-for-All的极致轻量化特性（2.2MiB内存占用）使其能够部署于边缘计算设备，适用于医疗监测、金融预测和环境监控等实时性要求高、资源受限的场景。该框架在不牺牲预测精度的前提下，显著降低了部署门槛，为大规模预训练模型在物联网和移动设备上的实际应用开辟了可行路径。
