---
title: "Learning to Select Visual In-Context Demonstrations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26775"
published: "2026-03-31"
summarized: "2026-04-01T07:17:57.401147"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对多模态大语言模型（MLLMs）的视觉上下文学习（ICL）中示例选择问题，提出传统的无监督k近邻（kNN）搜索策略在复杂事实回归任务中存在局限性，因其倾向于选择冗余示例而无法覆盖完整的输出范围。作者将示例选择重新定义为序列决策问题，提出LSD（Learning to Select Demonstrations）方法，利用基于Dueling DQN的强化学习智能体学习最优示例选择策略。实验发现kNN在主观偏好任务上仍具优势，而LSD在客观事实回归任务上显著优于基线方法，揭示了视觉ICL中学习型选择的必要性条件。

【方法概述 / Method】
LSD采用强化学习框架，将示例选择建模为马尔可夫决策过程，智能体通过迭代选择示例构建演示集。具体实现上使用Dueling DQN架构，结合以查询为中心的Transformer解码器编码状态信息，以最大化MLLM下游任务性能作为奖励信号进行策略优化。

【实验结果 / Results】
在五个视觉回归基准上的评估显示，LSD在客观事实回归任务（如深度估计、年龄预测等）上显著超越kNN基线，而在主观偏好任务（如美学评分）上kNN仍保持最优。结果表明LSD通过平衡视觉相关性与多样性，能够更准确地界定回归边界。

【应用价值 / Applications】
该研究为视觉ICL系统提供了任务自适应的示例选择机制，可提升MLLM在需要精确数值预测的客观视觉任务中的性能，适用于自动驾驶感知、医学影像分析、工业质检等需要可靠视觉回归预测的场景，同时明确了何时需要采用学习型选择而非简单相似度搜索。
