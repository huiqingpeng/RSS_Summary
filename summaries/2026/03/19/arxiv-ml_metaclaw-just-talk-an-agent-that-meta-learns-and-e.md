---
title: "MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17187"
published: "2026-03-19"
summarized: "2026-03-19T12:08:37.239927"
ai_provider: "openai"
---

【论文摘要 / Abstract】
MetaClaw 是一个面向大型语言模型智能体的持续元学习框架，解决了部署后智能体静态化、无法适应用户需求演变的问题。该框架通过技能驱动的快速适应机制和机会主义策略优化机制，实现零停机时间的智能体能力进化。实验表明，MetaClaw 在 MetaClaw-Bench 和 AutoResearchClaw 基准上分别实现最高 32% 的相对准确率提升，并将 Kimi-K2.5 的准确率从 21.4% 提升至 40.6%，复合鲁棒性提高 18.3%。

【方法概述 / Method】
MetaClaw 采用双机制协同设计：技能驱动快速适应通过 LLM 进化器分析失败轨迹并合成新技能，实现即时改进；机会主义策略优化则通过云端 LoRA 微调和基于过程奖励模型的强化学习（RL-PRM）进行梯度更新，由机会主义元学习调度器（OMLS）在用户非活跃窗口触发。两种机制相互强化：优化后的策略生成更高质量轨迹用于技能合成，而丰富的技能库为策略优化提供更优数据。

【实验结果 / Results】
在 MetaClaw-Bench 和 AutoResearchClaw 上的评估显示，仅技能驱动适应即可带来最高 32% 的相对准确率提升；完整流程将 Kimi-K2.5 的准确率从 21.4% 大幅提升至 40.6%，同时复合鲁棒性指标提高 18.3%。版本控制机制有效隔离支持数据与查询数据，防止数据污染。

【应用价值 / Applications】
MetaClaw 适用于需要 7×24 小时持续服务且任务分布动态变化的生产环境，如 OpenClaw 等多渠道智能体平台。其代理架构支持在生产级大模型上扩展而无需本地 GPU，为金融客服、研究助手、企业自动化等场景提供了可进化、零停机的智能体部署方案。
