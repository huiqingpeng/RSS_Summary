---
title: "EvoGuard: An Extensible Agentic RL-based Framework for Practical and Evolving AI-Generated Image Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17343"
published: "2026-03-19"
summarized: "2026-03-19T15:08:39.813890"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了EvoGuard，一种基于智能体强化学习的可扩展框架，用于应对不断演化的AI生成图像（AIGI）检测挑战。该框架将多种最先进的多模态大语言模型（MLLM）和非MLLM检测器封装为可调用的工具，通过能力感知的动态编排机制协调它们的工作，并利用智能体的自主规划与反思能力实现多轮调用推理。实验表明，EvoGuard在仅使用低成本二元标签进行GRPO优化的情况下，达到了最先进的检测准确率，同时缓解了正负样本间的偏差，并支持以即插即用方式集成新检测器。

【方法概述 / Method】
EvoGuard采用智能体架构，将异构检测器（包括MLLM和非MLLM模型）统一封装为工具库，通过能力感知的动态编排机制为给定样本智能选择合适的工具组合。框架核心是基于GRPO（Group Relative Policy Optimization）的智能体强化学习算法，仅依赖二元标签进行优化，无需细粒度标注，使智能体能够自主规划、反思中间结果并决定下一步行动。

【实验结果 / Results】
实验表明EvoGuard在AIGI检测任务上达到了最先进的准确率，同时有效缓解了检测过程中正负样本之间的偏差问题。更重要的是，该框架支持以无需重新训练的方式即插即用集成新的检测器，能够持续提升整体性能，为应对不断演变的AIGI威胁提供了长期实用的解决方案。

【应用价值 / Applications】
EvoGuard可广泛应用于社交媒体平台、新闻机构和内容审核系统，用于实时检测和标记AI生成的虚假图像，遏制 misinformation 传播。其可扩展架构特别适合快速迭代的实际部署场景，能够无缝集成未来出现的新型检测技术，降低维护成本，为构建可信的数字内容生态系统提供可持续的技术基础设施。
