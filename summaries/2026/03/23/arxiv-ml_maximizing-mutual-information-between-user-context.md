---
title: "Maximizing mutual information between user-contexts and responses improve LLM personalization with no additional data"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19294"
published: "2026-03-23"
summarized: "2026-03-24T07:15:26.172287"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了**互信息偏好优化（MIPO）**，一种无需额外标注数据或外部验证器的自改进框架。MIPO通过对比数据增强构建偏好对：基于正确提示生成正样本响应，基于随机无关提示生成负样本响应，并使用DPO优化以最大化用户上下文与响应之间的点条件互信息。实验表明，MIPO在个性化任务上实现3-40%的提升，且 surprisingly 在数学和多选题任务上也能获得1-18%的改进，完全无需额外数据或人工监督。

【方法概述 / Method】

MIPO是一种对比式数据增强方法，核心在于构造合成偏好对：正样本为模型在给定正确用户上下文下的生成响应，负样本为模型在随机采样无关提示下的生成响应。通过DPO训练，该方法理论上等价于最大化基础语言模型下的点条件互信息 $I(\text{response}; \text{context} | \text{base model})$，从而增强模型捕捉和利用用户特定上下文的能力。

【实验结果 / Results】

在多种规模的Llama和Qwen-Instruct模型上的实证结果显示：在真实用户数据集（如Anthropic Helpfulness、OpenAssistant对话）的个性化任务中，MIPO相比强基线取得3-40%的相对提升；更令人意外的是，该方法无需任何数学专用数据即可在GSM8K数学推理和MMLU多选题任务上获得1-18%的准确率提升，证明了最大化互信息作为一种通用自改进机制的有效性。

【应用价值 / Applications】

MIPO为LLM自我改进提供了一条不依赖昂贵人工标注或外部验证器的新路径，特别适用于个性化对话系统、推荐系统等需要深度理解用户上下文的场景。其"无额外数据"特性使其在数据稀缺领域（如垂直行业、低资源语言）具有重要价值，同时揭示的互信息最大化原则可能启发更广泛的自监督学习范式。
