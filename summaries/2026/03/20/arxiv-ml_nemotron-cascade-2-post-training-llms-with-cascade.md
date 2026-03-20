---
title: "Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19220"
published: "2026-03-20"
summarized: "2026-03-20T13:21:53.354437"
ai_provider: "openai"
---

【论文摘要 / Abstract】
Nemotron-Cascade 2 是一个开源的300亿参数MoE模型（仅激活30亿参数），在推理和智能体能力方面达到同类最优水平，数学和编程推理性能接近前沿开源模型。该模型是第二个在2025年国际数学奥林匹克（IMO）、国际信息学奥林匹克（IOI）和ICPC世界总决赛中均获得金牌级表现的开源权重LLM，参数规模仅为同类模型的1/20，展现出极高的智能密度。核心技术突破包括：在精心筛选的SFT数据集基础上，大幅扩展Cascade RL覆盖更广泛的推理和智能体领域；并引入多领域在线策略蒸馏，从各领域的最强中间教师模型中学习，以高效恢复基准回归并持续获得性能提升。

【方法概述 / Method】
论文采用三阶段后训练流程：首先基于精心筛选的数据集进行监督微调（SFT）；随后大幅扩展Cascade强化学习方法，覆盖数学推理、代码生成、智能体任务等更广泛领域；最关键的是在Cascade RL过程中引入多领域在线策略蒸馏（multi-domain on-policy distillation），针对不同领域动态选择最强的中间检查点作为教师模型进行知识迁移。

【实验结果 / Results】
Nemotron-Cascade 2在2025年IMO、IOI和ICPC三大国际顶级竞赛中均达到金牌级表现，成为继DeepSeekV3.2-Speciale-671B-A37B之后第二个达成此成就的开源模型；尽管仅激活30亿参数（总参数300亿），其数学和代码推理能力可媲美参数量大20倍的前沿模型，验证了极高的参数效率。

【应用价值 / Applications】
该模型为资源受限场景提供了高性能AI解决方案，可在边缘设备或低成本推理基础设施上部署企业级数学推理、代码生成和智能体系统；开源权重和训练数据的发布为研究社区提供了可复现的高效大模型训练范式，特别适用于需要平衡性能与部署成本的教育、科研和工业应用场景。
