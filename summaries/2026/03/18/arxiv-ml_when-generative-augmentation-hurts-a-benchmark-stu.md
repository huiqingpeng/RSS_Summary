---
title: "When Generative Augmentation Hurts: A Benchmark Study of GAN and Diffusion Models for Bias Correction in AI Classification Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16134"
published: "2026-03-18"
summarized: "2026-03-18T16:10:49.172616"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究系统比较了生成模型在数据稀缺场景下用于类别不平衡修正的效果，发现FastGAN在极少样本条件下不仅无法改善分类性能，反而会显著加剧分类器的偏见（偏见差距增加20.7%）。相比之下，基于LoRA微调的Stable Diffusion 1.5表现最优，在宏观F1分数上达到0.9125，并将偏见差距降低13.1%。研究还识别出一个关键样本量边界（20-50张/类），低于该阈值时GAN增强会产生有害效应。

【方法概述 / Method】
研究者在Oxford-IIIT Pet Dataset上构建了8个人工欠采样犬种的细粒度分类任务，对比三种增强策略：传统数据变换、FastGAN生成增强，以及LoRA微调的Stable Diffusion 1.5。实验采用三随机种子设计，通过t-SNE嵌入分析探究生成样本的分布特性，全部实验在消费级GPU（6-8GB显存）上完成。

【实验结果 / Results】
FastGAN在极少样本场景下表现出严重的模式崩溃，其生成样本在特征空间中形成与真实分布隔离的紧密聚类，导致分类器偏见显著上升（Cohen's d = +5.03, p = 0.013）。Stable Diffusion+LoRA组合取得最佳综合性能，宏观F1达0.9125±0.0047。研究初步确定20-50张/类为GAN增强的有效阈值边界。

【应用价值 / Applications】
该研究为实际AI系统中数据增强策略的选择提供了重要决策依据，尤其适用于野生动物保护、医学影像等细粒度识别且样本采集困难的领域。研究强调在资源受限场景下应优先采用扩散模型而非GAN进行数据增强，并为后续建立跨域的样本量边界标准奠定了基础。消费级硬件可复现的设计也降低了相关研究的准入门槛。
