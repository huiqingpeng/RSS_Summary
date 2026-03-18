---
title: "drGT: Attention-Guided Gene Assessment of Drug Response Utilizing a Drug-Cell-Gene Heterogeneous Network"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2405.08979"
published: "2026-03-18"
summarized: "2026-03-18T16:16:11.948156"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究提出drGT模型，一种基于药物-细胞-基因异构图的深度学习方法，通过注意力系数实现药物响应预测与机制导向的可解释性相结合。该模型在GDSC、NCI60和CTRP数据集上评估了预测泛化能力（随机划分、未见药物、未见细胞及零样本场景）和生物学合理性（利用PubMed文本挖掘和基于结构的DTI预测验证）。drGT在回归任务上达到最优性能（R²最高0.690），同时在分类任务保持竞争力（AUROC最高0.945），且是唯一在未见药物场景下取得正R²的模型。

【方法概述 / Method】
drGT构建了一个包含药物、基因和细胞系三类节点的异构图网络，采用图神经网络进行消息传递学习。模型利用注意力机制计算注意力系数（ACs），将预测任务与特征重要性解释相结合，使基因层面的预测具有生物学可解释性。

【实验结果 / Results】
在随机5折交叉验证中，drGT取得AUROC 0.945（排名第三）和R² 0.690（超越所有基线）。在未见细胞系和未见药物的留一法测试中，AUROC分别为0.706和0.844，R²分别为0.692和0.022。零样本预测中，drGT获得AUROC 0.786和R² 0.334，均为所有模型中最高。可解释性方面，36.9%的预测药物-基因链接与已知DTI匹配，63.7%得到PubMed摘要或结构模型支持。

【应用价值 / Applications】
drGT可用于新药开发的早期筛选和 repurposing，通过预测未见药物/细胞的响应降低实验成本。其注意力机制提供的通路级生物学解释有助于理解药物作用机制，支持精准医疗中的个体化用药决策。该框架展示了异构图学习在生物发现中的潜力，可扩展至其他多模态生物医学预测任务。
