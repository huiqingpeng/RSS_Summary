---
title: "FatigueFormer: Static-Temporal Feature Fusion for Robust sEMG-Based Muscle Fatigue Recognition"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26841"
published: "2026-03-31"
summarized: "2026-04-01T07:19:57.252278"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了FatigueFormer，一种半端到端框架，通过显著性引导的特征分离与深度时序建模相结合，从表面肌电信号（sEMG）中学习可解释且可泛化的肌肉疲劳动态特征。该框架采用并行的基于Transformer的序列编码器分别捕获静态和时序特征动态，融合其互补表示以提升在不同最大自主收缩（MVC）水平下的性能稳定性。在包含30名受试者、跨越四个MVC水平（20-80%）的自采集数据集上，该方法达到了最先进的准确率，并在轻度疲劳条件下展现出强大的泛化能力。

【方法概述 / Method】
FatigueFormer采用显著性引导的特征分离策略，将sEMG信号分解为静态特征和时序特征两个并行分支，分别通过Transformer编码器进行处理。两个分支的输出经过融合模块整合，形成对肌肉疲劳状态的联合表征，从而实现对信号变异性和低信噪比条件的鲁棒适应。

【实验结果 / Results】
在30人四MVC水平（20-80%）的数据集评估中，FatigueFormer取得了最先进的识别准确率，并在轻度疲劳条件下表现出优异的泛化性能。注意力可视化分析揭示了不同特征组和时间窗口在 varying MVC 水平下的差异化贡献模式，为疲劳进展机制提供了可解释的洞察。

【应用价值 / Applications】
该研究可应用于运动医学、康复工程和人机交互等领域，为实时肌肉疲劳监测提供可靠的算法支持。其可解释性特征有助于临床医生和研究人员理解疲劳发展的生理机制，指导个性化训练方案制定和疲劳相关损伤的预防。
