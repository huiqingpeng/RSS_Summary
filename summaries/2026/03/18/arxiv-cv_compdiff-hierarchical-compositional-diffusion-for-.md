---
title: "CompDiff: Hierarchical Compositional Diffusion for Fair and Zero-Shot Intersectional Medical Image Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16551"
published: "2026-03-18"
summarized: "2026-03-18T18:14:50.907936"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了CompDiff，一种层次化组合扩散框架，用于解决医学图像生成中的"不平衡生成器问题"——即生成模型在数据不平衡情况下对稀有子群体和未见过的交叉人口组合产生质量较差的图像。该框架通过分层条件网络（HCN）分解人口统计条件，实现参数共享和组合泛化。在MIMIC-CXR胸部X光和FairGenMed眼底图像数据集上，CompDiff在图像质量（FID 64.3 vs 75.1）、子群体公平性（ES-FID）和零样本交叉泛化（提升达21%）方面均优于现有方法，且生成的数据能有效提升下游分类器的AUROC并减少人口统计偏差。

【方法概述 / Method】

CompDiff的核心是层次化条件网络（Hierarchical Conditioner Network, HCN），该网络将人口统计属性（如种族、性别、年龄等）进行结构化分解，生成独立的人口统计标记（demographic token），并与CLIP嵌入拼接作为扩散模型的交叉注意力上下文。这种显式的因子化表示设计鼓励不同子群体间的参数共享，使模型能够通过组合已见属性来泛化到训练集中未出现的交叉人口组合（如"亚洲+女性+老年"）。

【实验结果 / Results】

在MIMIC-CXR和FairGenMed数据集上，CompDiff相比标准微调和FairDiffusion基线，FID分数从75.1降至64.3；在零样本交叉泛化任务中，对未见过的交叉人口组合FID提升高达21%；在子群体公平性指标ES-FID上表现更优。下游分类器实验显示，使用CompDiff生成数据训练的模型AUROC更高且人口统计偏差显著降低。

【应用价值 / Applications】

该研究为公平医学AI数据集增强提供了有效工具，可应用于需要平衡多人口统计属性分布的医学影像合成场景，如罕见疾病筛查、边缘化群体代表性不足时的数据扩充，以及保护隐私的敏感人口数据替代生成。其零样本组合泛化能力使其能灵活应对训练数据中缺失的复杂交叉子群体，对推动医疗AI的公平性和普适性具有重要实践意义。
