---
title: "VectorWorld: Efficient Streaming World Model via Diffusion Flow on Vector Graphs"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17652"
published: "2026-03-19"
summarized: "2026-03-19T16:22:42.056503"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出VectorWorld，一种面向自动驾驶闭环评估的流式世界模型，通过增量生成以自车为中心的64m×64m车道-智能体矢量图瓦片来解决现有生成式世界模型的三大缺陷：历史无关初始化导致的策略输入不匹配、多步采样延迟违反实时约束、以及长时域运动学不可行性累积。该模型采用运动感知门控VAE实现与历史条件策略的初始化对齐，通过边门控关系DiT配合区间条件MeanFlow和JVP大步监督实现单步实时补全，并引入物理对齐的ΔSim NPC策略稳定长时域推演。在Waymo和nuPlan数据集上，VectorWorld实现了地图结构保真度和初始化有效性的提升，支持稳定实时的1公里以上闭环推演。

【方法概述 / Method】

VectorWorld的核心架构包含三个关键组件：(1) 运动感知门控VAE，通过编码历史运动信息生成与策略兼容的交互状态，解决初始化不匹配问题；(2) 边门控关系扩散Transformer（DiT），采用区间条件MeanFlow训练和基于雅可比向量积（JVP）的大步监督，实现无需数值求解器的单步掩码补全；(3) ΔSim NPC策略，结合混合离散-连续动作与可微运动学logit整形，确保非自车智能体的物理一致性行为。整个系统以流式瓦片方式增量生成矢量图，支持实时外推。

【实验结果 / Results】

在Waymo Open Motion和nuPlan基准上，VectorWorld在地图结构保真度和初始化有效性方面显著优于现有方法，成功支持超过1公里的稳定闭环推演，同时满足实时性约束。消融实验验证了运动感知门控VAE对初始化对齐的贡献、边门控关系DiT的单步生成效率，以及ΔSim策略在长时域稳定性上的关键作用。

【应用价值 / Applications】

VectorWorld可直接应用于自动驾驶系统的闭环策略评估与训练，解决现有仿真器依赖日志回放、无法交互的问题，为端到端驾驶策略的安全验证提供高效平台。其实时流式生成能力也适用于在线决策规划、场景库自动扩充等需要快速交互式仿真的场景，有望降低实车测试成本并加速自动驾驶算法的迭代开发。
