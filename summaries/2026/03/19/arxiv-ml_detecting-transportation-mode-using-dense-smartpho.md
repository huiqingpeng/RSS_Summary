---
title: "Detecting Transportation Mode Using Dense Smartphone GPS Trajectories and Transformer Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.00340"
published: "2026-03-19"
summarized: "2026-03-19T14:12:37.650334"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究提出了一种名为 SpeedTransformer 的新型 Transformer 模型，仅依靠速度输入即可从密集智能手机 GPS 轨迹中推断交通模式。该模型在基准实验中优于传统的 LSTM 等深度学习模型，并在迁移学习中展现出强大灵活性——仅需少量数据微调即可在不同地理区域实现高精度。真实环境部署实验进一步验证了其在复杂建成环境和高数据不确定性条件下的优越性。

【方法概述 / Method】
研究采用纯速度序列作为输入，利用 Transformer 架构的自注意力机制捕捉 GPS 轨迹中的时序依赖关系，避免了传统方法对多源传感器数据的依赖。该设计实现了轻量化的特征工程，同时保持了模型对复杂移动模式的建模能力。

【实验结果 / Results】
SpeedTransformer 在基准测试中显著超越 LSTM 等传统深度学习模型；迁移学习实验表明，经小样本微调后模型在不同地理区域均能保持高准确率；真实场景部署中，该模型在复杂城市环境和高噪声数据条件下持续优于基线模型。

【应用价值 / Applications】
该研究为基于智能手机的被动式交通模式识别提供了高效解决方案，可广泛应用于个人出行行为分析、城市交通规划、碳排放估算及智慧城市管理等领域。其迁移学习能力尤其适用于数据稀缺的地区，降低了大规模部署的成本门槛。
