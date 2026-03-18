---
title: "Can Multimodal LLMs See Science Instruction? Benchmarking Pedagogical Reasoning in K-12 Classroom Videos"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.18466"
published: "2026-03-18"
summarized: "2026-03-18T19:07:01.581755"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了首个针对K-12科学课堂视频分析的基准测试SciIBI，包含113个符合NGSS标准的视频片段，标注了核心教学实践（CIP）及其复杂度等级。研究评估了8种最先进的LLM和多模态LLM，发现当前模型难以区分教学上相似的实践，且视频输入带来的性能提升不一致。关键发现是模型常通过表面捷径而非真正的教学理解来取得成功，揭示了科学课堂话语分析对多模态AI的挑战性。

【方法概述 / Method】
作者构建了SciIBI数据集，涵盖NGSS强调的基于模型的推理和视觉工件的科学课堂视频。研究设计了基于证据的评估框架，测试模型在CIP分类和复杂度评级任务上的表现，对比了纯文本输入（转录本）与多模态输入（视频+文本）的效果。

【实验结果 / Results】
实验显示，多模态LLM在科学教学实践识别上存在根本性局限，添加视频输入并未带来一致的性能提升，不同架构间差异显著。模型倾向于依赖表面模式匹配而非深层教学推理，在需要精细区分的教学场景（如不同复杂度层级的CIP）上表现薄弱。

【应用价值 / Applications】
该研究为教育AI领域确立了新的挑战性基准，指出当前技术更适合作为人机协作工具——用于检索证据以加速专家审核，而非替代人类专家。研究成果对开发智能教学辅助系统、教师专业发展工具以及课堂质量评估平台具有重要指导意义。
