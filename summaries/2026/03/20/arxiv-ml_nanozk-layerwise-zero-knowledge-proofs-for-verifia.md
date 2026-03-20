---
title: "NANOZK: Layerwise Zero-Knowledge Proofs for Verifiable Large Language Model Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18046"
published: "2026-03-20"
summarized: "2026-03-20T12:06:35.382969"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了NANOZK（文中称为METHOD），首个用于验证大语言模型推理的零知识证明系统，解决了用户无法验证LLM API服务商是否使用声称模型的问题。该方法利用Transformer推理天然分解为独立层计算的特性，构建了逐层证明框架，每层生成恒定大小的证明。论文开发了针对非算术运算（softmax、GELU、LayerNorm）的查找表近似方法，在零精度损失的前提下实现可验证计算，并引入Fisher信息引导的验证策略以应对全层证明开销过大的场景。

【方法概述 / Method】

NANOZK采用逐层证明架构，将Transformer推理分解为独立的注意力层和MLP层，每层生成常数大小证明（与模型宽度无关），支持并行证明生成。对于非线性激活函数，使用查找表近似将其转化为算术运算，同时保持模型困惑度不变；对于计算开销过大的场景，采用Fisher信息理论指导的关键层选择性验证策略。

【实验结果 / Results】

在维度d=128的Transformer模型上，NANOZK生成每层5.5KB的恒定大小证明（注意力层2.1KB + MLP层3.5KB），验证时间仅24毫秒。与EZKL相比，在d=128时证明大小缩小70倍，证明生成时间加快5.7倍，同时保持形式化可靠性保证（ε < 1e-37）。查找表近似方法完全保留了原始模型的困惑度指标。

【应用价值 / Applications】

该研究为LLM即服务（LLMaaS）场景提供了密码学级别的可信计算保障，使用户能够验证服务商是否使用了承诺的高质量模型，防止模型替换、量化降级或缓存欺骗等攻击。适用于金融、医疗、法律等对模型可信性要求严格的高价值应用场景，为AI服务的透明度和问责制奠定了技术基础。
