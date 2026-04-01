---
title: "HCLSM: Hierarchical Causal Latent State Machines for Object-Centric World Modeling"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29090"
published: "2026-04-01"
summarized: "2026-04-02T07:15:23.368046"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了HCLSM（层次因果隐状态机），一种面向对象的世界模型架构，通过三大核心原则解决现有世界模型的局限性：基于槽注意力的对象中心分解、结合选择性状态空间模型、稀疏Transformer和压缩Transformer的三层层次化时间动态引擎，以及基于图神经网络的因果结构学习。该模型采用两阶段训练协议，在PushT机器人操作基准上实现了0.008 MSE的下一状态预测损失，并展现出涌现的空间分解能力和学习到的事件边界。研究还开发了自定义Triton内核，使SSM扫描速度相比顺序PyTorch实现提升38倍。

【方法概述 / Method】
HCLSM采用三层次时间动态引擎：选择性状态空间模型（SSM）处理连续物理动态，稀疏Transformer捕捉离散事件，压缩Transformer建模抽象目标；通过槽注意力与空间广播解码实现对象中心分解，并利用图神经网络学习对象间的交互模式。训练分为两阶段：首先通过空间重建损失强制槽专业化，随后进行动态预测训练。

【实验结果 / Results】
在Open X-Embodiment数据集的PushT机器人操作基准上，6800万参数的HCLSM模型达到0.008的下一状态预测MSE损失，空间广播解码（SBD）损失为0.0075；模型展现出涌现的空间分解能力和自动学习到的事件边界。自定义Triton SSM扫描内核实现38倍加速，完整系统包含8,478行Python代码、51个模块和171个单元测试。

【应用价值 / Applications】
HCLSM可应用于机器人操作任务中的未来状态预测与规划，其对象中心表示和因果结构学习能力有助于提升机器人在复杂动态环境中的决策可靠性；层次化多尺度时间建模使其适用于需要同时处理物理连续动态、离散事件和长期目标规划的强化学习与控制场景，为具身智能系统提供了更可解释、更结构化的世界建模方案。
