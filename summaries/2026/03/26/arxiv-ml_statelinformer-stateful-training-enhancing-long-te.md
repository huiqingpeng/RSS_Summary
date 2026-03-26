---
title: "StateLinFormer: Stateful Training Enhancing Long-term Memory in Navigation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23571"
published: "2026-03-26"
summarized: "2026-03-27T07:14:58.158961"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了StateLinFormer，一种用于导航任务的线性注意力模型，通过状态化训练机制（stateful training）解决现有方法在长期记忆方面的局限。该模型在训练过程中保留跨批次边界的循环记忆状态，而非重新初始化，从而近似实现无限长序列的学习。实验表明，StateLinFormer在MAZE和ProcTHOR环境中显著优于无状态线性注意力模型和标准Transformer基线，且随着交互长度增加，其上下文依赖适应能力持续提升，展现出增强的上下文学习能力（ICL）。

【方法概述 / Method】
StateLinFormer采用线性注意力机制作为基础架构，核心创新在于状态化训练范式：在训练时将连续数据分段处理，但保留前一段的隐藏记忆状态作为下一段的初始状态，而非传统的批次独立训练。这种方法使模型能够在训练过程中维持跨片段的持久记忆状态，有效模拟无限长序列的依赖关系学习。

【实验结果 / Results】
在MAZE和ProcTHOR导航环境中，StateLinFormer显著超越其无状态版本（stateless counterpart）和固定上下文窗口的标准Transformer基线。关键发现表明，随着交互时长的增加，状态化训练带来的上下文依赖适应能力提升愈发明显，证实了该方法在长期记忆保持方面的优势。

【应用价值 / Applications】
该研究适用于需要长期记忆和持续适应的交互式导航场景，如自主机器人探索、智能体长期任务执行等。状态化训练机制可推广至其他需要处理超长序列的Transformer应用，为提升大语言模型和视觉导航模型的上下文学习能力提供新思路。
