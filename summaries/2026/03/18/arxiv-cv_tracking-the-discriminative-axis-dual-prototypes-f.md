---
title: "Tracking the Discriminative Axis: Dual Prototypes for Test-Time OOD Detection Under Covariate Shift"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15213"
published: "2026-03-18"
summarized: "2026-03-18T19:05:00.622531"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对测试时协变量偏移（covariate shift）下的分布外（OOD）检测问题，提出了一种名为DART的在线测试时方法。作者发现即使在协变量偏移条件下，偏移后的分布内（csID）和分布外（csOOD）样本在特征空间中仍沿一个判别轴保持可分离性。基于这一关键观察，DART通过动态追踪双原型（ID和OOD各一个）来恢复漂移的判别轴，并结合多层融合和翻转校正机制增强鲁棒性。在包含15种常见损坏类型（严重度5级）的广泛基准测试中，该方法相比基线方法在ImageNet-C vs. Textures-C上实现了15.32个百分点的AUROC提升和49.15个百分点的FPR@95TPR降低。

【方法概述 / Method】
DART是一种测试时在线OOD检测方法，核心在于动态维护两个原型向量（分别代表ID和OOD类别），通过追踪这两个原型之间的判别轴来适应不断变化的协变量偏移。方法采用多层特征融合以捕获不同层次的表征信息，并引入翻转校正机制防止原型方向错误反转，确保判别轴估计的稳定性。

【实验结果 / Results】
实验在多种挑战性基准上进行，所有数据集均经受15种常见损坏类型且严重度为5级的协变量偏移。结果表明DART显著优于现有基线方法，特别是在ImageNet-C与Textures-C的对比实验中，AUROC提升达15.32个百分点，FPR@95TPR降低达49.15个百分点，展现出强大的鲁棒检测性能。

【应用价值 / Applications】
该研究适用于真实世界中深度学习系统的可靠部署场景，特别是测试输入以流式混合方式到达、且同时受到环境协变量因素影响的动态环境，如自动驾驶、医学影像诊断和工业视觉检测等领域。DART为在持续变化环境中实现可信赖的OOD检测提供了有效解决方案，对提升AI系统的安全性和可靠性具有重要价值。
