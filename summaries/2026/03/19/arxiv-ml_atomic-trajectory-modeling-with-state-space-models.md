---
title: "Atomic Trajectory Modeling with State Space Models for Biomolecular Dynamics"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17633"
published: "2026-03-19"
summarized: "2026-03-19T13:14:25.575846"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 ATMOS，一种基于状态空间模型（SSM）的新型生成框架，用于生成生物分子系统的原子级分子动力学（MD）轨迹。该模型整合了 Pairformer 状态转移机制以捕获长程时间依赖关系，并采用基于扩散的模块以自回归方式解码轨迹帧。ATMOS 在 PDB 晶体结构及大规模 MD 模拟数据集（mdCATH 和 MISATO）上训练，在蛋白质单体和蛋白质-配体复合物系统的构象轨迹生成方面均达到最先进的性能，为生物分子动力学建模奠定了有前景的基础。

【方法概述 / Method】

ATMOS 采用状态空间模型（SSM）作为核心架构，结合 Pairformer 状态转移机制建模长程时间依赖性，并通过扩散模型模块实现轨迹帧的自回归解码。该框架在多样化的训练数据上进行学习，包括晶体结构数据和真实 MD 模拟轨迹，以实现对复杂生物分子系统动态行为的建模。

【实验结果 / Results】

ATMOS 在生成蛋白质单体和蛋白质-配体复合物的构象轨迹方面取得了最先进的性能。模型能够有效捕获生物分子系统的长程时间依赖关系，实现高效的原子运动轨迹推断，显著加速了传统 MD 模拟难以企及的长时尺度动力学过程。

【应用价值 / Applications】

该研究为药物发现和生物功能研究提供了高效的计算工具，可显著降低长时尺度分子动力学模拟的计算成本。ATMOS 能够模拟复杂的蛋白质-配体相互作用动态，有助于理解生物分子功能机制、预测构象变化，并加速基于结构的药物设计流程。
