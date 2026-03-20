---
title: "Meanings and Measurements: Multi-Agent Probabilistic Grounding for Vision-Language Navigation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19166"
published: "2026-03-20"
summarized: "2026-03-20T13:21:04.432546"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文揭示了现有视觉语言模型（VLMs）在处理包含度量约束的复杂语义语言查询时存在显著不足。为此，作者提出了MAPG（多智能体概率 grounding）框架，通过将语言查询分解为结构化子组件并概率化组合VLM的grounding结果，实现了在3D空间中度量一致的可执行决策。研究在HM-EQA基准上验证了MAPG的优越性，并发布了专门针对度量-语义目标grounding的新基准MAPG-Bench，同时展示了该方法在真实机器人上的迁移能力。

【方法概述 / Method】
MAPG采用智能体化架构，将复杂的自然语言指令分解为语义引用、空间关系和度量约束等结构化子组件，分别查询VLM进行grounding；随后通过概率推断机制组合各组件的输出，确保最终决策在物理3D空间中满足度量一致性。该框架还依赖结构化场景表示（如3D语义地图）来支撑物理空间中的推理。

【实验结果 / Results】
MAPG在HM-EQA基准上相比强基线方法展现出一致的性能提升；在新提出的MAPG-Bench基准上，该方法专门针对度量-语义grounding任务进行了系统评估，验证了其处理复杂语言查询的优越性；真实机器人实验进一步证明，当结构化场景表示可用时，MAPG能够成功从仿真环境迁移到真实世界。

【应用价值 / Applications】
MAPG可直接应用于人机协作场景中的自然语言指令执行，如家庭服务机器人、仓储物流机器人等需要根据口语化指令（如"走到冰箱右侧两米处"）进行精确导航和操作的领域。该方法填补了现有VLM在物理空间度量推理方面的空白，为构建更可靠、可解释的具身智能系统提供了重要基础，特别是在需要精确空间定位的机器人导航与操作任务中具有显著价值。
