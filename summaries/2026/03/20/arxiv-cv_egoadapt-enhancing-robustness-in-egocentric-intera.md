---
title: "EgoAdapt: Enhancing Robustness in Egocentric Interactive Speaker Detection Under Missing Modalities"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18082"
published: "2026-03-20"
summarized: "2026-03-20T16:07:36.088187"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了EgoAdapt框架，用于解决第一人称视角（egocentric）交互式说话人检测（TTM任务）中视觉数据缺失、头部姿态信息被忽略以及背景噪声等实际挑战。该框架通过整合头部朝向（非语言线索）和唇部运动（语言线索）实现全面的言语与非言语信号理解，并引入模态缺失感知机制动态调整系统响应。在Ego4D数据集TTM基准测试上，EgoAdapt以67.39%的mAP和62.01%的准确率显著超越现有最优方法，准确率提升达4.96%。

【方法概述 / Method】
EgoAdapt包含三个核心模块：视觉说话人目标识别（VSTR）模块同步捕捉头部朝向和唇部运动作为互补线索；并行共享权重音频（PSA）编码器增强噪声环境下的音频特征提取；视觉模态缺失感知（VMMA）模块实时估计各帧模态存在状态并自适应调整融合策略。

【实验结果 / Results】
在Ego4D数据集TTM基准上，EgoAdapt达到67.39%的平均精度（mAP）和62.01%的准确率（Acc），相比当前最先进方法分别提升1.56%和4.96%，验证了其在模态不完整场景下的鲁棒性优势。

【应用价值 / Applications】
该研究可应用于智能眼镜、AR/VR设备等第一人称视角可穿戴系统的实时社交交互理解，帮助用户识别对话对象；其模态自适应机制对实际环境中传感器遮挡、光照变化等导致的视觉缺失具有重要容错价值，为人机协作和社交辅助机器人提供可靠的感知基础。
