---
title: "Evaluating Black-Box Vulnerabilities with Wasserstein-Constrained Data Perturbations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15867"
published: "2026-03-18"
summarized: "2026-03-18T15:36:31.444740"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对机器学习模型在工业应用中的可解释性不足和黑箱算法风险问题，提出了一种基于最优传输理论的黑箱漏洞评估方法。研究通过寻找满足特定约束条件下Wasserstein距离最近的输入分布扰动，分析模型对输入分布变化的响应行为。作者建立了投影分布的收敛性理论结果，并在回归和分类任务的真实数据集上验证了该方法的有效性。

【方法概述 / Method】
该方法利用最优传输（Optimal Transport）理论，在Wasserstein距离度量下求解与原始输入分布最接近且满足预设约束条件的扰动分布。通过将分布层面的扰动约束形式化为Wasserstein球内的优化问题，实现对黑箱模型输入分布变化的系统性分析，并推导出投影分布的渐近收敛性质。

【实验结果 / Results】
论文在合成示例和多个真实数据集上验证了所提方法，涵盖了回归和分类两种任务场景。实验表明该方法能够有效识别黑箱模型在输入分布偏移时的脆弱性，并量化了模型行为的变化程度；理论收敛结果也在数值实验中得到验证。

【应用价值 / Applications】
该方法适用于工业界ML系统的风险评估与模型审计场景，特别是在无法获取模型内部结构的黑箱环境下。其可应用于金融风控、医疗诊断等高风险领域的模型稳健性测试，以及满足AI监管要求的模型可解释性与公平性分析。
