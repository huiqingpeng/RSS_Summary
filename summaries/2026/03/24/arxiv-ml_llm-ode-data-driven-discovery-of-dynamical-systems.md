---
title: "LLM-ODE: Data-driven Discovery of Dynamical Systems with Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20910"
published: "2026-03-24"
summarized: "2026-03-25T07:15:55.741764"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 LLM-ODE，一种利用大语言模型（LLM）辅助发现动力系统控制方程的新框架。该方法通过从精英候选方程中提取模式来指导符号进化，从而克服传统遗传编程（GP）在符号搜索空间中探索效率低下的问题。在 91 个动力系统上的实验表明，LLM-ODE 在搜索效率和帕累托前沿质量方面均优于经典 GP 方法，且相比纯线性或 Transformer 方法具有更好的高维系统可扩展性。

【方法概述 / Method】

LLM-ODE 将大语言模型的生成先验与进化算法相结合，利用 LLM 从优质候选解中学习和提取符号模式，生成更有信息量的搜索轨迹，同时保留进化算法的探索能力。该框架通过 LLM 引导的符号变异和重组操作，实现对复杂符号搜索空间的高效导航。

【实验结果 / Results】

在涵盖 91 个动力系统的基准测试中，LLM-ODE 的各类变体在搜索效率和帕累托前沿质量上均一致性地超越传统 GP 方法。此外，该方法在高维系统上的可扩展性显著优于纯线性方法和仅基于 Transformer 的模型发现方法，实现了效率与准确性的双重提升。

【应用价值 / Applications】

LLM-ODE 可广泛应用于物理学、生物学、化学等领域中复杂动力系统的自动建模与方程发现，加速科学知识的自动化提取。其数据驱动的特性使其特别适用于实验数据丰富但理论模型未知的场景，为科学研究提供高效、可解释的自动化工具。
