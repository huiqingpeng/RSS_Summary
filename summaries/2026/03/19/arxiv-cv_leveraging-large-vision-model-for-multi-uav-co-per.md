---
title: "Leveraging Large Vision Model for Multi-UAV Co-perception in Low-Altitude Wireless Networks"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16927"
published: "2026-03-19"
summarized: "2026-03-19T14:20:31.447807"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对多无人机协同感知中的通信延迟和资源效率挑战，提出了基站辅助无人机（BHU）框架，通过Top-K像素选择机制实现稀疏化视觉传输，并采用基于扩散模型的深度强化学习算法联合优化无人机选择、稀疏化比例和预编码矩阵。实验表明，该框架在Air-Co-Pred数据集上相比传统CNN基线感知性能提升超过5%，同时通信开销降低85%，为资源受限的无线环境下的多无人机协同感知提供了有效解决方案。

【方法概述 / Method】
该研究采用Top-K选择机制从无人机捕获的RGB图像中提取最具信息量的像素，实现稀疏化视觉传输；在地面服务器端使用基于Swin-large的MaskDINO编码器提取鸟瞰图（BEV）特征并进行协同特征融合；此外，开发了基于扩散模型的深度强化学习（DRL）算法，用于联合决策协同无人机选择、稀疏化比例和预编码矩阵。

【实验结果 / Results】
在Air-Co-Pred数据集上的仿真结果表明，与传统基于CNN的BEV融合基线相比，所提出的BHU框架将感知性能提升超过5%，同时通信开销减少85%，在通信效率与感知效用之间取得了良好平衡。

【应用价值 / Applications】
该研究适用于低空经济中的多种应用场景，如智能交通监控、城市安防巡逻和应急救援等，能够在带宽受限的无线网络环境下实现高效的多无人机协同感知；其通信高效的特性使其特别适合部署在5G/6G多用户MIMO系统中，为未来低空物联网和自动驾驶车辆感知提供技术支持。
