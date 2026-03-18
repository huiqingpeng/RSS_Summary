---
title: "Informative Perturbation Selection for Uncertainty-Aware Post-hoc Explanations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14894"
published: "2026-03-18"
summarized: "2026-03-18T17:07:39.012261"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了EAGLE（Expected Active Gain for Local Explanations），一种后验模型无关解释框架，将扰动选择重新表述为信息论主动学习问题。该方法通过自适应采样最大化期望信息增益的扰动，高效学习线性替代可解释模型，同时生成特征重要性分数及不确定性/置信度估计。理论分析表明累积信息增益按O(d log t)缩放，样本复杂度随特征维度d线性增长、随置信参数1/δ对数增长，实验验证了其在表格和图像数据上的优越性。

【方法概述 / Method】
EAGLE将局部解释中的扰动选择建模为信息论主动学习问题，通过自适应策略选择能最大化期望信息增益的扰动样本。该方法在构建目标样本邻域时，同时优化替代模型的学习效率并量化解释的不确定性，突破了传统方法随机或启发式采样扰动的局限。

【实验结果 / Results】
在表格和图像数据集上的实证结果验证了理论发现：相比Tilia、US-LIME、GLIME和BayesLIME等最先进基线，EAGLE显著提升了跨运行的解释可复现性，实现了更高的邻域稳定性，并改善了扰动样本质量，表明其采样策略能构建更具信息量的局部邻域。

【应用价值 / Applications】
该研究为高风险的机器学习部署场景（如医疗诊断、金融风控）提供了更可靠、透明的模型解释工具，其不确定性量化能力帮助用户识别解释可信度低的案例，避免错误决策；同时适用于需要解释一致性和稳定性的模型审计与合规验证场景。
