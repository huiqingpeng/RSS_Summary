---
title: "How Centralized Radar Processing on NVIDIA DRIVE Enables Safer, Smarter Level 4 Autonomy"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/how-centralized-radar-processing-on-nvidia-drive-enables-safer-smarter-level-4-autonomy/"
published: "2026-03-25"
summarized: "2026-03-26T07:04:30.430635"
ai_provider: "openai"
---

【是什么 / What it is】

本文介绍NVIDIA DRIVE平台的一项技术创新——集中式雷达处理架构。该架构将传统雷达信号处理从边缘设备（雷达传感器内置的DSP/MCU）迁移到中央计算平台，使原始ADC（模数转换器）数据直接流入DRIVE系统的DRAM，并由专用的可编程视觉加速器（PVA）完成信号处理，从而释放GPU用于AI计算。NVIDIA与成科科技（ChengTech）合作，已在DRIVE AGX Thor平台上实现了这一方案的实时运行验证。

This article introduces a technical innovation on the NVIDIA DRIVE platform—centralized radar processing architecture. This architecture migrates traditional radar signal processing from edge devices (DSP/MCU built into radar sensors) to a centralized compute platform, allowing raw ADC (analog-to-digital converter) data to flow directly into DRIVE system DRAM. Dedicated Programmable Vision Accelerator (PVA) hardware handles signal processing, freeing the GPU for AI computation. NVIDIA collaborated with ChengTech to validate this solution running in real-time on the DRIVE AGX Thor platform.

---

【为什么重要 / Why it matters】

传统边缘处理架构将雷达信号压缩为稀疏点云，信息损失约100倍，且固定 pipeline 无法支持L4级自动驾驶所需的大模型和端到端学习。集中式处理使AI系统能够访问完整的雷达原始信号（类似RAW图像），支持时序感知模型、信号级融合及视觉-语言-动作（VLA）架构，同时降低硬件成本30%、体积20%和系统功耗20%，符合绿色能源趋势。

Traditional edge-processing architectures compress radar signals into sparse point clouds with ~100x information loss, and their fixed pipelines cannot support large models and end-to-end learning required for L4 autonomy. Centralized processing enables AI systems to access complete raw radar signals (similar to RAW images), supporting temporal-aware models, signal-level fusion, and vision-language-action (VLA) architectures. It also reduces hardware costs by 30%, volume by 20%, and system power consumption by 20%, aligning with green energy trends.

---

【我能用什么 / How I can use it】

若从事自动驾驶感知开发，可探索基于原始ADC数据的端到端雷达学习模型（如参考CVPR 2022的Raw High-Definition Radar工作），或构建跨摄像头-雷达-激光雷达的信号级融合方案；若涉及硬件选型，可评估成科科技等支持原始数据输出的雷达供应商，并规划高带宽车以太网/PCIe链路以承载540 MB/s级数据流；若研究能效优化，可借鉴PVA专用加速器的异构计算思路，将传统DSP任务卸载至能效比更优的专用硬件。

For autonomous driving perception development, explore end-to-end radar learning models based on raw ADC data (referencing works like CVPR 2022's Raw High-Definition Radar), or build signal-level fusion across camera-radar-lidar modalities. For hardware selection, evaluate radar suppliers like ChengTech supporting raw data output, and plan high-bandwidth automotive Ethernet/PCIe links to handle ~540 MB/s data streams. For energy efficiency research, adopt the heterogeneous computing approach of PVA dedicated accelerators, offloading traditional DSP tasks to more power-efficient specialized hardware.
