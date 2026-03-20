---
title: "COTONET: A custom cotton detection algorithm based on YOLO11 for stage of growth cotton boll detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.11717"
published: "2026-03-20"
summarized: "2026-03-20T16:18:44.406796"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了COTONET，一种基于YOLO11的定制棉花检测算法，用于识别不同物候期的棉铃。该模型通过引入注意力机制（包括SimAM和PHAM）以及CARAFE上采样等架构改进，增强了难例检测能力。COTONET在仅使用7.6M参数和27.8 GFLOPS的情况下，实现了81.1%的mAP50和60.6%的mAP50-95，超越了标准YOLO基线模型，适用于边缘计算和移动机器人场景。

【方法概述 / Method】
COTONET以YOLO11为基础架构，进行了多项关键改进：使用Squeeze-and-Excitation模块替换卷积块，重新设计主干网络以集成注意力机制；采用CARAFE替代标准上采样操作；在特征聚合中引入Simple Attention Module（SimAM），并在下采样路径中部署Parallel Hybrid Attention Mechanisms（PHAM）实现通道、空间和坐标多维度的注意力机制。

【实验结果 / Results】
COTONET在棉花棉铃检测任务上显著优于标准YOLO基线，达到81.1%的mAP50和60.6%的mAP50-95。该模型属于中小型YOLO模型范畴，计算效率优异，可在低资源边缘设备上部署运行。

【应用价值 / Applications】
该研究为自动化棉花采收机器人提供了关键的视觉感知能力，通过精准识别不同生长阶段的棉铃，支持机械臂实现仿人工的轻柔抓取，从而减少纤维损伤、保持棉花品质。其轻量化设计特别适合农业移动机器人和边缘计算设备的实际部署需求。
