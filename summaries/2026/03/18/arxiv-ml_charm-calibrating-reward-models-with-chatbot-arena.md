---
title: "CHARM: Calibrating Reward Models With Chatbot Arena Scores"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2504.10045"
published: "2026-03-18"
summarized: "2026-03-18T17:09:52.850955"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文识别了奖励模型（RMs）中存在的一种"模型偏好偏差"——即系统性地对某些策略模型的回复给出过高分数，导致不公平判断。为此，作者提出了CHARM（CHatbot Arena calibrated Reward Modeling）校准方法，利用Chatbot Arena的Elo分数构建去偏好的偏好数据集并调整奖励模型评分。实验表明，校准后的奖励模型在RM-Bench和RewardBench的Chat-Hard域上评估准确率提升，与人类偏好相关性更强，且能改善下游后训练性能。

【方法概述 / Method】

CHARM通过利用大规模众包平台Chatbot Arena的Elo评分作为人类偏好的可靠代理，构建去偏好的偏好数据集。该方法通过对比不同模型在相同提示下的Elo排名差异，识别并校正奖励模型对特定策略模型的系统性评分偏差，从而实现奖励模型的校准。

【实验结果 / Results】

校准后的奖励模型在RM-Bench和RewardBench的Chat-Hard领域表现出更高的评估准确率；其评分与Elo排名的相关性显著增强，更贴近真实人类偏好；此外，在下游的后训练任务中，使用CHARM校准奖励模型的策略优化也展现出更好的性能表现。

【应用价值 / Applications】

CHARM可广泛应用于RLHF流程中的奖励模型优化，提升大语言模型对齐质量；为模型评估平台提供更公平、可靠的自动评分机制；同时其简单易实现的特点使其能够快速集成到现有的奖励模型训练 pipeline 中，提高模型开发效率和可信度。
