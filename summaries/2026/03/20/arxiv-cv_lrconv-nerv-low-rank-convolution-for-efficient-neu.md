---
title: "LRConv-NeRV: Low Rank Convolution for Efficient Neural Video Compression"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18261"
published: "2026-03-20"
summarized: "2026-03-20T15:07:01.629576"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了 LRConv-NeRV，一种高效的神经视频表示方法，通过用结构化低秩可分离卷积替代部分稠密 3×3 卷积层来降低计算开销。该方法支持从解码器深层到浅层的渐进式低秩分解，实现重建质量与效率的可控权衡。实验表明，仅对最后一层应用低秩卷积即可将解码器复杂度降低 68%，同时保持 negligible 的质量损失和约 9.2% 的码率缩减，为资源受限环境下的神经视频解码提供了可行的架构替代方案。

【方法概述 / Method】
LRConv-NeRV 采用低秩卷积分解技术，将选定的稠密 3×3 卷积层替换为低秩可分离卷积（low-rank separable convolutions），并在解码器架构中进行端到端训练。该方法通过从最大（最深）到较早解码器阶段的渐进式低秩分解策略，实现对计算效率与重建质量的灵活控制。

【实验结果 / Results】
仅对最终解码器阶段应用 LRConv 时，解码器复杂度从 201.9 GFLOPs 降至 64.9 GFLOPs（降低 68%），模型大小减少 9.3%，重建质量损失可忽略，并实现约 9.2% 的码率降低。在 INT8 后训练量化条件下，LRConv-NeRV 能保持接近稠密 NeRV 基线的重建质量；而早期阶段的激进分解会导致质量不成比例下降。与现有工作相比，在层对齐设置下实现了更优的效率-质量权衡，PSNR/MS-SSIM 更高且时间稳定性更好，LPIPS 分析显示时间闪烁与基线相当。

【应用价值 / Applications】
该研究适用于边缘设备、移动终端等资源受限环境下的高效视频解码场景，特别是在需要低精度量化（如 INT8）部署的实时视频流传输和存储应用中。LRConv-NeRV 为神经视频编解码器的实际工程落地提供了计算效率高、模型轻量化的架构选择，有望推动神经表示视频压缩在消费级硬件上的普及应用。
