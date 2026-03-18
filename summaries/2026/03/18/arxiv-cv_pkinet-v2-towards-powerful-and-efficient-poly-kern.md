---
title: "PKINet-v2: Towards Powerful and Efficient Poly-Kernel Remote Sensing Object Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16341"
published: "2026-03-18"
summarized: "2026-03-18T18:11:23.527976"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了PKINet-v2，一种面向遥感目标检测的强大高效骨干网络，通过统一范式联合处理几何复杂性和空间复杂性挑战。该网络协同各向异性轴向条带卷积与各向同性方形核，构建多尺度感受野，在保留细粒度局部纹理的同时渐进聚合长距离上下文。为高效部署，作者引入异构核重参数化（HKR）策略，将所有异构分支融合为单一深度卷积，实现推理加速。在DOTA-v1.0/1.5、HRSC2016和DIOR-R四个基准数据集上，PKINet-v2达到SOTA精度，同时相比PKINet-v1实现3.9倍FPS提升。

【方法概述 / Method】
PKINet-v2核心采用"多核协同"设计：并行使用各向异性条带核（捕捉细长目标）与各向同性方形核（捕获广泛上下文），通过多尺度感受野融合两者优势。训练阶段采用多分支结构，推理阶段通过异构核重参数化（HKR）策略将异构分支等价转换为单一深度卷积，消除碎片化核启动开销。

【实验结果 / Results】
在四个主流遥感检测基准上，PKINet-v2取得领先性能；相比前代PKINet-v1，推理速度提升3.9倍FPS，实现精度与效率的双重突破。该方法在有效性和效率上均超越现有遥感专用骨干网络。

【应用价值 / Applications】
PKINet-v2适用于卫星/航空影像中的目标检测任务，如船舶、飞机、车辆等遥感目标的自动识别与定位，可支撑智慧农业、城市规划、环境监测、军事侦察等实际应用。其高效推理特性使其特别适合边缘设备部署和实时处理场景。
