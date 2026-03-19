---
title: "Contrastive Reasoning Alignment: Reinforcement Learning from Hidden Representations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17305"
published: "2026-03-19"
summarized: "2026-03-19T13:11:17.103360"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出CRAFT（Contrastive Reasoning Alignment Framework for Training），一种针对大型推理模型的红队对齐框架，通过利用模型的推理能力和隐藏层表示来增强对越狱攻击的鲁棒性。与主要在输出层面运作的现有防御方法不同，CRAFT在隐藏状态空间上定义优化目标，使模型生成具有安全意识的推理轨迹。该框架将对比表示学习与强化学习相结合，在安全和不安全的推理轨迹之间建立清晰的潜在空间几何结构，在多个安全基准测试中实现了显著的性能提升。

【方法概述 / Method】
CRAFT采用两阶段训练策略：首先通过对比学习在隐藏状态空间中分离安全与不安全的推理轨迹，构建具有判别性的潜在空间几何结构；随后结合潜在-文本一致性约束的GRPO（Group Relative Policy Optimization）强化学习进行微调，从理论上消除表面安全的局部最优策略，确保推理层面的深度对齐。

【实验结果 / Results】
在Qwen3-4B-Thinking和R1-Distill-Llama-8B两个强推理模型上的评估表明，CRAFT平均实现推理安全性提升79.0%、最终响应安全性提升87.7%，显著优于IPO和SafeKey等最先进防御方法。理论分析证明，引入潜在-文本一致性约束可有效排除表面安全的次优策略。

【应用价值 / Applications】
CRAFT适用于需要高安全性保障的大语言模型部署场景，如企业级AI助手、内容审核系统和敏感信息处理平台。该研究为构建具有内在安全推理能力的AI系统提供了新范式，特别是在面对复杂越狱攻击时，能够在推理过程而非仅输出层面实现可靠的安全防护。
