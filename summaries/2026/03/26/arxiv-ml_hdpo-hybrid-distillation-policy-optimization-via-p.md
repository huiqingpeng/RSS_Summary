---
title: "HDPO: Hybrid Distillation Policy Optimization via Privileged Self-Distillation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23871"
published: "2026-03-26"
summarized: "2026-03-27T07:18:25.138849"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对数学推理任务中强化学习（RL）的梯度消失问题——即模型在完全无法解决的"悬崖"提示（cliff prompts）上无法获得任何学习信号——提出了混合蒸馏策略优化（HDPO）。HDPO通过特权自蒸馏增强标准RL，为失败提示生成包含真实答案的特权 rollout，并将教师模型的 token 级分布蒸馏给学生。由于师生模型共享权重，可实现性差距有界，且理论证明 R=1 过滤特权生成能在硬阈值极限下恢复最优 KL 正则化 RL 策略。实验表明，HDPO 在 OpenMathInstruct-2 上持续提升覆盖指标（pass@4 提升 0.8-1.1%，pass@8 提升 0.4-1.7%），同时保持贪婪解码准确率。

【方法概述 / Method】
HDPO 的核心机制是识别所有 rollout 均失败的 cliff prompts，通过向模型提供 ground-truth 信息生成特权 rollout，筛选正确解后执行 token 级的自蒸馏。该方法采用共享权重的师生架构，仅在输入层面区分（学生接收标准提示，教师接收含真实答案的特权提示），从而保证蒸馏的可实现性。

【实验结果 / Results】
在 Qwen2.5-Math-1.5B-Instruct 上的实验显示，HDPO 相比基线方法在 pass@4 和 pass@8 指标上分别提升 0.8-1.1% 和 0.4-1.7%，同时不损害 greedy accuracy。蒸馏权重 λ 提供了对探索-利用权衡的直接控制，使模型能够在保持利用能力的同时增强探索覆盖。

【应用价值 / Applications】
HDPO 适用于需要提升大语言模型数学推理覆盖能力的场景，如教育辅助、自动定理证明和复杂问题求解系统。该方法通过解决 RL 中的梯度消失问题，使模型能够从失败案例中学习，对任何存在"悬崖"数据分布的 RL 训练任务（如代码生成、科学推理）均具有潜在应用价值。
