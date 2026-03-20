---
title: "End-to-End QGAN-Based Image Synthesis via Neural Noise Encoding and Intensity Calibration"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18554"
published: "2026-03-20"
summarized: "2026-03-20T16:08:42.764054"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ReQGAN，一种端到端的量子生成对抗网络框架，能够使用单个D量子比特电路直接生成完整的N=2^D像素图像，解决了现有QGAN依赖经典后处理或分块方法的问题。该框架通过可学习的神经噪声编码器实现自适应量子态制备，并引入可微分的强度校准模块将量子测量结果映射到稳定的像素强度空间。实验表明，ReQGAN在严格的量子比特预算下实现了稳定的训练和有效的图像合成，消融研究验证了各组件的贡献。

【方法概述 / Method】
ReQGAN核心创新包括两个模块：神经噪声编码器（Neural Noise Encoder）替代传统的刚性经典-量子噪声接口，实现自适应的量子态制备；强度校准模块（Intensity Calibration）作为可微分层，将归一化的量子测量统计量映射到目标像素强度分布。整个框架采用端到端训练，使D量子比特量子电路直接输出完整图像而非局部补丁。

【实验结果 / Results】
在MNIST和Fashion-MNIST数据集上的实验表明，ReQGAN在有限量子比特（如D=8对应256像素）条件下实现了稳定的GAN训练收敛和高质量的图像生成。消融研究证实，移除神经噪声编码器或强度校准模块均会导致训练不稳定或图像质量显著下降，验证了这两个组件对端到端量子图像生成的必要性。

【应用价值 / Applications】
该研究为近中期量子设备上的实用化图像生成提供了可行路径，可应用于量子机器学习中的数据增强、隐私保护生成建模以及量子-经典混合计算系统。其端到端设计减少了对经典后处理的依赖，有助于推动量子生成模型在资源受限场景下的实际部署，并为更大规模的量子图像合成奠定基础。
