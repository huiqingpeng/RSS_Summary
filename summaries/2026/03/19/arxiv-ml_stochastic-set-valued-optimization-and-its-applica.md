---
title: "Stochastic set-valued optimization and its application to robust learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17691"
published: "2026-03-19"
summarized: "2026-03-19T13:15:10.257884"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了**随机集合值优化（Stochastic Set-Valued Optimization, SVO）**框架，专为鲁棒机器学习设计，其中每个决策变量映射到一组目标值，最优性通过集合关系定义。作者重点研究**超盒集合（hyperbox sets）**的SVO问题，可重构为具有有限目标的**多目标优化（MOO）**问题，并由此衍生出**区间值优化（IVO）**和**矩形值优化（RVO）**两种特例。通过将**子分位数（subquantiles）**和**超分位数（superquantiles）**纳入MOO重构的目标函数，该框架能够同时捕捉损失分布的上下尾行为，在分布偏移场景下展现出比经验风险最小化更好的鲁棒性和更低的变化性。

【方法概述 / Method】

论文构建了融合子分位数和超分位数的随机IVO/RVO公式，为多目标优化重构提供可解释的权衡机制，突破了传统经验风险最小化和经典鲁棒模型的局限。求解时采用**随机多梯度算法（stochastic multi-gradient algorithms）**，并通过选择**Pareto膝点解（Pareto knee solution）**来平衡多个目标之间的冲突。

【实验结果 / Results】

数值实验表明，所提算法结合Pareto膝点选择策略在分布偏移条件下，相比经验风险最小化（ERM）具有**更优的鲁棒性和更低的测试复制间变异性**，同时保持了具有竞争力的预测精度。该结果验证了同时建模损失分布上下尾行为对提升模型泛化能力的有效性。

【应用价值 / Applications】

该研究为**分布鲁棒优化**和**风险敏感决策**提供了新的数学工具，适用于金融风控、医疗诊断等对模型可靠性和极端情况敏感性要求高的领域。SVO框架的模块化设计使其可扩展至更一般的集合值映射，为开发自适应不确定性的机器学习系统奠定了理论基础。
