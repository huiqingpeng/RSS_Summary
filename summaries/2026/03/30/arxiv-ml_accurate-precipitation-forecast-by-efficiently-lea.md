---
title: "Accurate Precipitation Forecast by Efficiently Learning from Massive Atmospheric Variables and Unbalanced Distribution"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26108"
published: "2026-03-30"
summarized: "2026-03-31T07:21:50.558248"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究针对短时（0-24小时）降水预报中降水演变模式复杂、降水与非降水样本极度不平衡、以及现有模型无法高效利用多源大气观测数据等挑战，开发了一种新型预报模型。该模型通过自动提取并迭代预测与降水演变强相关的潜在特征，有效利用海量大气观测数据；同时提出"WMCE"损失函数以准确识别稀缺降水事件并精确预测其强度。在两个数据集上的大量实验表明，该模型在准确性和效率上均显著优于现有主流基线方法，且大幅降低了获取有价值预测所需的计算成本。

【方法概述 / Method】
该模型采用自动特征提取机制，从海量多源大气观测数据中迭代预测与降水演变强相关的潜在特征，实现高效的数据利用。针对降水样本不平衡问题，研究设计了WMCE（Weighted Multi-task Cross-Entropy）损失函数，能够同时处理降水事件的精确识别和强度预测任务。

【实验结果 / Results】
在两个数据集上的广泛实验表明，所提出的模型在准确性和计算效率方面均显著且持续地优于所有主流基线方法。该模型大幅降低了获取有价值预测所需的计算成本，在保持高精度的同时实现了高效的实际应用部署。

【应用价值 / Applications】
该研究可广泛应用于气象预报、防灾减灾、农业生产调度、交通运输管理等社会经济活动和公共安全领域。模型的高效率和低计算成本特性使其特别适合实时业务预报系统部署，为实用化降水预报设立了新的里程碑。
