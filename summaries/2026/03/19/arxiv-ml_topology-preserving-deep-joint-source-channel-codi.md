---
title: "Topology-Preserving Deep Joint Source-Channel Coding for Semantic Communication"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17126"
published: "2026-03-19"
summarized: "2026-03-19T12:07:47.185549"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了TopoJSCC，一种面向拓扑感知的深度联合信源信道编码（DeepJSCC）框架，用于语义通信。该方法通过引入持续同调正则化器进行端到端训练，利用Wasserstein距离惩罚原始图像与重建图像的立方体持续图差异，以及信道前后潜在特征的Vietoris-Rips持续性差异，从而在低信噪比和带宽受限条件下同时改善拓扑保持性和峰值信噪比（PSNR）。

【方法概述 / Method】
TopoJSCC采用端到端深度学习架构，将代数拓扑中的持续同调理论融入DeepJSCC训练过程。具体通过两种拓扑正则化约束：一是图像域的立方体持续性（cubical persistence）一致性约束，二是潜在特征空间的Vietoris-Rips持续性（Vietoris-Rips persistence）鲁棒性约束，无需任何边信息即可实现拓扑保持的联合编码。

【实验结果 / Results】
实验结果表明，在低信噪比（SNR）和低带宽比条件下，TopoJSCC相比传统DeepJSCC方案在拓扑保持性和PSNR指标上均有提升。该方法有效保护了图像的全局结构连通性，而非仅优化逐像素保真度。

【应用价值 / Applications】
该研究适用于自动驾驶等对全局结构信息敏感的无线视觉应用，能够在恶劣信道条件下保持语义层面的拓扑完整性。TopoJSCC为语义通信系统提供了新的设计范式，特别适用于带宽受限且对结构保真度要求高的边缘视觉任务。
