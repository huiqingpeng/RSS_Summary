---
title: "Foundation-Model Surrogates Enable Data-Efficient Active Learning for Materials Discovery"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.12567"
published: "2026-03-18"
summarized: "2026-03-18T17:16:10.511879"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了In-Context Active Learning (ICAL)方法，利用预训练的Transformer基础模型TabPFN替代传统高斯过程(GP)和随机森林(RF)代理模型，解决材料发现中小数据场景下的主动学习瓶颈。TabPFN通过在数百万个合成回归任务上元学习获得表格数据的通用先验，无需针对特定数据集重新训练即可进行贝叶斯推断，提供准确的小数据回归性能和良好校准的预测不确定性。在10个材料数据集上的基准测试表明，TabPFN在8个数据集上获胜，相比GP平均减少52%的额外评估次数，相比RF减少29.77%，验证了预训练基础模型作为主动学习代理模型的有效性。

【方法概述 / Method】
ICAL采用TabPFN作为核心代理模型，该模型是基于Transformer的表格数据基础模型，通过在数百万个合成回归任务上进行元学习，获得了对表格数据的通用先验知识。TabPFN利用上下文学习(in-context learning)机制，在单次前向传播中对新数据集执行原则性的贝叶斯推断，无需针对特定任务进行微调或重新训练，同时输出良好校准的预测不确定性估计，直接支持主动学习中的采集函数优化。

【实验结果 / Results】
在涵盖10个不同材料系统的数据集上，ICAL相比传统GP和RF代理模型展现出显著优势：TabPFN在8/10的数据集上取得最佳性能，平均相比GP节省52%的实验评估次数，相比RF节省29.77%。交叉验证分析表明，TabPFN的优势源于其卓越的不确定性校准能力，在所有代理模型中实现了最低的负对数似然(NLL)和稀疏化误差曲线下面积(AUSE)，确保了主动学习中采集策略的可靠性。

【应用价值 / Applications】
该方法可广泛应用于材料科学及其他小数据实验科学领域的高效材料发现，特别适用于合成与表征成本高昂的场景，如新型催化剂、电池材料、光电材料的高通量筛选。ICAL通过大幅减少所需的实验迭代次数，能够显著加速研发周期、降低研究成本，并为其他依赖主动学习的科学发现领域（如药物发现、化学合成优化）提供可迁移的技术范式。
