---
title: "REST: Receding Horizon Explorative Steiner Tree for Zero-Shot Object-Goal Navigation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18624"
published: "2026-03-20"
summarized: "2026-03-20T16:09:13.111124"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对零样本物体目标导航（ZSON）任务，提出现有免训练分层方法在"选项"（option）设计上的关键缺陷——将子目标候选简化为独立评分的孤立路点。作者的核心洞见是：选项空间应构建为**路径树结构**，以暴露沿途信息增益并支持大语言模型（LLM）的粗到精推理。基于此提出的REST框架，在Gibson、HM3D和HSSD基准上实现了成功率与路径效率的最佳平衡。

【方法概述 / Method】
REST框架包含三个核心组件：（1）从在线RGB-D流构建显式开放词汇3D地图；（2）通过基于采样的规划生成以智能体为中心的安全且信息丰富的路径树作为选项空间；（3）将每个分支文本化为空间叙事，并通过思维链LLM推理选择最优路径。该设计利用斯坦纳树（Steiner Tree）思想压缩组合路径空间，实现递推视野（Receding Horizon）的探索规划。

【实验结果 / Results】
在Gibson、HM3D和HSSD三大基准测试中，REST在成功率上持续位居前列，同时在路径效率指标上取得最佳或次佳表现。这表明该框架成功实现了探索效率与任务成功率之间的有利权衡，验证了路径树结构相比孤立路点评分的优越性。

【应用价值 / Applications】
REST为家庭服务机器人、仓储物流机器人等需要在未知环境中自主搜索目标物体的应用场景提供了高效且无需任务特定训练的解决方案。其开放词汇3D建图与LLM推理的结合，也适用于需要自然语言指令理解和语义导航的通用具身智能系统。
