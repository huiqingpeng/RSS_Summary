---
title: "Omanic: Towards Step-wise Evaluation of Multi-hop Reasoning in Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16654"
published: "2026-03-18"
summarized: "2026-03-18T16:13:48.113946"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Omanic，一个用于评估大型语言模型多跳推理能力的开放域问答资源，通过提供分解的子问题和中间答案作为结构化标注，解决了现有基准缺乏步骤级注释、难以诊断推理失败位置的问题。该资源包含10,296个机器生成的训练样本（OmanicSynth）和967个专家审核的人工标注评估样本（OmanicBench）。研究发现，最先进的LLM在OmanicBench上仅达到73.11%的多选准确率，且链式思维（CoT）的性能依赖于事实完整性，知识缺口会导致收益递减，错误会在后续跳步中放大。

【方法概述 / Method】
本文构建了一个具有步骤级标注的多跳问答数据集，将复杂问题分解为带中间答案的子问题序列，形成结构化的推理路径；同时开发了机器生成数据 pipeline（OmanicSynth）用于监督微调，以及严格的人工标注基准（OmanicBench）用于可靠评估。

【实验结果 / Results】
实验显示，主流推理模型在OmanicBench上的准确率仅为73.11%，表明该基准具有较高难度；步骤级分析揭示CoT的增益在知识不完整时显著下降，且早期错误会向后续推理步骤传播放大；在OmanicSynth上进行监督微调可在六个推理和数学基准上平均提升7.41个百分点，验证了数据集质量及其向通用推理能力的迁移效果。

【应用价值 / Applications】
该研究为LLM推理能力的细粒度诊断提供了标准化工具，可帮助开发者定位模型在复杂推理中的具体失败环节；OmanicSynth可作为高质量的推理训练数据，用于提升模型在多跳问答、数学推理等任务上的表现；该框架还可扩展至教育评估、智能问答系统等需要可解释推理过程的应用场景。
