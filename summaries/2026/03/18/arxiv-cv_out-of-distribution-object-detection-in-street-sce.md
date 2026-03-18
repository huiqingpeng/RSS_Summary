---
title: "Out-of-Distribution Object Detection in Street Scenes via Synthetic Outlier Exposure and Transfer Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16122"
published: "2026-03-18"
summarized: "2026-03-18T18:06:03.698106"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SynOE-OD框架，解决了分布外（OOD）目标检测中OOD对象被检测器完全遗漏并错误归类为背景的关键问题。该框架利用Stable Diffusion等生成模型和开放词汇目标检测器（OVODs）生成语义有意义的合成异常样本进行训练，实现了单一检测器对ID和OOD对象的统一检测。在街道场景OOD目标检测基准上，该方法达到了最先进的平均精度，显著优于GroundingDINO等OVODs的零样本性能。

【方法概述 / Method】
SynOE-OD采用合成异常暴露策略，结合强大的生成式模型（如Stable Diffusion）生成对象级别的合成OOD数据，并利用开放词汇检测器进行语义对齐。通过迁移学习将这些合成数据融入训练过程，在保持ID任务性能的同时增强模型对OOD对象的检测鲁棒性，无需复杂的辅助分支或架构修改。

【实验结果 / Results】
该方法在已建立的街道场景OOD目标检测基准上取得了最先进的平均精度，有效解决了GroundingDINO等OVODs在零样本OOD检测中表现有限的问题。实验表明，合成异常暴露训练能够显著提升检测器对原本被静默忽略的OOD对象的定位与识别能力。

【应用价值 / Applications】
该研究对自动驾驶和智能交通系统具有重要价值，可提升车辆在真实复杂街道场景中对意外物体（如异常障碍物、未训练类别）的感知安全性。同时，该框架为OOD检测提供了一种统一、可扩展的解决方案，可推广至其他需要可靠开集识别的计算机视觉应用场景。
