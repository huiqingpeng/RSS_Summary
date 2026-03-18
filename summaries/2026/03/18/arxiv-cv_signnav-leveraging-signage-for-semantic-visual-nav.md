---
title: "SignNav: Leveraging Signage for Semantic Visual Navigation in Large-Scale Indoor Environments"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16166"
published: "2026-03-18"
summarized: "2026-03-18T18:23:22.576092"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SignNav，一种新颖的具身导航任务，要求智能体解读室内标识中的语义提示并据此进行导航决策。为支持该领域研究，作者构建了LSI-Dataset数据集，并设计了时空感知Transformer（START）模型，通过空间感知模块将标识语义映射到物理世界，时间感知模块捕捉历史状态与当前观测的长程依赖关系。该方法在val-unseen划分上达到了80%成功率和0.74 NDTW的最先进性能，并成功部署于真实物理环境。

【方法概述 / Method】
论文采用端到端的时空感知Transformer（START）模型进行决策，包含两个核心模块：空间感知模块负责将标识的语义提示与物理世界位置关联，时间感知模块处理历史状态与当前观测之间的长程依赖。训练过程采用基于DAgger的两阶段训练策略，结合模仿学习与在线数据聚合。

【实验结果 / Results】
在LSI-Dataset的val-unseen测试集上，START模型取得了80%的成功率（SR）和0.74的NDTW指标，达到当前最优水平。此外，该方法在真实世界环境中无需预建地图即可实现有效部署，验证了其实际可行性。

【应用价值 / Applications】
SignNav可直接应用于医院、机场航站楼等大型室内场所的自主导航机器人，使其能够像人类一样利用标识信息完成目的地引导。该研究降低了对预建地图的依赖，为服务机器人在动态、复杂的真实室内环境中的部署提供了实用解决方案。
