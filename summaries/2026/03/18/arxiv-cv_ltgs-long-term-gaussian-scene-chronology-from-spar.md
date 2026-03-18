---
title: "LTGS: Long-Term Gaussian Scene Chronology From Sparse View Updates"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.09881"
published: "2026-03-18"
summarized: "2026-03-18T18:27:52.967152"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了LTGS（Long-Term Gaussian Scene Chronology），一种能够从稀疏视角更新中建模场景长期演化的3D高斯表示方法。该方法通过构建可复用的模板高斯（template Gaussians）作为结构先验，实现了对日常环境中突发运动和细微变化的鲁棒跟踪。训练完成后，该框架可通过简单变换泛化到多个时间步，显著提升了3D环境时序演化的可扩展性，并在新收集的真实世界数据集上验证了其实用性。

【方法概述 / Method】

LTGS以不完整的非结构化3D高斯溅射（3DGS）表示为起点，将场景中的物体建模为模板高斯作为共享的结构可复用先验。针对时变环境，设计了一个精炼流程，利用少量观测样本对先验进行调制适配，从而处理稀疏捕获下的场景变化。

【实验结果 / Results】

实验表明，LTGS在重建质量上优于其他基线方法，同时实现了快速轻量的场景更新。作者还构建了专门的真实世界数据集来评估稀疏捕获设置下的长期场景变化，验证了该流程在实际应用中的可行性。

【应用价值 / Applications】

LTGS适用于需要长期监测和可视化真实世界环境的场景，如智能家居监控、城市数字孪生、以及日常环境的渐进式3D重建等。其稀疏视角更新的特性使其特别适合普通用户通过日常随意拍摄即可维护和更新场景表示，降低了密集数据采集的门槛。
