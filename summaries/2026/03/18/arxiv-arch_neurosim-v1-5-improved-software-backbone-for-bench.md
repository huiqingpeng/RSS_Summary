---
title: "NeuroSim V1.5: Improved Software Backbone for Benchmarking Compute-in-Memory Accelerators with Device and Circuit-level Non-idealities"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2505.02314"
published: "2026-03-18"
summarized: "2026-03-18T15:32:03.557672"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文介绍了NeuroSim V1.5，一个用于评估存内计算（ACIM）加速器的开源仿真框架。该版本实现了四大关键改进：与TensorRT后训练量化流程的无缝集成以支持更多神经网络架构（包括Transformer）、基于预表征统计模型的灵活噪声注入方法、扩展对新兴非易失性电容式存储器的支持，以及通过优化行为仿真实现最高6.5倍的运行速度提升。这些能力使得系统性的设计空间探索能够在精度与硬件效率两个维度上同步进行，为下一代ACIM加速器的设计验证提供了重要工具。

【方法概述 / Method】
NeuroSim V1.5采用分层建模方法，将器件级SPICE仿真或硅片实测数据通过预表征的统计模型转换为可注入的噪声参数，实现了高保真度的非理想性建模。框架通过API级集成对接TensorRT的后训练量化流程，支持INT8等低精度推理，并采用优化的行为级仿真替代部分电路级仿真以加速整体运行。

【实验结果 / Results】
NeuroSim V1.5相比V1.4版本实现了最高6.5倍的仿真速度提升，同时保持了建模精度。通过多个案例研究，作者展示了在维持网络精度的前提下对关键设计参数（如阵列尺寸、电导范围、ADC精度等）进行优化的能力，验证了框架在Transformer等新型网络架构上的适用性。

【应用价值 / Applications】
该框架为存内计算芯片的设计者提供了从算法到硬件的协同优化平台，可用于早期设计阶段快速评估不同器件选择、电路拓扑和架构配置对系统能效与推理精度的影响。其开源特性促进了学术界和工业界在AI加速器领域的协作研究，有助于缩短下一代高能效边缘AI芯片的研发周期。
