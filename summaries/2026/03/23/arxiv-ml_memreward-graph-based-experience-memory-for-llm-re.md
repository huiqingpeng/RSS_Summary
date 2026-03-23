---
title: "MemReward: Graph-Based Experience Memory for LLM Reward Prediction with Limited Labels"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19310"
published: "2026-03-23"
summarized: "2026-03-24T07:16:34.423773"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MemReward，一种基于图结构经验记忆的框架，用于解决大型语言模型（LLM）强化学习微调中奖励标签稀缺的问题。该方法通过将查询、思考过程和答案构建为异构图，利用图神经网络（GNN）在标注节点上训练并将奖励传播到未标注样本，实现了在有限标签条件下的高效奖励预测。实验表明，仅使用20%标签时，MemReward在Qwen2.5-3B和1.5B模型上分别达到Oracle性能的97.3%和96.6%，在70%标签时可达99.4%，且在域外任务上超越Oracle表现。

【方法概述 / Method】
MemReward采用异构图神经网络架构，将LLM生成的推理轨迹（包含查询、思考过程、最终答案）建模为图节点，通过相似性边和结构边连接相关节点。框架首先用初始策略生成rollout并存储为经验记忆，随后利用少量标注节点训练GNN进行奖励预测，通过消息传递机制将奖励信号传播至未标注节点，支持在线优化过程中的持续学习。

【实验结果 / Results】
在Qwen2.5-3B和1.5B模型上的数学推理、问答和代码生成任务中，MemReward展现出显著的标签效率：20%标签即可达到近Oracle性能，且性能随标签预算平滑提升。尤为突出的是，该方法在域外任务上表现优于全监督Oracle，表明图结构记忆有效促进了跨任务知识迁移和泛化能力的提升。

【应用价值 / Applications】
MemReward适用于奖励标注成本高昂的场景，如数学证明验证、开放式问答和复杂代码生成等需要专家知识或缺乏明确 ground truth 的领域。该方法可大幅降低人工标注需求，使强化学习微调在资源受限条件下更具可行性，为LLM在专业化、高成本领域的部署提供了经济高效的解决方案。
