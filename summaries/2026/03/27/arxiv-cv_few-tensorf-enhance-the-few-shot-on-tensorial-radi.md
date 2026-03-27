---
title: "Few TensoRF: Enhance the Few-shot on Tensorial Radiance Fields"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.25008"
published: "2026-03-27"
summarized: "2026-03-28T07:20:32.409815"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Few TensoRF，一种结合TensorRF高效张量表示与FreeNeRF频率驱动少样本正则化的3D重建框架。该方法通过引入频率掩码和遮挡掩码，在稀疏输入视角下显著提升了重建稳定性和质量，同时保持TensorRF约10-15分钟的快速训练时间。在Synthetic NeRF基准测试中，该方法将平均PSNR从21.45 dB提升至23.70 dB（微调版本达24.52 dB），并在THuman 2.0数据集上仅用8张输入图像即可实现27.37-34.00 dB的人体重建性能。

【方法概述 / Method】
Few TensoRF以TensorRF的CP分解张量辐射场为基础表示，并引入FreeNeRF的频率正则化策略，通过频率掩码控制高频成分的渐进学习，同时利用遮挡掩码处理视角稀疏导致的伪影问题。该方法在保持张量表示计算效率的同时，增强了模型对少样本输入的泛化能力。

【实验结果 / Results】
在Synthetic NeRF基准测试中，Few TensoRF相比基线TensorRF提升PSNR约2.25 dB，微调后进一步提升至24.52 dB；在THuman 2.0人体数据集上，使用仅8张输入图像即可达到27.37-34.00 dB的重建精度。整个训练过程保持在10-15分钟，实现了质量与效率的平衡。

【应用价值 / Applications】
该研究适用于需要快速3D重建且数据采集受限的场景，如移动端实时重建、历史文物数字化、医学影像三维可视化等领域。其少样本特性降低了对密集采集设备的依赖，而高效的训练速度使其适合实时交互应用和边缘计算部署。
