---
title: "Locate-then-Sparsify: Attribution Guided Sparse Strategy for Visual Hallucination Mitigation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16284"
published: "2026-03-18"
summarized: "2026-03-18T16:11:48.840461"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对大型视觉-语言模型（LVLMs）中的视觉幻觉问题，提出了一种名为Locate-Then-Sparsify for Feature Steering（LTS-FS）的即插即用框架。该框架通过构建包含token级和句子级幻觉的合成数据集，引入基于因果干预的归因方法来量化各层与幻觉的相关性，并据此实现逐层的差异化特征引导强度控制。实验表明，LTS-FS能在有效缓解幻觉的同时，保持模型在通用任务上的性能。

【方法概述 / Method】
作者首先构建了一个合成幻觉数据集，涵盖token级和句子级两种幻觉案例；随后基于因果干预理论设计归因方法，计算每层对幻觉生成的贡献分数；最后提出逐层稀疏化策略，将归因分数转化为各层特征引导强度，实现对幻觉相关层的精准调控而非均匀干预。

【实验结果 / Results】
在多个LVLMs和基准测试上的广泛实验表明，LTS-FS框架能够有效降低视觉幻觉现象，同时维持模型在通用视觉-语言任务上的强劲表现，避免了传统均匀特征引导方法导致的性能退化问题。

【应用价值 / Applications】
该研究可提升大型视觉-语言模型在自动驾驶、医疗影像诊断、视觉问答等高风险场景中的可靠性，通过低成本即插即用的方式增强模型输出的可信度，促进LVLMs在关键实际应用中的安全部署。
