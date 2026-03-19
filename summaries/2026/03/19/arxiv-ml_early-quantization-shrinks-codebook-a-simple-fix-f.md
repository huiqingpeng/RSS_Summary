---
title: "Early Quantization Shrinks Codebook: A Simple Fix for Diversity-Preserving Tokenization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17052"
published: "2026-03-19"
summarized: "2026-03-19T12:07:04.407801"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究系统性地调查了向量量化（Vector Quantization）中的表征坍塌问题，发现离散码本标记（tokens）和连续潜在嵌入（embeddings）均存在坍塌现象。研究揭示了随机初始化和有限的编码器容量是导致标记坍塌和嵌入坍塌的主要原因，并提出了针对性的缓解方案。这是首个全面研究向量量化中表征坍塌问题的综合性工作。

【方法概述 / Method】
论文采用合成数据集与真实数据集相结合的实证分析方法，对向量量化中的两类坍塌（标记坍塌与嵌入坍塌）进行系统诊断，识别各类坍塌的严重程度与触发条件。基于分析结果，作者提出了针对每种坍塌类型的潜在解决方案。

【实验结果 / Results】
研究发现随机初始化会导致码本标记坍塌（codebook token collapse），而编码器容量受限则引发嵌入坍塌（embedding collapse）。通过早期量化（Early Quantization）等策略可有效缓解坍塌问题，从而保持码本的多样性。具体性能指标因论文未提供详细实验数据而无法量化总结。

【应用价值 / Applications】
该研究对大规模语言模型、扩散模型及其他生成模型中的数据表征token化具有重要指导意义，可帮助提升向量量化模块的训练稳定性和生成质量。提出的多样性保持token化方案可广泛应用于需要离散表征学习的生成式AI系统中，改善模型的表达能力和生成多样性。
