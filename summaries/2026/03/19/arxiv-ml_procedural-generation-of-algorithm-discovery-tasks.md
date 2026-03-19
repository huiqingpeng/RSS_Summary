---
title: "Procedural Generation of Algorithm Discovery Tasks in Machine Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17863"
published: "2026-03-19"
summarized: "2026-03-19T12:17:31.342267"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了 DiscoGen，一个用于机器学习算法发现任务的程序化生成器，能够生成数百万个涵盖不同难度、复杂度和机器学习领域的任务（如强化学习优化器、图像分类损失函数等）。为克服现有任务套件在评估方法、数据污染和任务饱和等方面的局限，作者同时发布了 DiscoBench 基准测试集，用于对算法发现智能体（ADAs）进行原则性评估，并通过提示优化实验展示了 DiscoGen 的实际应用。

【方法概述 / Method】
DiscoGen 采用程序化生成方法，通过少量配置参数即可生成多样化的算法发现任务，其设计灵感来源于强化学习中程序化生成的成功经验。该系统覆盖多个机器学习子领域，任务难度和复杂度可灵活调节，支持对算法发现智能体进行大规模训练和评估。

【实验结果 / Results】
论文展示了 DiscoGen 在提示优化场景下的应用实验，验证了该系统能够有效支持算法发现智能体的开发与优化。通过 DiscoBench 固定子集，研究者可对 ADAs 进行可复现、无数据污染的原则性性能评估。

【应用价值 / Applications】
DiscoGen 为自动化机器学习算法开发提供了可扩展的测试平台，可加速优化器、损失函数等核心组件的自动发现。其开源特性（已发布代码）支持学术界和工业界开展算法发现智能体的系统性研究，推动 AutoML 领域的突破性进展。
