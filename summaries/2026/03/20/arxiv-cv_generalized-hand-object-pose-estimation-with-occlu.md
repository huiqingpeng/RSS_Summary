---
title: "Generalized Hand-Object Pose Estimation with Occlusion Awareness"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19013"
published: "2026-03-20"
summarized: "2026-03-20T15:18:10.723113"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了GenHOI框架，用于解决单张RGB图像中广义3D手-物体姿态估计的挑战性问题，特别是在严重遮挡情况下。该框架通过整合层次化语义知识与手部先验信息，增强模型在遮挡条件下的泛化能力。实验表明，该方法在DexYCB和HO3Dv2基准测试上达到了最先进的性能。

【方法概述 / Method】
GenHOI引入层次化语义提示，通过文本描述编码物体状态、手部构型和交互模式，使模型学习抽象的高层交互表示。同时采用多模态掩码建模策略，在RGB图像、预测点云和文本描述上进行遮挡推理，并利用手部先验作为稳定的空间参考来提取隐式交互约束。

【实验结果 / Results】
在具有挑战性的DexYCB和HO3Dv2基准数据集上进行了大量实验，GenHOI在手-物体姿态估计任务中取得了最先进的性能表现，证明了该方法在处理未见物体、新颖交互模式以及严重遮挡情况下的有效性。

【应用价值 / Applications】
该技术可广泛应用于增强现实/虚拟现实中的自然交互、机器人抓取操作、人机协作以及智能监控等领域，特别是在需要理解复杂手-物体交互且视觉信息不完整的实际场景中具有重要价值。
