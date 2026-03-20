---
title: "OnlinePG: Online Open-Vocabulary Panoptic Mapping with 3D Gaussian Splatting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18510"
published: "2026-03-20"
summarized: "2026-03-20T15:10:58.913078"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了OnlinePG，首个基于3D高斯溅射（3D Gaussian Splatting）的在线开放词汇全景映射系统，解决了现有方法多为离线或缺乏实例级理解的问题。该系统采用高效的局部到全局范式与滑动窗口机制，通过3D分割聚类图融合几何与语义线索构建局部一致地图，并利用双向二分3D高斯实例匹配更新全局地图。实验表明，该方法在在线方法中性能最优，同时保持实时效率。

【方法概述 / Method】
OnlinePG采用滑动窗口驱动的局部到全局范式：在局部层面，构建3D分割聚类图联合利用几何和语义线索，将窗口内不一致的分段融合为完整实例；在全局层面，为局部3D高斯地图构建带空间属性的显式网格，通过鲁棒的双向二分3D高斯实例匹配融合到全局地图，最终利用融合的视觉语言模型（VLM）特征实现开放词汇场景理解。

【实验结果 / Results】
在多个广泛使用的数据集上的大量实验表明，OnlinePG在在线方法中取得了最优性能，同时保持了实时计算效率，验证了其在开放词汇场景理解和全景实例分割任务上的有效性。

【应用价值 / Applications】
该研究对具身智能（embodied AI）和机器人任务具有重要价值，使机器人能够在实时在线条件下感知环境、理解开放词汇指令并与场景进行交互，适用于自主导航、人机交互和动态环境理解等实际应用场景。
