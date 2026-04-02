---
title: "Hierarchical Apprenticeship Learning from Imperfect Demonstrations with Evolving Rewards"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00258"
published: "2026-04-02"
summarized: "2026-04-03T07:19:35.759997"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了HALIDE（Hierarchical Apprenticeship Learning from Imperfect Demonstrations with Evolving Rewards），一种层次化学徒学习方法，能够从非最优的学生演示中学习教学策略。该方法的核心创新在于将不完美演示视为结构化信号而非噪声，通过对其相对质量进行排序，并在多层次抽象框架中建模学生行为，从而推断高层意图和策略，同时显式捕捉学生奖励函数的时间演化。实验表明，HALIDE在预测学生教学决策方面优于依赖最优轨迹、固定奖励或未排序不完美演示的现有方法。

【方法概述 / Method】

HALIDE采用层次化学习框架，将学生行为建模为多个抽象层次，从低层动作推断高层策略和意图。方法通过整合演示质量到层次化奖励推断中，区分暂时性错误、次优策略与向高层学习目标的有意义进展，实现对非最优演示的有效利用和奖励函数的动态演化建模。

【实验结果 / Results】

实验结果表明，HALIDE在预测学生教学决策的准确性上显著优于基线方法，包括依赖最优专家轨迹的传统学徒学习、假设固定奖励函数的方法，以及未对不完美演示进行排序处理的对比方法，验证了层次化框架和演化奖励建模的有效性。

【应用价值 / Applications】

该研究对智能教育系统和个性化学习平台具有重要应用价值，能够从真实、非理想化的学生交互数据中自动学习有效的教学策略，适应学生学习过程中的探索、错误和目标演化，为构建更具鲁棒性和适应性的AI教育助手提供了新思路。
