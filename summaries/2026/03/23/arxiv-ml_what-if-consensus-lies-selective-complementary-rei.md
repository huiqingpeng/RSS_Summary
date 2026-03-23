---
title: "What If Consensus Lies? Selective-Complementary Reinforcement Learning at Test Time"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19880"
published: "2026-03-23"
summarized: "2026-03-24T07:23:20.882311"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SCRL（Selective-Complementary Reinforcement Learning），一种鲁棒的测试时强化学习框架，用于解决现有TTRL方法在答案分布高度分散时因弱共识而错误强化不正确推理轨迹的问题。SCRL通过选择性正伪标签策略严格过滤不可靠的多数共识，并首次引入基于熵门控的负伪标签机制来剪枝错误轨迹。实验表明，该方法在多个推理基准上显著优于基线，且在受限推理预算下保持良好的泛化性和训练稳定性。

【方法概述 / Method】
SCRL采用双机制设计：选择性正伪标签机制通过严格的共识标准筛选可靠的多数答案作为正监督信号；熵门控负伪标签机制则利用生成不确定性识别并惩罚高置信度的错误轨迹，首次将负监督引入TTRL框架。两种机制互补协作，有效缓解标签噪声放大问题。

【实验结果 / Results】
SCRL在多个推理基准测试上相比现有TTRL基线取得显著提升，同时展现出优异的鲁棒泛化能力。该方法在受限的推理预算（rollout budgets）条件下仍能保持训练稳定性，证明了其在资源受限场景下的实用价值。

【应用价值 / Applications】
该研究适用于需要大规模语言模型进行复杂推理但实际标注数据稀缺的场景，如数学问题求解、代码生成和科学推理等。SCRL通过提升测试时学习的可靠性，降低了对人工标注的依赖，为部署在开放环境中的LLM推理系统提供了更稳健的自主改进方案。
