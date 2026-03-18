---
title: "Theoretical Foundations of Latent Posterior Factors: Formal Guarantees for Multi-Evidence Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15674"
published: "2026-03-18"
summarized: "2026-03-18T16:06:19.619954"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Latent Posterior Factors (LPF)的完整理论刻画，这是一个用于概率预测任务中聚合多源异构证据的原则性框架。LPF通过变分自编码器将每个证据项编码为高斯潜在后验，经蒙特卡洛边缘化转换为软因子，并通过精确Sum-Product Network推断或学习神经聚合器进行聚合。作者证明了涵盖可信AI关键需求的七项形式化保证，包括校准保持、蒙特卡洛误差衰减、非空泛化PAC-Bayes界、接近信息论下界、对抗腐败下的优雅降级、校准衰减规律以及认知-偶然不确定性的精确分解，所有定理均在多达4,200个训练样本的控制数据集上得到验证。

【方法概述 / Method】
LPF框架采用三阶段架构：首先使用变分自编码器将异构证据编码为结构化高斯潜在后验分布；然后通过蒙特卡洛采样将后验转换为可组合的软因子表示；最后通过两种聚合方式——基于精确概率推断的LPF-SPN或数据驱动的LPF-Learned神经聚合器——实现多证据融合。

【实验结果 / Results】
实验验证了七项理论保证：期望校准误差满足ECE ≤ ε + C/√K_eff；蒙特卡洛误差以O(1/√M)速率衰减；在N=4,200时PAC-Bayes训练-测试间隙仅为0.0085；运行效率达信息论下界的1.12倍；对抗攻击下半数证据被替换仍保持88%性能，降级速率为O(ε·δ·√K)；校准衰减遵循O(1/√K)规律且R²=0.849；认知-偶然不确定性分解误差低于0.002%。

【应用价值 / Applications】
LPF框架适用于医疗诊断、金融风险评估、法律案例分析和监管合规等高 stakes 领域的多证据推理场景，为安全关键型AI应用提供了具有形式化可信保证的理论基础，解决了现有方法缺乏理论保证或无法架构化处理多证据场景的核心痛点。
