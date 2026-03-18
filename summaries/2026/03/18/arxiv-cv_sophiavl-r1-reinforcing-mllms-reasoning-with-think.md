---
title: "SophiaVL-R1: Reinforcing MLLMs Reasoning with Thinking Reward"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2505.17018"
published: "2026-03-18"
summarized: "2026-03-18T18:25:58.217388"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SophiaVL-R1，一种通过引入"思考奖励"来增强多模态大语言模型（MLLMs）推理能力的新方法。针对现有基于规则强化学习范式仅关注结果奖励、缺乏对思考过程监督的问题，作者训练了一个思考奖励模型来评估推理过程质量，并设计了Trust-GRPO方法和退火训练策略来缓解奖励黑客问题。实验表明，SophiaVL-R1-7B在多个基准测试上超越了参数量10倍的LLaVA-OneVision-72B，展现出强大的推理和泛化能力。

【方法概述 / Method】
核心方法是构建一个思考奖励模型（Thinking Reward Model）来评估模型生成答案前的完整推理过程质量，并将其与结果奖励结合。为解决思考奖励可能不可靠的问题，提出Trust-GRPO算法，通过比较正确与错误回答的思考奖励差异来计算可信度权重，动态调整思考奖励的影响；同时采用退火策略逐步降低思考奖励权重，使模型后期更依赖准确的结果奖励。

【实验结果 / Results】
SophiaVL-R1在MathVisita、MMMU等多个多模态推理基准上超越了一系列现有推理MLLMs。特别地，仅7B参数的SophiaVL-R1-7B在大多数基准上超过了72B参数的LLaVA-OneVision-72B，实现了约10倍的参数效率提升，证明了该方法在增强模型推理能力和泛化性方面的有效性。

【应用价值 / Applications】
该研究可广泛应用于需要复杂多模态推理的场景，如数学问题求解、科学视觉问答、医学影像分析等。通过以更小的模型规模实现更强的推理性能，该方法有助于降低部署成本，使高性能多模态推理能力更易在资源受限环境中应用，同时开源的代码、模型和数据集也将促进相关领域的研究发展。
