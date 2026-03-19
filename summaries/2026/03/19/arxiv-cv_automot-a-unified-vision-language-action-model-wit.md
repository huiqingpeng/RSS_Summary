---
title: "AutoMoT: A Unified Vision-Language-Action Model with Asynchronous Mixture-of-Transformers for End-to-End Autonomous Driving"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.14851"
published: "2026-03-19"
summarized: "2026-03-19T17:04:15.663166"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了AutoMoT，一个端到端自动驾驶框架，将推理与动作生成统一在单一的视觉-语言-动作（VLA）模型中。该研究解决了现有视觉语言模型集成策略中的三大问题：推理与动作空间的分布不对齐、预训练VLM通用推理能力利用不足、以及动作策略生成时的高推理延迟。实验表明，AutoMoT在开放环和封闭环设置下均达到最先进的性能，同时揭示了预训练VLM在自动驾驶中的功能边界——语义提示即可实现多任务场景理解，但动作级任务仍需微调。

【方法概述 / Method】
AutoMoT采用混合Transformer（MoT）架构，通过联合注意力共享机制保留预训练VLM的通用推理能力，并支持不同任务频率下的异步快慢推理。该架构实现了推理模块（低频）与动作生成模块（高频）的解耦执行，从而在保持模型统一性的同时降低推理延迟。

【实验结果 / Results】
在多个基准测试的开放环和封闭环评估中，AutoMoT与现有最先进方法相比具有竞争力。研究还发现，仅通过语义提示，预训练VLM即可在场景理解任务上表现优异，但在决策和轨迹规划等动作级任务上，针对性的微调仍然不可或缺。

【应用价值 / Applications】
AutoMoT为端到端自动驾驶系统提供了一种高效统一的VLA解决方案，适用于需要实时决策与规划的智能驾驶场景。该研究对预训练VLM能力边界的分析也为自动驾驶模型的设计提供了重要指导，有助于优化计算资源分配和模型部署策略。
