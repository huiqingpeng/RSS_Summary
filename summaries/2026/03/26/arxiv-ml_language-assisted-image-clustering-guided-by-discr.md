---
title: "Language-Assisted Image Clustering Guided by Discriminative Relational Signals and Adaptive Semantic Centers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24275"
published: "2026-03-26"
summarized: "2026-03-27T07:22:43.825519"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对语言辅助图像聚类（LAIC）任务中存在的两个关键问题——文本特征高度相似导致类间判别性不足、以及聚类步骤受限于预构建的图像-文本对齐——提出了一个新的LAIC框架。该框架通过利用跨模态关系生成更具判别性的自监督信号，并基于提示学习学习类别级连续语义中心以生成最终聚类结果。在八个基准数据集上的实验表明，该方法相比最先进方法平均提升2.6%，且学习到的语义中心具有较强的可解释性。

【方法概述 / Method】
本文提出的LAIC框架包含两个互补组件：一是利用跨模态关系（cross-modal relations）生成更具判别性的自监督信号，该设计与大多数视觉-语言模型（VLMs）的训练机制兼容；二是通过提示学习（prompt learning）学习类别级连续语义中心，从而灵活地生成最终聚类分配，突破了预构建图像-文本对齐的限制。

【实验结果 / Results】
在八个基准数据集上的大量实验表明，该方法相比现有最先进方法实现了平均2.6%的性能提升；此外，学习得到的语义中心展现出较强的可解释性，验证了方法在语义理解方面的优势。

【应用价值 / Applications】
该研究可应用于大规模图像自动组织与检索、视觉内容分析与标注等场景，特别是在需要结合文本语义理解进行细粒度图像分类的任务中具有重要价值；所学习的可解释语义中心也有助于提升模型决策的透明度和用户信任度。
