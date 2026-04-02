---
title: "WARP: Guaranteed Inner-Layer Repair of NLP Transformers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00938"
published: "2026-04-02"
summarized: "2026-04-03T07:26:20.962260"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出WARP（Weight-Adjusted Repair with Provability），一种约束驱动的Transformer修复框架，突破了现有修复方法仅局限于最后一层的限制。WARP将对数几率差距的一阶线性化转化为凸二次规划问题，实现了高维参数空间上的可追踪优化。该方法在保持一阶近似成立的条件下，为每个样本提供三项保证：正边界约束、保留集约束和基于Lipschitz连续性的认证鲁棒半径。实验表明，WARP能够在实际中兑现这些理论保证，同时提升模型对对抗样本的鲁棒性。

【方法概述 / Method】

WARP的核心方法是将Transformer修复重新表述为凸二次规划问题，通过对logit差距进行一阶线性化处理，使得优化问题在多层参数空间上可解。为确保可行性，论文引入基于敏感度的预处理步骤来调节优化 landscape，并设计了迭代优化过程，在温和假设下收敛至满足所有修复约束的解。

【实验结果 / Results】

作者在多种层结构的仅编码器Transformer上进行了实证评估，验证了WARP的理论保证在实践中成立。修复后的模型在对抗输入上表现出 improved robustness，同时成功维持了保留集上的性能，表明该方法能够在扩展参数搜索空间的同时实现可验证的、可泛化的修复。

【应用价值 / Applications】

WARP适用于需要高可靠性保证的NLP应用场景，如金融文本分析、医疗诊断系统和法律文档处理等安全关键领域。该方法为部署Transformer模型提供了形式化验证能力，使模型所有者能够在发现漏洞后进行可证明的局部修复，而无需完全重新训练，显著降低了模型维护成本并增强了部署信心。
