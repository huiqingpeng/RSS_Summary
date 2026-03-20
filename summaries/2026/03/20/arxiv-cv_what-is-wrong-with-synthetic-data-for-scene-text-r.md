---
title: "What Is Wrong with Synthetic Data for Scene Text Recognition? A Strong Synthetic Engine with Diverse Simulations and Self-Evolution"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.06450"
published: "2026-03-20"
summarized: "2026-03-20T16:17:45.468288"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文系统分析了现有场景文本识别（STR）合成数据集的关键局限性，发现语料、字体和布局多样性不足导致与真实数据存在显著域差距。为此，作者提出UnionST合成引擎，生成覆盖复杂挑战样本的多样化文本数据，并构建大规模合成数据集UnionST-S。此外，作者还提出自进化学习（SEL）框架，仅用9%的真实数据标注即可达到竞争性能，使合成数据训练模型在特定场景下甚至超越真实数据训练效果。

【方法概述 / Method】

UnionST引擎通过扩展语料多样性、字体库和复杂布局模拟（如多方向、遮挡、形变等）来生成更具挑战性的合成样本；SEL框架采用迭代式自训练策略，利用模型预测筛选高置信度样本进行伪标签学习，逐步减少对真实标注的依赖。

【实验结果 / Results】

在UnionST-S上训练的模型相比现有主流合成数据集取得显著提升，在部分复杂场景下性能超过真实数据训练模型；结合SEL框架时，模型仅使用9%的真实数据标签即可达到与全量监督相当的性能，大幅降低标注成本。

【应用价值 / Applications】

该研究为场景文本识别领域提供了高质量合成数据生成方案，可缓解真实数据收集难、标注成本高的痛点，适用于文档分析、自动驾驶路牌识别、智能监控等实际场景；SEL框架的提出也为低资源条件下的模型训练提供了有效途径。
