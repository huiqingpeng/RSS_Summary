---
title: "RTLSeek: Boosting the LLM-Based RTL Generation with Multi-Stage Diversity-Oriented Reinforcement Learning"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.27630"
published: "2026-03-31"
summarized: "2026-04-01T07:16:07.965723"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了RTLSeek，一种基于多阶段多样性导向强化学习的后训练范式，用于提升大语言模型生成寄存器传输级（RTL）硬件设计代码的能力。针对现有方法因高质量可验证数据稀缺而导致的准确性和多样性不足问题，RTLSeek通过规则化的多样性导向强化学习，结合专家知识与电子设计自动化（EDA）反馈，实现了RTL正确性与多样性的双重提升。实验表明，该方法在RTLLM基准上超越现有方法，并验证了"生成越多、效果越好"的设计原则。

【方法概述 / Method】
RTLSeek采用三阶段训练框架，通过多样性中心的多目标奖励调度机制整合专家知识与EDA工具反馈。核心方法包括基于规则的多样性导向强化学习（Diversity-Oriented RL），鼓励模型在设计空间中进行更广泛的探索，而非仅生成单一实现方案。

【实验结果 / Results】
在RTLLM基准测试上的实验表明，RTLSeek显著优于现有方法；消融实验进一步证实，鼓励更广泛的设计空间探索能够有效提升RTL代码质量，并实现了生成数量与结果质量正相关的"生成越多、效果越好"现象。

【应用价值 / Applications】
该研究可应用于自动化硬件设计流程，帮助工程师从高级规格快速生成多样化、可验证的Verilog实现方案，满足不同设计目标（如面积、功耗、时序）的优化需求。开源的框架、数据集、代码和模型权重有助于推动LLM辅助芯片设计的研究与工业落地。
