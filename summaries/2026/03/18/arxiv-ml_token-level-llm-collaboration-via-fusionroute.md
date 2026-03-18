---
title: "Token-Level LLM Collaboration via FusionRoute"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.05106"
published: "2026-03-18"
summarized: "2026-03-18T17:13:42.318090"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了FusionRoute，一种基于token级别的多LLM协作框架，通过轻量级路由器在每个解码步骤选择最合适的专家模型，并生成互补的logit来修正所选专家的输出分布。作者从理论上证明了纯专家路由存在根本性局限，而FusionRoute通过引入可训练的互补生成器扩展了有效策略类，能够在温和条件下恢复最优值函数。实验表明，该方法在数学推理、代码生成和指令遵循等任务上均优于序列级/token级协作、模型合并和直接微调等方法。

【方法概述 / Method】

FusionRoute采用双组件架构：（1）轻量级路由器基于当前上下文为每个token选择最合适的专家LLM；（2）路由器同时生成一个互补logit，通过logit加法与所选专家的输出分布融合。这种设计突破了传统token级协作仅依赖固定专家输出的限制，使路由器能够主动修正或细化专家的预测。

【实验结果 / Results】

在Llama-3和Gemma-2模型家族上的实验显示，FusionRoute在多个基准测试（包括数学推理、代码生成和指令遵循）中均优于现有的序列级协作、token级协作、模型合并以及直接微调基线，同时在各专家擅长的特定任务上保持竞争力。该方法实现了更强的跨领域泛化能力，而无需训练超大型的通用模型。

【应用价值 / Applications】

FusionRoute为构建高效的多领域AI系统提供了实用方案，特别适用于需要在数学推理、编程、对话等多个专业领域同时保持高性能的场景。该方法允许组合多个小型专家模型而非部署单一巨型模型，显著降低了训练和推理成本，为资源受限环境下的企业级LLM部署提供了可行路径。
