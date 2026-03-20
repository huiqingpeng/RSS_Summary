---
title: "BeamAgent: LLM-Aided MIMO Beamforming with Decoupled Intent Parsing and Alternating Optimization for Joint Site Selection and Precoding"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18855"
published: "2026-03-20"
summarized: "2026-03-20T13:16:56.486852"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出BeamAgent，一种LLM辅助的MIMO波束成形框架，通过将语义意图解析与数值优化显式解耦，解决了现有方法将LLM紧密耦合于物理层计算所导致的精度不足问题。该框架利用LLM将自然语言描述转换为结构化空间约束，再由专用梯度优化器联合求解离散基站选址与连续预编码设计。在基于射线追踪的城市MIMO场景实验中，BeamAgent在相同暗区约束下实现84.0 dB亮区功率，较穷举零迫方法提升7.1 dB，端到端系统性能距专家上界仅3.3 dB，且完整优化可在笔记本电脑上2秒内完成。

【方法概述 / Method】

BeamAgent采用"解耦式"架构：LLM仅作为语义翻译器，通过场景感知提示实现无需微调的空间推理，将自然语言指令转化为结构化的亮区/暗区空间约束；数值优化部分则采用交替优化算法，联合处理离散基站选址与连续预编码矩阵设计，并引入基于惩罚的损失函数在强制暗区功率约束的同时释放自由度以最大化亮区增益。系统还包含多轮交互机制与双层意图分类模块以确保约束验证的鲁棒性。

【实验结果 / Results】

在射线追踪构建的城市MIMO场景验证中，BeamAgent达到84.0 dB亮区功率，相比穷举零迫基准提升7.1 dB；端到端系统性能与理论专家上界差距仅为3.3 dB；完整优化流程在普通笔记本电脑上执行时间低于2秒，展现出优异的实时性与实用性。

【应用价值 / Applications】

该研究为6G智能无线通信网络提供了自然语言驱动的波束成形新范式，使非专业用户可通过直观语言指令操控复杂的MIMO系统，适用于应急通信、动态覆盖调整、军事通信等需要快速重构波束形状的场景；其"LLM语义解析+专用数值优化"的解耦架构也为其他物理层优化问题（如资源分配、功率控制）的智能化提供了可迁移的方法论参考。
