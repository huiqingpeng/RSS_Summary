---
title: "DROID-SLAM in the Wild"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19076"
published: "2026-03-20"
summarized: "2026-03-20T16:04:04.343503"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DROID-SLAM in the Wild，一个鲁棒的实时RGB SLAM系统，通过可微分的Uncertainty-aware Bundle Adjustment处理动态环境。该方法利用多视角视觉特征不一致性估计逐像素不确定性，在未知动态物体或高度杂乱场景中实现鲁棒跟踪与重建。系统在杂乱动态场景中达到了最先进的相机位姿和场景几何估计精度，同时以约10 FPS实时运行。

【方法概述 / Method】
核心方法是可微分的Uncertainty-aware Bundle Adjustment，通过检测多视角视觉特征的不一致性来估计逐像素的不确定性权重。该不确定性估计机制使系统能够自动识别并降低动态区域在优化过程中的影响，无需预定义的动态先验。

【实验结果 / Results】
系统在真实世界杂乱动态场景中实现了最先进的相机位姿和场景几何估计性能。算法以约10 FPS的速度实时运行，在动态物体存在的情况下仍保持鲁棒跟踪，避免了传统SLAM方法的典型跟踪失败问题。

【应用价值 / Applications】
该研究适用于机器人导航、自动驾驶和AR/VR等需要在真实动态环境中运行的应用场景。系统无需预先知道动态物体的类别或运动模式，可直接部署于复杂的真实世界环境，显著提升了SLAM技术在非受控场景中的实用性和可靠性。
