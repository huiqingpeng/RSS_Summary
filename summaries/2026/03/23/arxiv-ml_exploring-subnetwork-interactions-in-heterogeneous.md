---
title: "Exploring Subnetwork Interactions in Heterogeneous Brain Network via Prior-Informed Graph Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19307"
published: "2026-03-23"
summarized: "2026-03-24T07:16:16.835855"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了KD-Brain，一种先验信息引导的图学习框架，用于显式编码先验知识以指导脑功能子网络交互的学习过程。该框架通过语义条件交互机制将语义先验注入注意力查询，并引入病理一致性约束来对齐学习到的交互分布与临床先验。KD-Brain在多种精神障碍诊断任务上达到了最先进的性能，并识别出与精神病病理生理学一致的可解释生物标志物。

【方法概述 / Method】
KD-Brain采用先验信息引导的图学习方法，核心包含两个关键组件：一是语义条件交互机制，将功能子网络的语义先验注入Transformer的注意力查询中，显式引导基于功能身份的子网络交互学习；二是病理一致性约束，通过正则化模型优化过程，使学习到的交互分布与临床先验知识保持一致。

【实验结果 / Results】
KD-Brain在广泛的精神障碍诊断任务上取得了最先进的性能表现。该方法成功识别出与精神病病理生理学一致的可解释生物标志物，证明了其在捕捉有意义子网络交互方面的有效性，同时在小样本训练条件下展现出优于现有Transformer方法的鲁棒性。

【应用价值 / Applications】
该研究具有重要的临床应用价值，可用于精神障碍的辅助诊断和功能性神经通路的识别。通过整合神经科学先验知识，KD-Brain为脑网络分析提供了可解释的计算工具，有助于深入理解精神疾病的神经机制，并可能推动个性化治疗策略的发展。
