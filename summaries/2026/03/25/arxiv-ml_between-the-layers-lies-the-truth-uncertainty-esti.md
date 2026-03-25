---
title: "Between the Layers Lies the Truth: Uncertainty Estimation in LLMs Using Intra-Layer Local Information Scores"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22299"
published: "2026-03-25"
summarized: "2026-03-26T07:08:36.704287"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种轻量级的不确定性估计（UE）方法，通过分析大语言模型内部表示的跨层一致性模式来识别模型是否"自信地犯错"。该方法仅需单次前向传播，在分布内场景下性能匹配传统探测方法，在跨数据集迁移和4-bit量化场景下显著优于探测方法，为LLM可靠性评估提供了紧凑且可迁移的解决方案。

【方法概述 / Method】
作者提出基于"层内局部信息分数"（Intra-Layer Local Information Scores）的UE方法，通过量化不同网络层之间表示的一致性模式来估计预测不确定性。该方法从模型内部激活中提取紧凑的逐实例特征，避免了高维表示探测的计算开销和迁移困难。

【实验结果 / Results】
在三个模型上的实验显示：分布内任务中，该方法与探测方法的AUPRC差异不超过-1.8个百分点，Brier分数差异不超过+4.9点；跨数据集迁移时，该方法实现最高+2.86 AUPRC和+21.02 Brier分数的提升；4-bit权重量化下，平均提升+1.94 AUPRC和+5.33 Brier分数。层间交互分析还揭示了不同模型编码不确定性的机制差异。

【应用价值 / Applications】
该方法适用于需要高效、可靠不确定性量化的LLM部署场景，如高风险决策支持系统、模型输出可信度排序、以及资源受限环境（如量化模型）中的安全监控。其跨模型迁移能力使其特别适合多模型集成和模型即服务（MaaS）平台的质量控制。
