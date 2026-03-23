---
title: "Optimizing Resource-Constrained Non-Pharmaceutical Interventions for Multi-Cluster Outbreak Control Using Hierarchical Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19397"
published: "2026-03-23"
summarized: "2026-03-24T07:18:13.924901"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对资源受限的非药物干预措施（NPIs）在多集群疫情爆发控制中的优化问题，提出了一种分层强化学习框架。该框架将问题建模为约束性不安定多臂老虎机（constrained restless multi-armed bandit），通过全局控制器学习连续动作成本乘数来调节全局资源需求，同时利用局部策略估计每个集群内资源分配的边际价值。在基于SARS-CoV-2的真实代理仿真器中，该方法在多种系统规模和检测预算下均优于基线方法，疫情控制效果提升20%-30%，且支持多达40个并发活跃集群的高效决策。

【方法概述 / Method】
论文采用分层强化学习架构，包含两个核心组件：上层全局控制器输出连续成本乘数以动态调整资源分配总量，下层广义局部策略网络评估个体层面的资源分配边际收益。该方法通过将组合优化问题解耦为全局预算调控与局部分配决策，有效处理异步到达、规模异质的动态集群场景。

【实验结果 / Results】
实验基于真实SARS-CoV-2传播动力学构建的代理仿真器，测试了不同系统规模（最多40个并发集群）和检测预算配置。结果表明，所提方法相比RMAB启发式和启发式基线，在疫情控制有效性指标上稳定提升20%-30%，同时决策速度显著优于RMAB方法，展现出良好的可扩展性。

【应用价值 / Applications】
该研究为公共卫生应急响应提供了可扩展的智能决策工具，特别适用于早期疫情阶段检测资源稀缺、多传播链并发的场景。方法可推广至流感、新兴传染病等需要快速、公平分配有限NPI资源的疫情管控实践，辅助公共卫生部门优化检测隔离策略的实时部署。
