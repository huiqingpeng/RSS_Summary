---
title: "Mapping Space Exploration for Multi-Chiplet Accelerators Targeting LLM Inference Serving Workloads"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2512.06093"
published: "2026-04-02"
summarized: "2026-04-03T07:15:58.663924"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对大语言模型（LLM）推理服务对多芯粒加速器的需求，提出了一种新的映射空间探索方法。现有研究主要面向传统CNN/Transformer工作负载，无法有效支持真实LLM推理服务中动态的请求类型混合和可变序列长度。为此，作者提出了基于计算执行图的映射编码方案，并开发了Compass框架，实现了平均63.12%的EDP（能量延迟积）降低。

【方法概述 / Method】
论文提出了一种计算执行图（computation execution graph）的映射编码方案，将微批次（micro-batches）与层（layers）解耦，从而在异构芯粒上实现细粒度执行控制，并灵活表示各种并行策略。在此基础上，开发了Compass框架，集成了评估引擎和基于遗传算法的映射生成引擎，以高效搜索最优映射方案。

【实验结果 / Results】
与最先进的工作相比，该解决方案实现了平均63.12%的EDP（能量延迟积）降低，显著提升了多芯粒加速器在LLM推理服务工作负载上的能效表现。

【应用价值 / Applications】
该研究可直接应用于大规模LLM推理部署场景，如云端AI服务、数据中心等需要高效处理动态混合请求的环境。通过优化多芯粒加速器的任务映射策略，能够提升硬件利用率、降低推理延迟和能耗，为下一代AI加速器设计提供重要的方法论支持。
