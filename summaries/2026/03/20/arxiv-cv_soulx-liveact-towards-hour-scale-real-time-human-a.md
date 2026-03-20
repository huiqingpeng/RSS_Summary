---
title: "SoulX-LiveAct: Towards Hour-Scale Real-Time Human Animation with Neighbor Forcing and ConvKV Memory"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.11746"
published: "2026-03-20"
summarized: "2026-03-20T16:18:55.054867"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了SoulX-LiveAct，一种面向小时级实时人体动画生成的自回归扩散模型。针对现有方法中强制学习策略导致扩散状态不匹配、历史表征无界增长两大核心问题，作者设计了Neighbor Forcing策略和ConvKV记忆机制，实现了训练收敛稳定、推理内存恒定的无限视频生成。实验表明，该方法在双卡H100/H200上可达20 FPS实时流式推理，并在唇形同步、动画质量和情感表现力上达到SOTA性能。

【方法概述 / Method】

Neighbor Forcing是一种扩散步骤一致的自回归形式，将时序相邻帧作为同噪声条件下的"潜在邻居"进行传播，提供分布对齐的稳定学习信号同时保持AR链的漂移特性。ConvKV记忆机制则将因果注意力中的键值对压缩为固定长度表征，突破短期运动帧记忆限制，实现真正的无限长度视频生成。

【实验结果 / Results】

LiveAct支持小时级实时人体动画生成，在仅两块NVIDIA H100或H200 GPU上实现20 FPS实时流式推理。定量评估显示，该方法在唇同步精度、人体动画质量和情感表现力方面达到最先进的性能水平，同时具有最低的推理成本，显著优于现有自回归扩散方法。

【应用价值 / Applications】

该技术可广泛应用于实时数字人直播、虚拟主播、远程会议替身、游戏NPC动画等需要长时间连续生成的场景。其恒定内存特性和低硬件门槛（双卡H100/H200）使小时级实时人体动画首次具备实际部署可行性，有望推动实时生成式AI在娱乐、社交、企业服务等领域的规模化应用。
