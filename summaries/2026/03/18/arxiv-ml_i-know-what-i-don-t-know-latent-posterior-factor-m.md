---
title: "I Know What I Don't Know: Latent Posterior Factor Models for Multi-Evidence Probabilistic Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15670"
published: "2026-03-18"
summarized: "2026-03-18T16:06:12.545647"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了Latent Posterior Factors (LPF)框架，将变分自编码器(VAE)的潜在后验分布转化为Sum-Product Network (SPN)推理的软似然因子，实现了对非结构化证据的可追踪概率推理，同时保持校准的不确定性估计。作者实例化了两种架构——LPF-SPN（结构化因子推理）和LPF-Learned（端到端学习聚合），在8个领域（7个合成数据集和FEVER基准）的实验中，LPF-SPN达到了最高97.8%的准确率和仅1.4%的期望校准误差(ECE)，显著优于证据深度学习、大语言模型和图神经网络基线方法。

【方法概述 / Method】

LPF框架的核心创新在于将VAE编码器输出的潜在后验分布（均值μ和方差σ²）解释为对证据可信度的软概率因子，替代传统SPN中需要人工设计的离散谓词。该方法通过重参数化技巧实现端到端训练，使神经网络的不确定性表示与结构化概率推理相结合，形成兼具可解释性和可扩展性的混合架构。

【实验结果 / Results】

在跨15个随机种子的系统评估中，LPF-SPN展现出卓越的准确性和校准性能，ECE仅为1.4%，大幅优于证据深度学习(EDL)、BERT、R-GCN等基线。特别是在FEVER事实验证基准上，该方法在处理多证据冲突场景时表现出鲁棒的不确定性量化能力，而大型语言模型在此类结构化推理任务中校准误差显著更高。

【应用价值 / Applications】

该研究适用于需要整合多源噪声证据并进行可靠不确定性量化的决策场景，如税务合规评估、医疗诊断和金融风控等领域。LPF框架为高风险决策系统提供了一种可扩展的替代方案，既能处理非结构化数据（如文本报告），又能输出经过良好校准的概率预测，弥补了纯神经网络方法不确定性估计不足和纯逻辑方法扩展性受限的双重缺陷。
