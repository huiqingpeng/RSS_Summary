---
title: "MemGuard-Alpha: Detecting and Filtering Memorization-Contaminated Signals in LLM-Based Financial Forecasting via Membership Inference and Cross-Model Disagreement"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26797"
published: "2026-03-31"
summarized: "2026-04-01T07:18:23.512087"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文揭示了大型语言模型（LLMs）在金融预测中存在记忆污染问题——LLMs会记忆训练语料中的历史金融数据，导致产生虚假的样本内预测准确性，但在样本外测试中崩溃。作者提出MemGuard-Alpha框架，首次实现了零成本的信号级实时过滤，通过成员推理攻击和跨模型分歧检测，有效分离记忆污染信号与真实推理信号，解决了记忆诱导的前视偏差威胁。

【方法概述 / Method】

MemGuard-Alpha包含两个核心算法：（i）MemGuard复合评分（MCS），将五种成员推理攻击（MIA）方法与时序邻近特征通过逻辑回归组合，实现污染分离；（ii）跨模型记忆分歧（CMMD），利用不同LLMs训练截止日期差异来区分记忆信号与真实推理信号。两种方法均在生成后阶段运行，无需重新训练模型或匿名化输入。

【实验结果 / Results】

在7个LLM（1.24亿-70亿参数）、50只标普100股票、42,800个提示和5.5年数据（2019-2024）的评估中，MCS达到Cohen's d = 18.57的污染分离效果（单独MIA特征仅d = 0.39-1.37）；CMMD过滤后信号的夏普比率达4.11，较未过滤信号2.76提升49%。清洁信号日均收益14.48个基点，污染信号仅2.13个基点（7倍差距）。关键发现：样本内准确率随污染上升（40.8%→52.5%），样本外却下降（47%→42%），直接证明记忆化以牺牲泛化为代价虚增准确性。

【应用价值 / Applications】

该研究为量化金融领域的LLM应用提供了实用的实时信号过滤工具，可直接部署于高频交易和策略构建流程，无需承担模型重训练的高昂成本或信息损失。MemGuard-Alpha帮助投资经理识别并剔除不可靠的记忆污染信号，避免"假阿尔法"陷阱，提升投资组合的真实风险调整后收益，对依赖LLM生成交易信号的资产管理行业具有重要实践意义。
