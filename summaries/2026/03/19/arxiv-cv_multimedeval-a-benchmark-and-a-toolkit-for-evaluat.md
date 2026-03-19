---
title: "MultiMedEval: A Benchmark and a Toolkit for Evaluating Medical Vision-Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2402.09262"
published: "2026-03-19"
summarized: "2026-03-19T16:23:36.034742"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MultiMedEval，一个开源工具包，用于公平且可复现地评估大型医学视觉-语言模型（VLM）。该工具包全面评估模型在6种多模态任务上的性能，涵盖23个数据集和11个医学领域，基于社区广泛采用的多样化指标确保对模型泛化能力的 thorough 评估。作者开源了Python工具包，提供简洁的接口和设置流程，仅需几行代码即可完成任意VLM的评估，旨在简化VLM评估的复杂现状，促进未来模型的公平统一基准测试。

【方法概述 / Method】
MultiMedEval采用模块化设计，整合六种多模态医学任务（如视觉问答、图像分类、报告生成等），覆盖23个公开医学数据集。工具包提供标准化评估流程和统一接口，支持用户通过简单配置快速接入自定义模型，并自动计算多种性能指标以确保评估的一致性和可复现性。

【实验结果 / Results】
论文通过该工具包对多个主流医学VLM进行了系统评估，揭示了不同模型在各任务和医学领域间的性能差异与泛化瓶颈。实验结果表明，现有模型在跨域迁移和复杂临床场景下仍存在显著不足，为后续模型改进提供了明确方向。

【应用价值 / Applications】
MultiMedEval为医学AI研究社区提供了标准化评估基础设施，可用于新药研发的影像分析、临床决策支持系统的模型选型、以及医学VLM的公平比较与监管审批。该工具包降低了评估门槛，有助于加速安全可靠的医学人工智能技术的临床转化与部署。
