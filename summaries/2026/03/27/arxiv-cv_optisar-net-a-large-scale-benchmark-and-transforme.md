---
title: "OptiSAR-Net++: A Large-Scale Benchmark and Transformer-Free Framework for Cross-Domain Remote Sensing Visual Grounding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24876"
published: "2026-03-27"
summarized: "2026-03-28T07:18:09.698296"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了跨域遥感视觉定位（CD-RSVG）任务，并构建了首个大规模基准数据集OptSAR-RSVG，涵盖光学与合成孔径雷达（SAR）双域图像。作者设计了OptiSAR-Net++框架，通过PL-MoE模块实现高效的跨域特征解耦，并采用CLIP对比学习范式替代传统Transformer解码，结合动态对抗负采样将生成式回归转化为跨模态匹配任务。实验表明，该框架在OptSAR-RSVG和DIOR-RSVG基准上均达到SOTA性能，在定位精度与计算效率方面具有显著优势。

【方法概述 / Method】

OptiSAR-Net++采用三阶段技术方案：（1）使用补丁级低秩自适应混合专家（PL-MoE）对光学与SAR特征进行解耦与自适应融合；（2）基于CLIP的对比学习框架替代Transformer解码器，通过动态对抗负采样策略优化跨模态匹配；（3）引入文本引导双门控融合模块（TGDF-SSA）和区域感知辅助头，增强语义-视觉对齐与空间建模能力。

【实验结果 / Results】

该框架在OptSAR-RSVG和DIOR-RSVG两个基准数据集上均取得最优性能，定位精度超越现有方法。同时，由于摒弃了计算密集型的Transformer解码结构，模型在保持高精度的同时实现了显著的推理效率提升，验证了对比学习范式在遥感视觉定位任务中的有效性。

【应用价值 / Applications】

该研究突破了传统RSVG方法仅适用于单一传感器域的局限，支持光学与SAR图像的联合理解与目标定位，适用于灾害应急响应、军事侦察、环境监测等需要多源遥感数据协同分析的场景。其高效的无Transformer设计也为资源受限的星载或机载边缘计算平台部署提供了可行性。
