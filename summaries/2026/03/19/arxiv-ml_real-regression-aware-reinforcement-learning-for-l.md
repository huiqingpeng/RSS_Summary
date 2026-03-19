---
title: "REAL: Regression-Aware Reinforcement Learning for LLM-as-a-Judge"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17145"
published: "2026-03-19"
summarized: "2026-03-19T12:08:05.189381"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了REAL（Regression-Aware Reinforcement Learning），一种针对LLM-as-a-Judge场景优化的强化学习框架，用于解决回归任务中标准RL方法忽略序数结构的问题。该框架通过广义策略梯度估计器将优化分解为思维链探索与回归感知预测精修两个互补组件，理论上证明对相关性指标最优。实验表明，在8B至32B参数规模的模型上，REAL显著优于回归感知的SFT基线和标准RL方法，在Qwen3-32B上相比SFT基线提升Pearson相关系数8.40、Spearman相关系数7.20。

【方法概述 / Method】

REAL采用广义策略梯度估计器处理显式依赖于策略的回归目标函数，克服了标准策略梯度方法在此场景下的失效问题。该方法将优化过程自然分解为两个部分：一是对思维链（Chain-of-Thought）推理轨迹的探索，二是对最终评分预测的回归感知精修，从而实现推理路径优化与评分准确性的协同提升。

【实验结果 / Results】

跨模型规模（8B-32B）的广泛实验显示REAL在域外基准测试上具有显著更好的泛化能力。在Qwen3-32B模型上，REAL相比SFT基线获得Pearson +8.40和Spearman +7.20的提升，相比基础模型更是达到+18.30/+11.20的改进幅度。该方法同时超越了标准RL方法和回归感知SFT基线，验证了将回归目标整合进RL探索的有效性。

【应用价值 / Applications】

REAL可直接应用于需要精确数值评估的LLM-as-a-Judge场景，如自动化模型输出质量评分、生成内容排序、多维度评估等任务，提升评估的细粒度区分能力。该研究为构建更准确的自动化评估系统提供了方法论基础，对模型训练中的奖励建模、RLHF优化以及评估基准的自动化标注具有重要实践意义。
