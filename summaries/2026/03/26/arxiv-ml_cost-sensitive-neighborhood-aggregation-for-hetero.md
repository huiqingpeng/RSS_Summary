---
title: "Cost-Sensitive Neighborhood Aggregation for Heterophilous Graphs: When Does Per-Edge Routing Help?"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24291"
published: "2026-03-26"
summarized: "2026-03-27T07:22:49.480345"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文区分了图神经网络中的两种异质性（heterophily）机制：对抗性异质性（cross-class edges损害分类信号）和信息性异质性（异质性结构本身携带有用信号）。作者提出成本敏感邻域聚合（CSNA）方法，通过学习的投影空间中的成对距离实现per-edge软路由，将消息分别通过concordant和discordant通道进行独立变换。理论分析和实验结果表明，per-edge路由仅在对抗性异质性场景下有效，而在信息性异质性场景下反而无益，这一模式本身即构成重要发现。

【方法概述 / Method】
CSNA层首先在学习到的投影空间中计算节点间的成对距离，然后基于该距离对每条边进行软路由（soft-route），将消息分别送入concordant（同类）和discordant（异类）两个独立变换通道。该方法通过成本敏感加权机制，在理论上保证当$w_+/w_- > q/p$时能够保留类别判别信号，而均值聚合会衰减该信号。

【实验结果 / Results】
在六个标准基准数据集上，CSNA在对抗性异质性数据集（Texas、Wisconsin、Cornell、Actor）上与最先进方法具有竞争力，但在信息性异质性数据集（Chameleon、Squirrel）上表现较差。这一对比模式验证了核心假设：当成本函数能够有效分离边类型时（对抗性场景），细粒度路由才有价值；反之，统一频谱通道已足够。

【应用价值 / Applications】
该研究为GNN架构设计提供了诊断工具：通过评估成本函数分离边类型的能力，可预判per-edge路由是否值得部署，避免在不适用的场景下引入不必要的计算开销。这对于图分类任务的模型选择和异质性图数据的预处理策略具有直接指导意义，尤其在社交网络、引文网络等异质性结构普遍存在的领域。
