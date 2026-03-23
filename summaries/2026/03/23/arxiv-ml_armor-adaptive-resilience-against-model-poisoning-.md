---
title: "ARMOR: Adaptive Resilience Against Model Poisoning Attacks in Continual Federated Learning for Mobile Indoor Localization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19594"
published: "2026-03-23"
summarized: "2026-03-24T07:19:53.145619"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ARMOR框架，用于解决持续联邦学习（CFL）中模型中毒攻击的问题，特别是在移动室内定位场景下。ARMOR通过引入状态空间模型（SSM）学习全局模型权重张量的历史演化规律，预测下一时刻的权重状态，从而检测并缓解异常更新。实验表明，该方法相比现有最优方法可将平均误差降低8.0倍，最坏情况误差降低4.97倍，显著提升了系统对模型污染的鲁棒性。

【方法概述 / Method】
ARMOR采用状态空间模型（SSM）建模全局模型权重张量的时序演化特性，通过历史学习预测下一时刻的权重状态。系统将接收到的本地更新与SSM预测值进行比对，检测偏离预期的异常更新，并在聚合前选择性过滤受损更新，实现动态环境下的自适应防护。

【实验结果 / Results】
在真实世界移动设备和实际数据上的测试表明，ARMOR相比现有最优室内定位框架实现了显著性能提升：平均定位误差降低达8.0倍，最坏情况误差降低4.97倍。该方法在持续学习环境、设备异构性和动态室内环境变化条件下均展现出强大的抗模型中毒攻击能力。

【应用价值 / Applications】
ARMOR可广泛应用于隐私敏感的室内定位场景，如商场导航、资产追踪、个性化服务推送等移动应用。该方法特别适用于需要持续学习适应环境变化、同时防范恶意攻击的实际部署环境，为联邦学习在资源受限移动设备上的安全应用提供了可靠保障。
