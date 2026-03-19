---
title: "Training-free Detection of Generated Videos via Spatial-Temporal Likelihoods"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15026"
published: "2026-03-19"
summarized: "2026-03-19T14:20:25.781438"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了STALL（Spatial-Temporal Likelihoods），一种无需训练、理论可解释的视频生成检测方法。该方法通过概率框架联合建模视频的空间和时间特征，利用真实数据统计对视频进行似然评分，实现零样本、模型无关的检测。实验表明，STALL在两个公开基准测试以及新提出的ComGenVid基准（包含最新生成模型）上均优于现有的图像和视频基线方法。

【方法概述 / Method】

STALL基于概率框架，通过估计视频在真实数据分布下的空间-时间联合似然来检测生成视频。该方法无需任何合成数据训练，直接利用预训练的概率模型（如标准化流或扩散模型）计算视频帧的空间似然以及帧间的时间一致性似然，并将两者结合得到最终检测分数。

【实验结果 / Results】

STALL在多个基准测试上 consistently 超越现有方法，包括传统图像检测器和有监督视频检测器。在新提出的ComGenVid基准（涵盖当前最先进的视频生成模型）上，该方法展现出优异的泛化能力，能够有效检测来自未见过生成器的合成视频，解决了监督方法泛化性差的核心问题。

【应用价值 / Applications】

该研究为深度伪造视频检测提供了实用解决方案，特别适用于快速迭代的生成模型环境，无需针对每个新模型重新训练。可广泛应用于社交媒体平台的内容审核、新闻真实性验证、司法取证等场景，帮助缓解AI生成视频带来的虚假信息传播风险。
