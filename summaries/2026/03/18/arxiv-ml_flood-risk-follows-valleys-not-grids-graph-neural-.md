---
title: "Flood Risk Follows Valleys, Not Grids: Graph Neural Networks for Flash Flood Susceptibility Mapping in Himachal Pradesh with Conformal Uncertainty Quantification"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15681"
published: "2026-03-18"
summarized: "2026-03-18T15:33:59.933745"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究针对印度喜马偕尔邦（HP）暴洪灾害风险制图问题，提出了一种基于图神经网络（GraphSAGE）的新方法。研究指出传统基于像素的模型忽略了上游洪水对下游风险的连通性影响，因此构建了包含460个子流域和1,700条有向边的水文连通图。通过六年的Sentinel-1 SAR洪水清单数据（2018-2023年，3,000个事件）和12个环境变量进行训练，并采用符合性预测（conformal prediction）量化不确定性，该研究首次为喜马偕尔邦提供了具有统计保证的90%覆盖区间的敏感性制图。

【方法概述 / Method】

研究采用GraphSAGE图神经网络架构，在基于DEM提取的流域连通图上进行消息传递，以捕捉水流上下游的依赖关系。模型输入包括30米分辨率的12个环境变量，以2018-2022年数据训练，2023年数据作为测试集。评估采用留一盆地空间交叉验证（leave-one-basin-out spatial CV），避免随机划分导致的5-15% AUC虚高问题。不确定性量化采用符合性预测框架生成预测区间。

【实验结果 / Results】

GNN模型达到AUC = 0.978 ± 0.017，显著优于最佳基线模型（XGBoost/LightGBM集成，AUC = 0.881）和已发表文献基准（AUC = 0.88），性能提升+0.097证实了流域连通性携带了像素模型无法捕捉的预测信号。符合性区间在2023年测试集上实现82.9%的经验覆盖率，但高风险区域覆盖率较低（45-59%），提示SAR标签噪声需进一步处理。

【应用价值 / Applications】

研究成果可直接服务于喜马偕尔邦的灾害风险管理与基础设施规划：高敏感区域识别出1,457公里公路（含217公里战略性的马纳里-列城走廊）、2,759座桥梁及4座主要水电设施面临的洪水威胁。符合性不确定性量化可为决策者提供风险置信区间，支持疏散路线规划、桥梁加固优先级排序及保险定价等实际应用。
