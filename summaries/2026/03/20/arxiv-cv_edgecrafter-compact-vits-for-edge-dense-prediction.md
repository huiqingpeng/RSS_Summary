---
title: "EdgeCrafter: Compact ViTs for Edge Dense Prediction via Task-Specialized Distillation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18739"
published: "2026-03-20"
summarized: "2026-03-20T15:15:22.673330"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了EdgeCrafter，一个统一的紧凑型Vision Transformer（ViT）框架，用于边缘设备上的密集预测任务。研究表明，小型ViT在边缘密集预测中表现不佳的主要原因并非ViT架构本身的问题，而是缺乏任务特定的表征学习。通过任务专用蒸馏（task-specialized distillation）和边缘友好型编解码器设计，EdgeCrafter在目标检测、实例分割和姿态估计三个任务上均取得了优于或媲美当前主流轻量级CNN架构（如YOLO系列）的性能，且无需大规模预训练数据。

【方法概述 / Method】

EdgeCrafter的核心是ECDet检测模型，采用蒸馏得到的紧凑骨干网络，配合边缘友好的编码器-解码器架构。该方法通过任务专用蒸馏策略，将大型教师模型的任务特定知识迁移到小型ViT学生模型中，而非仅进行通用特征蒸馏。框架统一扩展至实例分割（ECInsSeg）和姿态估计（ECPose），保持一致的边缘高效设计理念。

【实验结果 / Results】

在COCO数据集上，ECDet-S仅用COCO标注数据、不到10M参数即达到51.7 AP；ECInsSeg在参数量显著少于RF-DETR的情况下取得可比性能；ECPose-X达到74.8 AP，大幅超越使用Objects365大规模预训练的YOLO26Pose-X（71.6 AP）。这些结果表明，经过适当设计的紧凑型ViT能够在边缘密集预测任务中成为CNN的实用替代方案。

【应用价值 / Applications】

EdgeCrafter为资源受限的边缘设备（如移动端、嵌入式系统、物联网设备）提供了高性能的密集预测解决方案，可广泛应用于实时目标检测、实例分割和人体姿态估计等场景。该研究打破了"ViT不适合边缘部署"的固有认知，为边缘AI应用的模型选型提供了新的技术路径，特别是在对预训练数据获取受限的实际生产环境中具有重要价值。
