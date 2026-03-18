---
title: "FSMC-Pose: Frequency and Spatial Fusion with Multiscale Self-calibration for Cattle Mounting Pose Estimation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16596"
published: "2026-03-18"
summarized: "2026-03-18T18:15:38.794016"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了FSMC-Pose，一种用于奶牛爬跨姿态估计的自顶向下框架，通过融合轻量级频域-空间特征提取网络CattleMountNet和多尺度自校准头SC2Head，有效解决了复杂背景遮挡和动物间重叠导致的姿态估计难题。研究构建了包含1176个爬跨实例的MOUNT-Cattle数据集，并与公开NWAFU-Cattle数据集联合训练。实验表明，该方法在保持实时推理速度的同时，以更低的计算量和参数量实现了优于强基线模型的精度，能够可靠地估计复杂环境下的奶牛爬跨姿态。

【方法概述 / Method】
FSMC-Pose采用两阶段设计：CattleMountNet作为主干网络，包含空间频率增强块（SFEBlock）用于分离目标与杂乱背景，以及感受野聚合块（RABlock）用于捕获多尺度上下文信息；SC2Head作为检测头，通过空间-通道自注意力机制建模依赖关系，并引入自校准分支缓解动物重叠时的结构错位问题。

【实验结果 / Results】
在MOUNT-Cattle与NWAFU-Cattle联合数据集上，FSMC-Pose相比强基线方法实现了更高的姿态估计精度，同时显著降低了计算开销和模型参数量；该方法可在普通GPU上实现实时推理，并通过大量实验和定性分析验证了其在复杂 cluttered 环境中对奶牛爬跨姿态的有效捕获能力。

【应用价值 / Applications】
该研究为奶牛发情监测提供了自动化视觉解决方案，爬跨姿态的准确识别可辅助牧场实现精准繁育管理，减少人工观察成本；轻量化设计使其易于部署于边缘计算设备，适用于规模化养殖场的实时健康与繁殖状态监控系统。
