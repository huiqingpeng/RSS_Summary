---
title: "WAFT-Stereo: Warping-Alone Field Transforms for Stereo Matching"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24836"
published: "2026-03-27"
summarized: "2026-03-28T07:17:34.703429"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了WAFT-Stereo，一种基于warping的简单高效的立体匹配方法。研究表明，许多领先方法中常用的代价体（cost volume）设计并非必需，可通过warping操作替代，从而在保持高性能的同时提升效率。WAFT-Stereo在ETH3D、KITTI和Middlebury三大公开基准上均排名第一，在ETH3D基准上将零样本误差降低了81%，同时速度比竞争方法快1.8-6.7倍。

【方法概述 / Method】
WAFT-Stereo采用纯warping机制替代传统的代价体构建，通过field transforms直接对特征进行空间变换和对齐，避免了显式构建3D代价体的高计算开销。该方法简化了立体匹配的网络架构，在降低内存和计算复杂度的同时保持了精确的视差估计能力。

【实验结果 / Results】
WAFT-Stereo在ETH3D、KITTI和Middlebury三大立体匹配基准上均取得第一名的性能，在ETH3D基准上实现81%的零样本误差降低。与现有竞争方法相比，该方法实现了1.8-6.7倍的推理速度提升，在精度与效率之间取得了显著优势。

【应用价值 / Applications】
该研究为实时立体视觉系统（如自动驾驶、机器人导航和增强现实）提供了高效高精度的深度估计方案。通过消除代价体带来的计算瓶颈，WAFT-Stereo特别适用于资源受限的边缘设备和需要高帧率处理的应用场景。
