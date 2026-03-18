---
title: "TinyGLASS: Real-Time Self-Supervised In-Sensor Anomaly Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16451"
published: "2026-03-18"
summarized: "2026-03-18T18:13:51.592975"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了TinyGLASS，一种面向资源受限边缘设备的轻量化自监督异常检测方法。该工作将GLASS框架中的WideResNet-50骨干网络替换为紧凑型ResNet-18，并引入面向部署的优化以实现静态图追踪和INT8量化。TinyGLASS在Sony IMX500智能视觉传感器上实现了实时异常检测，在MVTec-AD基准上达到94.2%的图像级AUROC，同时满足8MB内存约束并以20 FPS运行。

【方法概述 / Method】
TinyGLASS采用ResNet-18替代原有的WideResNet-50作为特征提取骨干网络，显著降低模型参数量。通过Sony模型压缩工具包实现INT8量化和静态图追踪，使模型能够部署于IMX500智能视觉传感器的嵌入式AI处理器上，实现真正的"感内计算"(in-sensor computing)。

【实验结果 / Results】
TinyGLASS实现了8.7倍的参数压缩，在MVTec-AD基准上保持94.2%的图像级AUROC检测性能。系统在IMX500平台上以20 FPS实时运行，单次推理功耗仅4.0 mJ，能效达到470 GMAC/J。此外，模型在中等程度训练数据污染下仍保持稳定性能，并引入MMS数据集进行跨设备评估验证。

【应用价值 / Applications】
该研究适用于工业质量控制的实时边缘检测场景，特别是需要在产线端直接进行缺陷筛查的智能制造环境。感内计算架构消除了数据传输延迟和隐私风险，可广泛应用于自动化质检、半导体晶圆检测、精密零部件制造等对实时性和数据安全要求高的工业领域。
