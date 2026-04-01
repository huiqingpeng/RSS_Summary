---
title: "ARCS: Autoregressive Circuit Synthesis with Topology-Aware Graph Attention and Spec Conditioning"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.29068"
published: "2026-04-01"
summarized: "2026-04-02T07:11:48.456437"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出ARCS系统，一种用于摊销式模拟电路生成的方法，可在毫秒级时间内生成完整的SPICE可仿真电路设计（拓扑结构和元件参数），相比基于搜索的方法（需数分钟）实现数量级加速。该系统采用混合流水线（图VAE+流匹配模型）结合SPICE排序，在32种拓扑上仅用8次SPICE仿真即达到99.9%仿真有效率和6.43/8.0的奖励分数，比遗传算法减少40倍仿真次数。核心技术创新是Group Relative Policy Optimization（GRPO），通过每拓扑优势归一化解决了REINFORCE的跨拓扑奖励分布失配问题，仅用500步RL训练即提升9.6个百分点仿真有效率。

【方法概述 / Method】
ARCS采用自回归生成框架，结合拓扑感知图注意力机制将电路表示为序列化token，并通过语法约束解码确保100%结构有效性。训练阶段使用GRPO强化学习算法，对每个拓扑组独立计算相对优势以稳定多拓扑联合训练；推理阶段采用混合流水线（图VAE生成候选拓扑→流匹配模型采样元件值→SPICE仿真排序）或单模型拓扑感知图Transformer配合Best-of-3选择策略。

【实验结果 / Results】
混合流水线在32种拓扑上达到99.9%仿真有效率和6.43/8.0奖励，仅需8次SPICE评估；单模型推理在97ms内达到85%仿真有效率，比随机搜索快600倍以上。GRPO相比REINFORCE在仅500步（10倍更少）内提升仿真有效率9.6个百分点。作为搜索方法的暖启动，ARCS可用49%更少仿真次数恢复遗传算法96.6%的设计质量（5.48 vs 7.48奖励）。

【应用价值 / Applications】
ARCS的>1000倍加速优势适用于模拟电路快速原型设计、大规模设计空间探索和搜索方法暖启动，显著降低模拟电路设计迭代周期。尽管单设计质量尚未超越传统搜索优化，但其高效率使其成为交互式设计工具和自动化EDA流程中的实用组件，可与传统优化方法形成互补。
