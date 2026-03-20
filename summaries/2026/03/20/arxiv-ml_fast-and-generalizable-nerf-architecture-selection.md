---
title: "Fast and Generalizable NeRF Architecture Selection for Satellite Scene Reconstruction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18306"
published: "2026-03-20"
summarized: "2026-03-20T13:11:20.601717"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对卫星影像NeRF重建中架构选择耗时的问题，通过SHAP分析发现多视图一致性而非模型架构才是决定重建质量的关键因素。基于此洞察，作者提出PreSCAN预测框架，可在训练前利用轻量级几何和光度描述符估计NeRF质量，实现30秒内完成架构选择，较神经架构搜索(NAS)加速1000倍。该框架在DFC2019数据集上展现出良好的跨场景泛化能力，且在边缘设备(Jetson Orin)上结合离线成本分析可降低26%功耗和43%延迟。

【方法概述 / Method】
PreSCAN采用轻量级的几何描述符（如视角基线、深度一致性）和光度描述符（如图像熵、亮度变化）作为输入特征，训练一个快速预测模型来估计不同NeRF架构的重建质量（PSNR）。该方法无需实际训练NeRF即可预测其性能，避免了耗时的NAS过程。

【实验结果 / Results】
PreSCAN在DFC2019卫星数据集上实现了<1 dB的预测误差，架构选择时间从数小时缩短至<30秒。在Jetson Orin边缘平台上的部署实验表明，结合预测结果与离线成本分析，可在仅损失极小重建质量的前提下，实现推理功耗降低26%、延迟降低43%。

【应用价值 / Applications】
该研究对实时卫星影像三维重建具有重要价值，特别适用于计算资源受限的边缘部署场景（如星上处理、无人机载荷）。PreSCAN的快速预测能力使动态场景自适应成为可能，可广泛应用于灾害监测、城市规划、军事侦察等需要快速响应的卫星遥感应用。
