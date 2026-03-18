---
title: "DST-Net: A Dual-Stream Transformer with Illumination-Independent Feature Guidance and Multi-Scale Spatial Convolution for Low-Light Image Enhancement"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16482"
published: "2026-03-18"
summarized: "2026-03-18T18:14:19.074774"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种用于低光照图像增强的双流Transformer网络（DST-Net），通过光照无关的信号先验引导和多尺度空间卷积来解决现有方法中存在的固有信号先验严重丢失问题。该方法设计了融合高斯差分（DoG）、LAB色彩空间变换和VGG-16的特征提取模块，以解耦的光照无关特征作为信号先验指导增强过程；同时构建了双流交互架构，利用跨模态注意力机制动态修正退化信号表示。实验表明，DST-Net在LOL数据集上达到25.64 dB的PSNR，并在LSRW数据集上展现出良好的跨场景泛化能力。

【方法概述 / Method】
DST-Net采用双流Transformer架构，核心包含两个创新模块：一是特征提取模块，整合DoG、LAB变换和VGG-16提取纹理，生成光照无关的信号先验；二是多尺度空间融合块（MSFB），采用伪3D和3D梯度算子卷积，通过显式梯度算子恢复高频边缘，并利用多尺度空间卷积捕捉通道间空间相关性。网络通过跨模态注意力机制实现先验特征与增强图像的动态交互，最终通过可微分曲线估计实现迭代增强。

【实验结果 / Results】
DST-Net在主观视觉质量和客观指标上均取得优异性能：在LOL数据集上PSNR达到25.64 dB，显著优于现有方法；在LSRW数据集上的验证进一步证实了其强大的跨场景泛化能力。消融研究验证了各模块设计的有效性，证明光照无关先验引导和多尺度空间卷积对提升增强质量的关键作用。

【应用价值 / Applications】
该研究可广泛应用于夜间监控、自动驾驶视觉感知、移动设备摄影、医学影像处理等需要在低光照环境下获取高质量图像的场景。DST-Net的光照无关特性使其具备跨场景鲁棒性，适用于光照条件剧烈变化的实际环境，为视觉传感器在极端条件下的可靠工作提供了技术支撑。
