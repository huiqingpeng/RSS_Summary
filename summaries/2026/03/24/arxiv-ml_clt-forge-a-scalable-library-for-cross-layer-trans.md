---
title: "CLT-Forge: A Scalable Library for Cross-Layer Transcoders and Attribution Graphs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.21014"
published: "2026-03-24"
summarized: "2026-03-25T07:17:47.272374"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CLT-Forge，一个用于跨层转码器（Cross-Layer Transcoders, CLTs）端到端训练和可解释性分析的开源库。CLTs通过跨层共享特征同时保持层特定解码，解决了传统特征归因图庞大冗余的问题，但此前难以大规模训练和分析。该库集成了分布式训练、自动特征解释、归因图计算和可视化界面，为基于CLT的机械可解释性研究提供了实用且统一的规模化解决方案。

【方法概述 / Method】
CLT-Forge采用模型分片和压缩激活缓存技术实现可扩展的分布式训练，并构建了统一的自动化可解释性流程。该流程结合Circuit-Tracer进行归因图计算，同时提供灵活的可视化接口，支持从训练到分析的全链路CLT研究。

【实验结果 / Results】
论文主要介绍框架设计与功能实现，未报告具体的定量实验结果或性能基准。核心成果是提供了一个完整可用的开源工具库，解决了CLT训练和分析中的工程挑战。

【应用价值 / Applications】
该库可支持研究人员对大型语言模型进行深入的机械可解释性分析，帮助理解模型的内部信息表示与计算机制。其实际价值在于降低CLT技术的应用门槛，促进更高效、可解释的AI系统开发与审计，适用于模型安全、对齐研究和透明化AI部署等场景。
