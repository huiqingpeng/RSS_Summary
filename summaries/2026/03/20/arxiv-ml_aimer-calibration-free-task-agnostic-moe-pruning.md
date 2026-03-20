---
title: "AIMER: Calibration-Free Task-Agnostic MoE Pruning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18492"
published: "2026-03-20"
summarized: "2026-03-20T12:12:23.474821"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了AIMER（Absolute mean over root mean square Importance for Expert Ranking），一种无需校准数据的专家剪枝方法，用于解决混合专家（MoE）语言模型部署中的内存开销问题。现有任务无关剪枝方法依赖校准集估计专家重要性，导致剪枝结果对校准集敏感且预处理成本高。AIMER通过简单的统计指标实现了清晰的层内分数分离和专家分层，在7B到30B规模的MoE模型上，以仅0.22-1.27秒的评分时间达到或超越现有基于校准的SOTA方法。

【方法概述 / Method】
AIMER采用绝对均值除以均方根（|mean|/RMS）作为专家重要性评分准则，直接从专家权重计算重要性分数，无需任何输入数据或前向传播。该方法利用该统计量在层内产生明显的分数分布差异，从而有效区分重要专家与可剪枝专家。

【实验结果 / Results】
在16个基准测试上，AIMER在25%和50%剪枝比例下均展现出与校准依赖基线相当或更优的整体性能；专家评分速度极快，仅需0.22-1.27秒，显著降低了预处理开销；实验覆盖7B至30B参数规模的MoE语言模型，验证了方法的广泛适用性。

【应用价值 / Applications】
AIMER适用于需要快速部署MoE模型的场景，如边缘设备推理、动态模型压缩和云服务等，消除了对校准数据集的依赖和繁琐的预处理流程。该方法特别有利于模型即服务（MaaS）提供商和需要频繁调整模型规模的实际生产环境，可大幅降低部署成本并提高灵活性。
