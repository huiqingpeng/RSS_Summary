---
title: "FIPO: Eliciting Deep Reasoning with Future-KL Influenced Policy Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19835"
published: "2026-03-23"
summarized: "2026-03-24T07:22:49.945938"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出未来KL散度影响策略优化（FIPO），一种旨在突破大语言模型推理瓶颈的强化学习算法。FIPO通过将折扣未来KL散度纳入策略更新，构建密集优势函数，根据token对后续轨迹行为的影响重新加权，解决了GRPO类方法中基于结果奖励的粗粒度信用分配问题。在Qwen2.5-32B上的实验表明，FIPO将平均思维链长度从约4,000 token扩展至10,000以上，AIME 2024 Pass@1准确率从50.0%提升至峰值58.0%，超越了DeepSeek-R1-Zero-Math-32B和o1-mini。

【方法概述 / Method】
FIPO的核心创新在于引入折扣未来KL散度作为密集优势信号，替代传统ORM方法中将全局优势均匀分配给轨迹中每个token的做法。该方法通过量化每个token对后续策略行为分布的影响程度，实现对关键逻辑转折点的精细信用分配，从而引导模型生成更长、更深的推理链。

【实验结果 / Results】
在Qwen2.5-32B模型上的评估显示，FIPO显著突破了基线方法的长度停滞问题，平均推理长度扩展至2.5倍以上。AIME 2024 Pass@1准确率达到峰值58.0%（收敛于约56.0%），较GRPO基线（50.0%）提升8个百分点，并优于DeepSeek-R1-Zero-Math-32B（约47.0%）和o1-mini（约56.0%）。

【应用价值 / Applications】
FIPO为提升大语言模型的深度推理能力提供了可扩展的训练范式，特别适用于数学证明、复杂问题求解等需要长链条推理的场景。该研究验证了密集优势函数设计在解锁基模型推理潜力方面的关键作用，为ORM-based算法的演进指明了方向，且训练系统已开源便于社区复用。
