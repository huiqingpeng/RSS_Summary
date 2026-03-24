---
title: "Structural Sensitivity in Compressed Transformers: Error Propagation, Lyapunov Stability, and Formally Verified Bounds"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20991"
published: "2026-03-24"
summarized: "2026-03-25T07:17:21.967445"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究揭示了Transformer模型压缩中的结构性敏感度差异：GPT-2 Small中单个矩阵的压缩可导致困惑度激增20,000倍，而敏感度跨越五个数量级。作者发现早期层MLP上投影矩阵具有灾难性敏感度，而值投影矩阵几乎可免费压缩，且该层级结构在多种架构、压缩率和评估规模下保持稳定。研究结合Lyapunov稳定性理论与形式化验证（Lean 4），首次为Transformer压缩误差提供了机器检验的严格边界。

【方法概述 / Method】
研究采用Lyapunov稳定性理论分析残差连接对压缩误差的收缩机制，证明隐藏状态增长速率超过误差增长时误差会被抑制；同时建立形式化验证框架，使用Lean 4证明语言开发了10个无"sorry"标记的机器检验定理，为每个矩阵的压缩误差提供严格数学边界。

【实验结果 / Results】
在五个架构（117M-8B参数）上的实验表明，早期层MLP上投影的压缩敏感度最高，而值投影敏感度最低；形式化验证的边界在14,040+种配置中零违反；混合架构LFM2-2.6B尽管误差放大更高，但因架构冗余仅退化7倍，而完全收缩的GPT-2 Small退化达120倍。下游任务评估（HellaSwag等）和激活感知剪枝进一步验证了发现。

【应用价值 / Applications】
研究提出的"压缩脆弱性指数"可量化排序模型鲁棒性，指导模型压缩策略的制定，优先保护高敏感度矩阵；形式化验证框架为神经网络压缩的安全性关键应用（如边缘部署、实时系统）提供了可证明的保证，降低部署风险。
