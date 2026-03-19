---
title: "No Need For Real Anomaly: MLLM Empowered Zero-Shot Video Anomaly Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.19248"
published: "2026-03-19"
summarized: "2026-03-19T16:31:34.322558"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了LAVIDA，一种端到端的零样本视频异常检测框架，无需使用真实异常数据进行训练。该框架通过异常曝光采样器生成伪异常，并集成多模态大语言模型（MLLM）增强语义理解能力，同时设计了基于反向注意力的token压缩方法来处理异常模式的时空稀疏性。在四个基准数据集上的实验表明，LAVIDA在零样本设置下达到了帧级和像素级异常检测的最先进性能。

【方法概述 / Method】
LAVIDA采用三阶段技术方案：首先通过Anomaly Exposure Sampler将分割后的正常对象转换为伪异常样本；其次集成多模态大语言模型以捕获上下文相关的异常语义；最后引入基于反向注意力的token压缩机制，在降低计算成本的同时有效处理异常事件的时空稀疏特性。

【实验结果 / Results】
该模型仅在伪异常数据上进行训练，无需任何真实视频异常检测数据，在四个标准VAD基准数据集上均取得了零样本设置下的最优性能，同时在帧级和像素级异常检测任务中均达到SOTA水平。

【应用价值 / Applications】
LAVIDA解决了真实异常数据难以获取的行业痛点，可广泛应用于智能监控、公共安全、工业质检等开放世界场景，显著降低了异常检测系统对大规模标注数据的依赖，为部署于新环境或新兴异常类型的检测任务提供了灵活高效的解决方案。
