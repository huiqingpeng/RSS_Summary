---
title: "SuCor: Susceptibility Distortion Correction via Parameter-Free and Self-Regularized Optimal Transport"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16758"
published: "2026-03-18"
summarized: "2026-03-18T18:20:15.954118"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SuCor，一种基于最优传输（OT）的磁化率诱导几何畸变校正方法，用于回波平面成像（EPI）。该方法将反向相位编码EPI图像对的畸变场建模为Wasserstein-2重心位移，并通过频域弯曲能量惩罚实现自正则化，强度由Morozov偏差原理自动确定。在HCP数据集上，SuCor与T1结构像的平均体素互信息达0.341，优于FSL TOPUP的0.317，且单核CPU运行仅需约12秒。

【方法概述 / Method】
SuCor采用最优传输理论，将每列畸变场建模为相反极性强度分布之间的Wasserstein-2重心位移。正则化在频域通过弯曲能量惩罚实现，其强度通过Morozov偏差原理自动选择，无需手动调参，实现了完全参数自由的自正则化框架。

【实验结果 / Results】
在HCP数据集（含左右/右左b0 EPI对及配准T1结构参考）上，SuCor与T1图像的平均体素互信息为0.341，显著优于传统方法FSL TOPUP的0.317。计算效率方面，SuCor在单核CPU上运行时间约为12秒，展现出优异的准确性与效率平衡。

【应用价值 / Applications】
该方法可直接应用于神经影像学中的扩散MRI预处理流程，解决EPI序列因磁化率差异导致的图像几何畸变问题。其参数自由特性降低了临床和科研使用门槛，快速单核CPU运行能力使其适用于大规模脑连接组数据处理和实时成像场景。
