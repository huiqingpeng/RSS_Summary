---
title: "PC-CrossDiff: Point-Cluster Dual-Level Cross-Modal Differential Attention for Unified 3D Referring and Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17753"
published: "2026-03-19"
summarized: "2026-03-19T15:17:26.353651"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了PC-CrossDiff，一种用于统一3D指代表达理解（3DREC）和分割（3DRES）的双层级跨模态差分注意力框架。针对复杂多物体场景中现有方法难以解析隐式定位线索和抑制动态空间干扰的问题，该框架通过点级和簇级差分注意力机制，自适应提取判别性特征并增强定位相关的空间关系。在ScanRefer、NR3D和SR3D基准测试中取得最优性能，尤其在ScanRefer的Implicit子集上将3DREC任务的Overall@0.50指标提升了10.16%。

【方法概述 / Method】

PC-CrossDiff采用点-簇双层架构，包含两个核心模块：点级差分注意力（PLDA）模块通过可学习权重在文本与点云间建立双向差分注意力，自适应提取隐式定位线索；簇级差分注意力（CLDA）模块构建分层注意力机制，通过定位感知差分注意力块增强相关空间关系并抑制模糊干扰。该框架以统一方式处理3DREC和3DRES两个任务。

【实验结果 / Results】

该方法在多个基准数据集上达到SOTA性能，在ScanRefer的Implicit子集上3DREC任务的Overall@0.50指标提升10.16%，显著优于现有方法。实验结果表明，所提出的双层差分注意力机制有效增强了对复杂多物体场景中隐式空间线索的解析能力。

【应用价值 / Applications】

该研究可应用于智能机器人导航、增强现实交互和自动驾驶等需要自然语言引导3D场景理解的实际场景。通过提升复杂环境中多物体指代定位的准确性，PC-CrossDiff有助于推动3D视觉语言 grounding 技术在真实世界部署中的应用。
