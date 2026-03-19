---
title: "Do Understanding and Generation Fight? A Diagnostic Study of DPO for Unified Multimodal Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17044"
published: "2026-03-19"
summarized: "2026-03-19T12:06:52.430278"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究首次系统性地探究了直接偏好优化（DPO）能否同时对齐统一多模态模型的理解与生成能力。研究发现，在Janus-Pro架构（1B和7B参数）上，生成质量对所有DPO训练策略均表现出抗性，7B模型上无任何方法能提升生成CLIPScore，1B模型上所有方法反而损害生成性能。梯度分析揭示理解与生成梯度近乎正交（余弦相似度≈0）且存在11-14倍的幅度失衡，这种由VQ token数量不对称（576个生成token vs. 30-100个文本token）驱动的失衡是多任务DPO中的主要干扰机制。

【方法概述 / Method】

研究在Janus-Pro 1B和7B模型上实施了七种DPO训练策略（包括标准DPO、加权DPO、任务解耦等）和两种事后分析方法，测试了两种偏好数据类型（真实vs生成图像、模型vs模型比较）及150-288对的数据规模。通过梯度分析量化理解与生成任务的梯度方向与幅度关系，并采用统计显著性检验（n=200每种子，3个种子）评估结果可靠性。

【实验结果 / Results】

7B模型上所有DPO方法对生成CLIPScore的改善均不显著（|Δ|<0.2, p>0.5）；1B模型上所有方法均损害生成性能。梯度余弦相似度接近0，生成梯度幅度约为理解梯度的11-14倍。幅度平衡策略虽使理解任务产生正向变化（VQA提升+0.01-0.04），但生成差距依然存在。生成DPO损失收敛至ln(2)的现象表明离散VQ token化可能是结构性瓶颈。

【应用价值 / Applications】

本研究为使用VQ-based统一多模态模型的实践者提供了关键指导：当前DPO方法难以同时优化理解与生成，需针对生成任务设计专门的优化策略或改进架构（如替代离散token化）。研究结果对视觉-语言模型、多模态内容生成系统的训练流程优化具有重要参考价值，特别是在需要高质量图像生成的应用场景中。
