---
title: "Simple Projection-Free Algorithm for Contextual Recommendation with Logarithmic Regret and Robustness"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20826"
published: "2026-03-24"
summarized: "2026-03-25T07:14:48.688353"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对上下文推荐问题（contextual recommendation），提出了一种比现有在线牛顿步（ONS）方法更高效的简单算法，同时保持了 O(d log T) 的对数遗憾界。核心思想是利用上下文推荐固有的"非适定性"（improperness），设计出类似二阶感知机的更新规则，从而消除了 ONS 中计算代价高昂的 Mahalanobis 投影步骤。更重要的是，该算法对次优动作反馈具有鲁棒性，而此前 ONS 方法需要运行多个不同学习率的 ONS 学习器才能实现类似扩展。该方法还可推广到一般 Hilbert 空间（如通过核化），此时消除 Mahalanobis 投影的收益更为显著。

【方法概述 / Method】

作者提出了一种基于二阶感知机思想的投影自由算法，通过利用上下文推荐中允许预测动作与观察动作不同的"非适定性"特性，避免了 ONS 所需的 Mahalanobis 距离投影计算。该更新规则仅涉及简单的矩阵运算和向量乘法，计算复杂度显著降低，同时可自然扩展至核化的无限维特征空间。

【实验结果 / Results】

（注：摘要中未明确提及具体实验结果，但理论分析表明）该算法在保持 O(d log T) 遗憾界的同时，计算效率优于 ONS 方法；在存在次优动作反馈的鲁棒性扩展中，单一算法即可实现目标，而无需像先前方法那样维护多个 ONS 学习器；在 Hilbert 空间设置下，算法避免了无限维空间中的投影计算瓶颈。

【应用价值 / Applications】

该研究适用于大规模在线推荐系统，如新闻推荐、广告投放等需要实时决策的场景，可显著降低计算延迟和基础设施成本。其核化扩展使其能处理复杂的非线性特征交互，适用于具有丰富上下文信息的个性化推荐。算法的鲁棒性保证使其在实际部署中更能容忍噪声反馈，提升系统可靠性。
