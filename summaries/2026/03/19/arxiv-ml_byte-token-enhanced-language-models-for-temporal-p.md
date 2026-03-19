---
title: "Byte-token Enhanced Language Models for Temporal Point Processes Analysis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2502.07139"
published: "2026-03-19"
summarized: "2026-03-19T14:14:41.008456"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Language-TPP，一个将时序点过程（TPPs）与大语言模型（LLMs）统一融合的框架，用于增强网络事件序列建模。核心创新在于将连续时间间隔转换为专门的"字节token"（byte-tokens）的新型时序编码机制，使标准语言模型架构无需TPP特定修改即可直接进行TPP建模。该框架在多个真实世界数据集（电商评论、社交媒体、在线问答平台）上实现了事件时间预测和类型预测的SOTA性能，同时解锁了TPP研究的新能力：时序信息的引入显著提升了生成事件描述的质量（更高的ROUGE-L分数和更一致的情感分布）。

【方法概述 / Method】
论文采用字节token增强的时序编码机制，将连续的时间间隔离散化为可与文本token统一处理的特殊token，从而实现时序动态与文本描述的无缝融合。该方法直接利用标准Transformer架构，无需设计专门的TPP组件（如强度函数或递归结构），通过简单的token级处理统一建模时间和文本信息。

【实验结果 / Results】
Language-TPP在多个TPP基准测试上达到SOTA性能，涵盖事件时间预测和事件类型预测任务；生成任务方面，引入时序信息使ROUGE-L分数显著提升，并产生更一致的情感分布；此外，框架在长序列上展现出良好的可扩展性，并通过定性分析验证了其对学习分布的有效捕捉。

【应用价值 / Applications】
该研究对内容生成（如自动撰写带有时序上下文的用户评论）、用户行为理解（分析网络平台的时序交互模式）以及Web平台应用（个性化推荐、异常检测）具有重要价值；统一的LLM-TPP框架还为未来开发具备时序感知能力的通用基础模型奠定了基础。
