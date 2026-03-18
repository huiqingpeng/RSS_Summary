---
title: "Parallel In-context Learning for Large Vision Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16092"
published: "2026-03-18"
summarized: "2026-03-18T16:10:25.594110"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了并行上下文学习（Parallel-ICL），一种即插即用的推理算法，用于解决大型视觉语言模型（LVLMs）在多模态上下文学习（MM-ICL）中面临的准确率与推理效率之间的权衡问题。该方法将长演示上下文分割为多个短片段并行处理，并通过加权Product-of-Experts（PoE）集成在logit层面融合预测结果。实验表明，Parallel-ICL在VQA、图像描述和分类任务上达到了与完整上下文MM-ICL相当的性能，同时显著提升了推理速度。

【方法概述 / Method】
Parallel-ICL的核心是将长演示上下文划分为多个较短的、可管理的块，利用Transformer的自注意力机制可并行计算的特性，在多个GPU上同时处理这些上下文块。基于集成学习理论，作者提出了两种策略：基于聚类的上下文分块策略以最大化块间多样性，以及基于相似度的上下文编译策略以根据查询相关性加权预测结果。

【实验结果 / Results】
在多个基准测试上的广泛实验表明，Parallel-ICL在保持与完整上下文MM-ICL相当性能的同时，显著降低了推理延迟。具体而言，该方法通过并行处理多个短上下文块，有效规避了Transformer注意力随序列长度二次增长的计算开销，实现了高效的动态任务适应。

【应用价值 / Applications】
Parallel-ICL为需要实时响应的视觉语言应用提供了实用解决方案，如交互式视觉问答、动态图像描述生成和快速视觉分类等场景。该方法使LVLMs能够在资源受限环境下部署更多演示示例以提升任务适应性能，同时大幅降低推理成本，推动了多模态大模型在实际产品中的高效落地。
