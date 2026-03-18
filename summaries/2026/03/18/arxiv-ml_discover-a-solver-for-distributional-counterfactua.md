---
title: "DISCOVER: A Solver for Distributional Counterfactual Explanations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16436"
published: "2026-03-18"
summarized: "2026-03-18T15:44:00.485580"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DISCOVER，一种模型无关的分布反事实解释（DCE）求解器。现有DCE方法依赖梯度优化，无法适用于现实世界中占主导的非可微表格模型。DISCOVER通过稀疏的"提议-选择"搜索范式替代梯度下降，同时保留了原始DCE的优化目标和统计认证机制，将分布反事实推理扩展至现代黑盒学习流程。

【方法概述 / Method】
DISCOVER采用稀疏提议-选择搜索范式，利用运输目标的样本级分解计算每行影响分数，并强制执行top-k干预预算以聚焦最具影响力的样本。为在无预测器梯度的情况下指导候选生成，该方法引入了由输入侧传输几何驱动的OT引导锥采样原语。

【实验结果 / Results】
在多个表格数据集上的实验表明，DISCOVER实现了输入分布与输出分布的强联合对齐，成功将分布反事实推理能力扩展到非可微的黑盒学习管道，验证了该方法在模型无关设定下的有效性。

【应用价值 / Applications】
该研究适用于金融风控、医疗诊断等依赖非可微模型（如梯度提升树、随机森林）的关键决策场景，使机构能够在不暴露模型内部结构的情况下，生成具有统计认证的分布级反事实解释，支持合规审计和策略优化。
