---
title: "Beyond Masks: Efficient, Flexible Diffusion Language Models via Deletion-Insertion Processes"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23507"
published: "2026-03-27"
summarized: "2026-03-28T07:12:34.850432"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了删除-插入扩散语言模型（Deletion-Insertion Diffusion, DID），通过将token删除和插入严格建模为离散扩散过程，替代了现有掩码扩散语言模型（MDLMs）中的掩码与解掩码机制。DID消除了MDLMs中两大计算开销来源：非信息性的<MASK>标记和变长设置中的<PAD>标记填充，显著提升了训练与推理效率。实验表明，DID在固定长度和变长设置下均优于MDLM基线和现有基于插入的语言模型，在建模性能、采样质量及速度方面均取得优势，且无需超参数调优。

【方法概述 / Method】
DID将token删除和插入形式化为离散扩散过程，其中删除过程逐步移除token，插入过程逐步构建序列。为训练该模型，作者设计了基于分数的方法为插入操作分配分数，并推导出涉及子序列计数问题的训练目标，通过并行化动态规划算法高效求解。

【实验结果 / Results】
实验显示DID在固定长度和变长设置中均超越MDLM基线及现有插入式语言模型，在模型性能、采样质量和训练/推理速度方面表现更优。特别地，DID天然支持变长序列而无需固定长度填充，且推理过程中具备内在的自纠正机制。

【应用价值 / Applications】
DID的高效性和灵活性使其适用于需要快速、高质量文本生成的场景，如实时对话系统、交互式写作辅助和可变长度内容生成（如代码补全、摘要生成）。其自纠正机制还可提升生成可靠性，减少对后处理的依赖。
