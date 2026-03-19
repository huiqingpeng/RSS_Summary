---
title: "HoloByte: Continuous Hyperspherical Distillation for Tokenizer-Free Modeling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16917"
published: "2026-03-19"
summarized: "2026-03-19T12:05:41.168726"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出 **HoloByte**，一种严格无分词器的序列建模框架，通过连续超球面蒸馏（Continuous Hyperspherical Distillation）解决字节级注意力计算复杂度与离散分词带来的优化不连续性问题。该方法将字节序列投影到连续有界超球面流形，使Transformer在压缩连续表示上运算，将精确注意力复杂度从 $\mathcal{O}(N^2D)$ 降至 $\mathcal{O}(N^2D/W^2 + ND^2)$。理论分析证明了无误差离散恢复所需的最小嵌入维度，实验表明在严格匹配参数条件下，HoloByte 系统性地优于BPE基线。

【方法概述 / Method】

HoloByte 采用**可逆保维正交旋转算子**将离散字节分块投影到连续超球面流形，实现空间叠加压缩；宏观Transformer仅在此连续流形上运算，再通过**局部因果微解码器**解绑表示以计算精确字节级分布。训练采用**双目标公式**，包含严格梯度有界的全息潜变量均方误差，保证渐近稳定性。

【实验结果 / Results】

在严格匹配的参数约束下，HoloByte 系统性地优于可比较的离散BPE基线模型；理论推导得出确保无误差离散恢复的最小嵌入维度为 $D = \Omega(W \ln |\mathcal{V}|)$，其中 $W$ 为块容量，$|\mathcal{V}|$ 为字节词汇表大小（通常为256）。

【应用价值 / Applications】

HoloByte 为**词汇表无关的序列建模**提供了数学严谨且计算可扩展的基础，适用于多语言处理、低资源语言建模、音频/图像等原生连续数据的统一建模，以及需要避免分词引入的形态学偏差和跨语言迁移障碍的场景。
