---
title: "SuperOcc: Toward Cohesive Temporal Modeling for Superquadric-based 3D Occupancy Prediction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.15644"
published: "2026-03-20"
summarized: "2026-03-20T16:17:35.443927"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SuperOcc，一种基于超二次曲面（superquadric）的3D占用预测新框架，旨在解决现有方法中密集场景表示忽略真实驾驶场景稀疏性的问题。该框架通过三项关键设计——融合视角中心与物体中心时间线索的连贯时序建模机制、多超二次曲面解码策略以及高效的超二次曲面到体素 splatting 方案——在SurroundOcc和Occ3D基准上实现了最先进的性能，同时保持了卓越的计算效率。

【方法概述 / Method】
SuperOcc采用超二次曲面作为稀疏场景表示，并提出三项核心技术：（1）连贯时序建模机制同时利用视角中心（view-centric）和物体中心（object-centric）的时间线索；（2）多超二次曲面解码策略，在保持查询稀疏性的同时增强几何表达能力；（3）高效的超二次曲面到体素 splatting 方案，提升计算效率。

【实验结果 / Results】
在SurroundOcc和Occ3D两个主流基准数据集上的大量实验表明，SuperOcc达到了最先进的性能水平，同时保持了优越的计算效率，有效解决了现有超二次曲面框架中时序建模不足、查询稀疏性与几何表达性之间的权衡难题以及splatting效率低下的问题。

【应用价值 / Applications】
该研究可直接应用于自动驾驶系统的环境感知模块，为车辆提供对驾驶环境的全面3D理解。相比传统密集表示方法，SuperOcc的稀疏表示和高效推理特性更适合实时部署，有助于提升自动驾驶的安全性和计算资源利用效率。
