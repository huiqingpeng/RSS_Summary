---
title: "PEANUT: Perturbations by Eigenvalue Alignment for Attacking GNNs Under Topology-Driven Message Passing"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26136"
published: "2026-03-30"
summarized: "2026-03-31T07:22:10.122790"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文揭示了图神经网络（GNNs）在利用图拓扑结构（邻接矩阵或拉普拉斯矩阵）进行消息传递时的核心脆弱性，并提出了PEANUT攻击方法。PEANUT是一种简单、无梯度、受限黑盒的对抗攻击，通过在推理阶段注入虚拟节点来破坏GNN性能，无需迭代优化、参数学习或训练替代模型。实验表明，即使注入特征为零的节点，仅通过精心设计的连接关系也能显著降低GNN在三个图任务上的性能。

【方法概述 / Method】
PEANUT基于特征值对齐（Eigenvalue Alignment）原理，通过分析目标图的特征谱结构，计算使扰动最大化的虚拟节点连接模式。该方法无需访问模型参数或梯度信息，仅利用图的拓扑特征即可确定最优的注入节点连接方式，实现了完全非迭代的即时攻击生成。

【实验结果 / Results】
在多个真实数据集上的实验表明，PEANUT在节点分类、图分类和链接预测三个任务上均能有效降低GNN性能。尽管方法极其简单（无梯度计算、无特征要求），其攻击成功率与需要大量计算资源的复杂攻击方法相当，且推理阶段即时生效的特点使其具有显著的时间效率优势。

【应用价值 / Applications】
该研究对GNN安全部署具有重要警示意义，特别是在金融风控、推荐系统等需要防范恶意注入攻击的场景。PEANUT揭示了拓扑驱动型GNN对结构扰动的本质脆弱性，为设计更鲁棒的GNN架构提供了理论依据，同时也可用于安全测试和模型鲁棒性评估。
