---
title: "Attention Sinks Are Provably Necessary in Softmax Transformers: Evidence from Trigger-Conditional Tasks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.11487"
published: "2026-03-18"
summarized: "2026-03-18T17:05:54.993676"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文从理论上证明了注意力汇聚点（attention sinks）在某些情况下是softmax Transformer的功能性必需组件，而非仅仅是优化或训练的副产品。作者通过设计一个触发条件任务（trigger-conditional task）——当特定触发词出现时输出前面所有token表示的平均值，否则输出零——严格证明了softmax自注意力必须形成汇聚点才能实现这种默认状态。相比之下，非归一化的ReLU注意力可以在没有汇聚点的情况下解决相同任务，证实了归一化约束是汇聚行为的根本驱动力。实验结果验证了这一理论预测，并在单头和多头设置中均成立。

【方法概述 / Method】
论文采用理论证明与实验验证相结合的方法。理论上，作者构造了一个具体的触发条件任务，利用概率单纯形上的归一化约束进行形式化分析，证明softmax注意力必须将概率质量集中在固定位置以形成"默认"行为。实验上，对比了softmax注意力与ReLU注意力在相同任务上的表现，并扩展到多头Transformer架构进行验证。

【实验结果 / Results】
实验验证了理论预测：softmax模型确实发展出强烈的注意力汇聚点，而ReLU注意力则完全消除了这一现象。该结论在单头（single-head）和多头（multi-head）变体中均成立，表明理论分析的结果能够推广到更广泛的实际设置中。这些发现与先前观察到的真实注意力头行为（如Barbero et al., 2025; Guo et al., 2024）相吻合。

【应用价值 / Applications】
该研究为理解Transformer的内部工作机制提供了理论基础，特别是解释了为何大型语言模型中会出现注意力汇聚现象（如LLaMA等模型中观察到的[CLS]或初始token汇聚）。这一认识有助于指导模型架构设计——例如在需要避免汇聚点时可考虑替代注意力机制（如ReLU），同时为理解模型的默认行为和条件计算能力提供了形式化框架，对可解释性AI研究具有重要参考价值。
