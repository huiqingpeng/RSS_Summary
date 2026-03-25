---
title: "FAAR: Format-Aware Adaptive Rounding for NVFP4"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22370"
published: "2026-03-25"
summarized: "2026-03-26T07:13:48.239589"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对NVFP4超低精度量化格式提出了一种格式感知自适应舍入方法FAAR，通过将NVFP4的非均匀数值网格显式纳入优化过程，利用损失梯度自适应调整舍入决策，有效逼近理论最优量化。配合提出的两阶段格式对齐（2FA）微调策略，该方法在Llama3-1B和Qwen3-1.7B模型上显著降低了困惑度，且仅需约4 GPU小时的训练开销，在多个零样本下游任务上持续优于现有最先进方法。

【方法概述 / Method】
FAAR是一种专为NVFP4格式设计的可学习舍入策略，通过梯度优化自适应调整舍入决策以匹配NVFP4的非均匀数值分布；同时引入2FA（2-stages Format Alignment）逐层微调方案，将LLM参数对齐到NVFP4数值空间，进一步缩小性能差距。

【实验结果 / Results】
在WikiText-2数据集上，相比最近邻舍入（RTN），FAAR将Llama3-1B的困惑度从14.28降至12.60，Qwen3-1.7B从23.06降至21.27；该学习优化过程在Llama3-1B上仅消耗约4 GPU小时训练时间，且在多种零样本下游任务上 consistently 超越现有最优方法。

【应用价值 / Applications】
FAAR为边缘设备部署大语言模型提供了高效的超低精度量化方案，在极低的训练成本下实现接近最优的量化效果，可广泛应用于移动端AI推理、嵌入式智能系统等资源受限场景，推动LLM在边缘计算环境中的实际落地。
