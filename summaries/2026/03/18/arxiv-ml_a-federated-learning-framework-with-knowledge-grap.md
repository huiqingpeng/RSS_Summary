---
title: "A federated learning framework with knowledge graph and temporal transformer for early sepsis prediction in multi-center ICUs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15651"
published: "2026-03-18"
summarized: "2026-03-18T15:33:10.589191"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种用于多中心ICU脓毒症早期预测的新型联邦学习框架，通过整合医学知识图谱、时间Transformer和元学习技术，在保护患者隐私的前提下实现跨医院协作建模。该框架在MIMIC-IV和eICU数据集上取得了0.956的AUC，相比传统集中式模型提升22.4%，相比标准联邦学习提升12.7%，显著提高了脓毒症预测准确性。

【方法概述 / Method】
该框架采用联邦学习架构实现多医院数据协作而不共享原始数据；利用医学知识图谱编码结构化医学关系，结合时间Transformer捕获临床时序数据中的长程依赖；并引入模型无关元学习（MAML）策略，使全局模型能够快速适应各医院的本地数据分布。

【实验结果 / Results】
在MIMIC-IV和eICU数据集上的评估表明，该方法AUC达到0.956，较传统集中式模型提升22.4%，较标准联邦学习方法提升12.7%，展现出优异的脓毒症预测性能。

【应用价值 / Applications】
该研究为医疗机构间的隐私保护型协作提供了可靠的技术方案，可部署于多中心ICU网络实现脓毒症的早期预警，有助于提高患者生存率并促进医疗资源的优化配置，对推动智慧医疗和精准医学具有重要实践意义。
