---
title: "DCARL: A Divide-and-Conquer Framework for Autoregressive Long-Trajectory Video Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24835"
published: "2026-03-27"
summarized: "2026-03-28T07:17:27.453538"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DCARL，一种新颖的分治自回归框架，用于解决长轨迹视频生成中的视觉漂移和可控性差的问题。该方法结合了分治策略的结构稳定性与视频扩散模型的高保真生成能力，通过专门的关键帧生成器建立全局一致的结构锚点，再利用插值生成器以自回归方式合成密集帧。在大规模互联网长轨迹视频数据集上训练后，该方法在视觉质量（FID/FVD）和相机 adherence（ATE/ARE）方面均优于现有最优的自回归和分治基线方法，能够稳定生成长达32秒的高保真长轨迹视频。

【方法概述 / Method】
DCARL采用两阶段分治策略：首先，关键帧生成器（Keyframe Generator）在无时间压缩的条件下训练，生成全局一致的关键帧作为结构锚点；其次，插值生成器（Interpolation Generator）以重叠片段的自回归方式合成密集帧，利用关键帧提供全局上下文，同时使用单个干净的前一帧保证局部连贯性。

【实验结果 / Results】
实验表明，DCARL在视觉质量指标（FID和FVD）和相机 adherence 指标（ATE和ARE）上均显著优于当前最先进的自回归和分治基线方法。该方法成功实现了长达32秒的长轨迹视频的稳定高保真生成，有效缓解了现有方法中的视觉漂移问题。

【应用价值 / Applications】
DCARL可广泛应用于世界建模、自动驾驶模拟、机器人学习等需要长时序一致视频生成的场景。其稳定的长时间视频生成能力为虚拟环境构建、电影制作预览以及交互式内容创作提供了可靠的技术基础，有望推动具身智能和模拟器技术的发展。
