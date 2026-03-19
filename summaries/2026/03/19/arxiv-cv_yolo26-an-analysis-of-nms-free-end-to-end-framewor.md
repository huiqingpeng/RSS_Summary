---
title: "YOLO26: An Analysis of NMS-Free End to End Framework for Real-Time Object Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.12882"
published: "2026-03-19"
summarized: "2026-03-19T16:30:18.822806"
ai_provider: "openai"
---

【论文摘要 / Abstract】

YOLO26提出了一种无需非极大值抑制（NMS）的端到端实时目标检测框架，通过消除传统NMS后处理带来的延迟和超参数依赖，实现了确定性的推理延迟。该框架集成了MuSGD优化器、小目标感知标签分配（STAL）和ProgLoss动态监督等核心机制，并在COCO val2017基准上完成了从Nano到Extra-Large全尺度模型的系统评估。研究还涵盖了YOLOE-26开放词汇模块的统一多任务能力，分析了表征学习与启发式后处理解耦对"导出差距"和边缘部署确定性的影响。

【方法概述 / Method】

YOLO26采用原生端到端学习策略，以MuSGD优化器稳定骨干网络训练，配合STAL机制优化小目标的标签分配，并通过ProgLoss实现动态监督调度。该方法完全摒弃了NMS后处理，将目标检测转化为纯粹的神经网络前向推理问题，同时支持开放词汇检测等扩展任务。

【实验结果 / Results】

论文在COCO val2017 leaderboard上完成了YOLO26全尺度模型（Nano/Extra-Large）与CNN系列（前代YOLO）及Transformer架构（RT-DETR、DEIM、RF-DETR）的全面对比，详细记录了速度-精度权衡曲线和参数量需求。分析表明，NMS-free设计显著降低了"导出差距"并提供了确定性的边缘部署延迟，但未宣称单一最优模型配置。

【应用价值 / Applications】

该研究对边缘计算场景下的实时计算机视觉部署具有重要价值，尤其适用于自动驾驶、工业质检、移动设备等对延迟确定性要求严格的应用。开放词汇检测模块YOLOE-26进一步扩展了零样本和提示式检测能力，为需要灵活适应新类别的动态环境提供了实用解决方案。
