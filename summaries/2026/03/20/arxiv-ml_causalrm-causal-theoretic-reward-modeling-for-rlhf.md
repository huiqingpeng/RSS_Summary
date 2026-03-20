---
title: "CausalRM: Causal-Theoretic Reward Modeling for RLHF from Observational User Feedbacks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18736"
published: "2026-03-20"
summarized: "2026-03-20T12:15:25.374817"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CausalRM，一种从观测性用户反馈（如点击、复制、点赞）中学习奖励模型的因果理论框架，作为传统RLHF中昂贵实验性反馈的可扩展替代方案。研究识别出观测反馈的两个核心挑战：标注噪声导致的偏好偏离，以及用户选择性反馈造成的分布偏移。CausalRM通过噪声感知替代损失和基于倾向得分的样本重加权分别解决这两个问题，在WildGuardMix和HarmBench等基准上分别取得49.2%和32.7%的性能提升。

【方法概述 / Method】
CausalRM采用因果推断理论构建奖励建模框架：针对噪声问题，引入显式建模标注错误生成过程的噪声感知替代损失项，证明其在无噪声条件下与原损失等价；针对选择偏误，利用倾向得分（用户反馈概率）对训练样本重加权，消除用户偏好导致的分布偏移。

【实验结果 / Results】
实验在多种LLM骨干网络和基准数据集上验证了CausalRM的有效性，表明其能从噪声且偏倚的观测反馈中准确学习奖励信号；在下游RLHF任务中，CausalRM在WildGuardMix上提升49.2%，在HarmBench上提升32.7%，展现出显著的性能优势。

【应用价值 / Applications】
CausalRM为大规模语言模型对齐提供了一种成本效益更高的RLHF方案，可直接利用廉价易得的观测性用户行为数据替代昂贵的人工标注实验数据；该框架适用于内容推荐、对话系统等需要持续从真实用户交互中学习偏好的场景，降低了高质量奖励模型的获取门槛。
