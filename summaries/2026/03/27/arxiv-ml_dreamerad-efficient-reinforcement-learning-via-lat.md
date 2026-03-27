---
title: "DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24587"
published: "2026-03-27"
summarized: "2026-03-28T07:12:00.725660"
ai_provider: "openai"
---

【论文摘要 / Abstract】
DreamerAD 是首个面向自动驾驶的潜变量世界模型强化学习框架，通过将扩散采样从 100 步压缩至 1 步，实现了 80 倍加速同时保持视觉可解释性。该框架解决了现有像素级扩散世界模型因多步推理延迟（2秒/帧）而无法支持高频 RL 交互的问题，在 NavSim v2 基准上达到 87.7 EPDMS 的最先进性能，证明了潜空间 RL 在自动驾驶中的有效性。

【方法概述 / Method】
DreamerAD 采用三项核心机制：（1）shortcut forcing 通过递归多分辨率步长压缩降低采样复杂度；（2）自回归密集奖励模型直接在潜表征上运行以实现细粒度信用分配；（3）面向 GRPO 的高斯词表采样将探索约束在物理可行的轨迹空间。该方法利用视频生成模型的去噪潜特征，避免了像素级扩散的高昂推理成本。

【实验结果 / Results】
DreamerAD 在 NavSim v2 自动驾驶仿真基准上取得 87.7 EPDMS 分数，达到当前最优水平。相比传统像素级扩散世界模型，推理速度提升 80 倍（从 100 步扩散采样降至单步），同时维持了视觉可解释性，实现了高效与可解释性的统一。

【应用价值 / Applications】
该研究为自动驾驶领域提供了安全高效的离线 RL 训练范式，可在避免真实道路测试风险的前提下，基于真实驾驶数据训练决策策略。其高速推理特性支持高频闭环交互，适用于仿真平台训练、策略预训练及安全关键场景的快速策略迭代，有望降低自动驾驶系统开发的时间与经济成本。
