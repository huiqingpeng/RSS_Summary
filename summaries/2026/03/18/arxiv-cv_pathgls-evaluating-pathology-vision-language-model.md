---
title: "PathGLS: Evaluating Pathology Vision-Language Models without Ground Truth through Multi-Dimensional Consistency"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16113"
published: "2026-03-18"
summarized: "2026-03-18T18:05:52.134906"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了PathGLS，一种无需参考标注的病理视觉-语言模型（VLM）评估框架，通过三个维度（Grounding细粒度视觉-文本对齐、Logic蕴涵图一致性、Stability对抗扰动下的输出稳定性）综合评估模型质量。实验表明，PathGLS在Quilt-1M数据集上对幻觉报告的敏感度下降达40.2%，远超BERTScore的2.1%；与专家定义的临床错误层级相比，其Spearman秩相关系数达0.71，显著优于Gemini 3.0 Pro等LLM方法（ρ=0.39），为病理VLM的可靠评估提供了新基准。

【方法概述 / Method】
PathGLS采用三维一致性评估架构：Grounding维度通过细粒度跨模态对齐检测视觉-文本不匹配；Logic维度利用自然语言推理（NLI）构建蕴涵图验证报告的逻辑连贯性；Stability维度通过对抗性视觉-语义扰动测试输出鲁棒性。该框架支持补丁级和全切片图像（WSI）级分析，最终输出综合信任评分。

【实验结果 / Results】
在Quilt-1M、TCGA、REG2025、PathMMU和TCGA-Sarcoma多数据集验证中，PathGLS展现出卓越的幻觉检测能力：对幻觉报告的敏感度降幅达40.2%，较传统指标提升近20倍；与专家临床错误层级的一致性达ρ=0.71（p<0.0001），显著优于LLM评估方法；同时可有效量化域迁移鲁棒性，为私有临床数据集上的模型基准测试提供可靠依据。

【应用价值 / Applications】
PathGLS为病理VLM的临床安全部署提供关键工具：无需真实标注即可直接量化幻觉率和域迁移鲁棒性，适用于私有临床数据集的模型筛选与监控；其多维一致性评估机制可指导模型改进方向，降低自动化病理诊断中的临床风险，推动可解释、可信的计算病理学应用落地。
