---
title: "WIST: Web-Grounded Iterative Self-Play Tree for Domain-Targeted Reasoning Improvement"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22352"
published: "2026-03-25"
summarized: "2026-03-26T07:13:25.148853"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出WIST（Web-Grounded Iterative Self-Play Tree），一种面向特定领域的推理改进框架，通过直接从开放网络学习而无需预整理的领域语料库。WIST通过增量式领域树扩展进行探索，检索并清洗路径一致的网页语料构建可控训练环境，然后执行带可验证奖励的Challenger-Solver自博弈，并将可学习性信号反馈更新节点后验以指导后续探索。在四个主干模型上，WIST相比基线模型取得显著提升，Qwen3-4B-Base和OctoThinker-8B的整体增益分别达到+9.8和+9.7，且在医学领域和物理推理任务上展现出良好的领域可操控性。

【方法概述 / Method】

WIST采用三阶段迭代流程：首先基于当前领域树节点检索网络语料并清洗构建训练环境；然后在该环境上执行Challenger（生成难题）与Solver（解决问题）的自博弈，利用可验证奖励进行强化学习；最后根据训练信号更新节点后验分布，通过自适应课程学习指导下一轮的树扩展方向，形成"探索-学习-反馈"的闭环。

【实验结果 / Results】

WIST在四个不同规模的主干模型上均实现一致提升，显著优于纯内生自进化和基于固定语料库的自博弈基线方法。具体而言，Qwen3-4B-Base获得+9.8的整体增益，OctoThinker-8B获得+9.7；领域针对性实验中，Qwen3-8B-Base在医学领域提升+14.79，Qwen3-4B-Base在PhyBench物理推理基准上提升+5.28。消融实验验证了网络检索、路径一致性清洗和自适应课程等关键组件的重要性。

【应用价值 / Applications】

WIST适用于需要快速适配特定专业领域（如医学、物理学、法律等）的推理场景，无需昂贵的领域专家标注或预构建语料库，可直接利用开放网络资源实现模型的自我提升。该方法为构建可领域定制、成本可控的大型语言模型持续学习系统提供了实用路径，特别适合资源受限但需要专业推理能力的应用场景。
