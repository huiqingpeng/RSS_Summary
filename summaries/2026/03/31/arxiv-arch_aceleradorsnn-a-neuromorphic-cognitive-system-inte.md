---
title: "AceleradorSNN: A Neuromorphic Cognitive System Integrating Spiking Neural Networks and DynamicImage Signal Processing on FPGA"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.28429"
published: "2026-03-31"
summarized: "2026-04-01T07:16:36.042144"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了AceleradorSNN，一种第三代人工智能认知系统架构，旨在解决自动驾驶系统（ADAS）、无人机（UAV）和工业4.0机器人等应用中对高速、低延迟、高能效目标检测的需求。该架构集成了基于脉冲神经网络（SNN）的神经形态处理单元（NPU）用于处理动态视觉传感器（DVS）的异步数据，以及一个可动态重配置的认知图像信号处理器（ISP）用于RGB相机。论文详细阐述了这两个IP核的硬件导向设计、代理梯度训练的SNN骨干网络评估，以及在FPGA上实现的实时流式ISP架构。

【方法概述 / Method】

论文采用硬件-软件协同设计方法，开发了基于FPGA的异构神经形态认知系统。核心方法包括：使用代理梯度训练策略优化SNN骨干网络以适应硬件部署；设计动态可重配置的ISP架构实现RGB相机的实时流处理；以及将NPU与ISP集成到统一的FPGA平台中，实现DVS异步事件流与传统帧图像的融合处理。

【实验结果 / Results】

论文在FPGA硬件平台上实现了所提出的AceleradorSNN系统，验证了SNN骨干网络的实时推理能力以及ISP的流式处理能力。具体性能指标（如延迟、功耗、检测精度）在提供的摘要中未详细说明，但强调了系统实现了"实时"（real-time）处理目标检测任务。

【应用价值 / Applications】

该研究主要面向边缘AI和自主系统的低功耗实时感知需求，特别适用于ADAS、无人机导航和工业4.0机器人等场景。通过整合神经形态计算（事件驱动、高能效）与传统图像处理，该系统为资源受限环境下的高速目标检测提供了可行的硬件解决方案，有望推动第三代AI芯片在自动驾驶和智能机器人领域的实际部署。
