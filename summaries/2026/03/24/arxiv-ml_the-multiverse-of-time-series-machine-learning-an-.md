---
title: "The Multiverse of Time Series Machine Learning: an Archive for Multivariate Time Series Classification"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20352"
published: "2026-03-24"
summarized: "2026-03-25T07:08:25.622879"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文对2018年发布的UEA多元时间序列分类数据集进行了重大扩展，从30个数据集增至133个分类问题，并额外提供14个预处理后的缺失值或非等长序列数据集，总计147个数据集。研究团队将该档案重新命名为"Multiverse archive"，以反映其涵盖领域的多样性，并推出了用于初步探索的核心子集MV-core。论文还提供了详细的基线评估和可复现的aeon/scikit-learn兼容框架，为时间序列机器学习研究建立了新的性能基准。

【方法概述 / Method】
本研究通过整合多个来源的数据集（包括其他独立集合和单独发布的数据集），构建了一个统一的标准化存储库。团队开发了与aeon和scikit-learn兼容的编程框架，支持实验的可复现性，并建立了交互式结果探索界面。此外，设计了分层评估策略，推荐MV-core子集以降低全档案实验的计算成本。

【实验结果 / Results】
论文对多种已建立的和最新的时间序列分类算法进行了全面的基线评估，建立了未来研究可参考的性能基准。评估涵盖了扩展后的全档案以及推荐的MV-core子集，为研究者提供了算法选择的实证依据。详细的实验记录和结果通过专用仓库公开发布，便于社区追踪和比较。

【应用价值 / Applications】
Multiverse档案为时间序列机器学习领域提供了标准化的基准测试平台，支持分类、聚类和外推回归等多种任务的算法开发与评估。该资源特别适用于需要处理多元时间序列数据的领域，如医疗健康监测、工业设备故障诊断、金融预测和人机交互等。统一的框架和交互界面降低了研究门槛，促进了算法公平比较和领域间的知识迁移。
