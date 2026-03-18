---
title: "Transformers can do Bayesian Clustering"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.24318"
published: "2026-03-18"
summarized: "2026-03-18T16:20:19.974899"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Cluster-PFN，一种基于Transformer的贝叶斯聚类方法，通过扩展Prior-Data Fitted Networks (PFNs)实现无监督学习。该方法在合成的高斯混合模型数据上训练，能够同时估计聚类数量和聚类分配的后验分布。实验表明，Cluster-PFN在聚类数量估计上优于AIC、BIC等传统模型选择方法，在聚类质量上与变分推断相当但速度提升数个数量级，且能有效处理含缺失数据的复杂场景。

【方法概述 / Method】
Cluster-PFN采用Transformer架构，通过在高斯混合模型(GMM)先验生成的合成数据集上进行元学习(meta-learning)，直接逼近贝叶斯后验推断。模型将聚类问题转化为序列预测任务，利用自注意力机制捕捉数据点间的复杂依赖关系，无需迭代优化即可一次性输出聚类数量和分配的概率分布。

【实验结果 / Results】
在合成数据上，Cluster-PFN的聚类数量估计准确率显著超越AIC、BIC和变分推断(VI)等基线方法；在运行效率上比VI快数个数量级。在高缺失率的真实基因组数据集上，该方法优于基于插补的基线方法，证明了其对缺失数据不确定性的有效建模能力。

【应用价值 / Applications】
Cluster-PFN适用于大规模数据的快速贝叶斯聚类分析，特别是在计算资源受限或需要实时推断的场景。其在高缺失率基因组数据上的优异表现，使其成为生物信息学、医疗数据分析等领域的有力工具，为处理含不确定性的真实世界数据提供了可扩展的解决方案。
