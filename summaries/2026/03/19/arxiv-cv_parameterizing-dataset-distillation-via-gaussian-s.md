---
title: "Parameterizing Dataset Distillation via Gaussian Splatting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2509.26219"
published: "2026-03-19"
summarized: "2026-03-19T16:26:34.927784"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了GSDD（Gaussian Splatting for Dataset Distillation），一种基于高斯溅射的新型数据集参数化技术，用于数据集蒸馏任务。该方法通过CUDA并行批处理渲染实现高效训练，利用高斯基元以稀疏而表达力强的方式捕获图像特征，在有限存储预算下显著提升蒸馏数据集的多样性。GSDD在多个标准基准测试以及ImageNet-1K大规模数据集和视频蒸馏任务上均取得优异性能，同时具备良好的计算效率、内存优化和跨GPU架构稳定性。

【方法概述 / Method】
GSDD将3D高斯溅射技术适配到2D图像数据集蒸馏中，使用可学习的高斯基元（包含位置、协方差、颜色和不透明度参数）来表示每个蒸馏样本，替代传统的像素级存储。该方法通过CUDA优化的可微分溅射算子实现批量并行渲染，并采用紧凑的参数化结构避免复杂辅助模块，在保持高表征能力的同时降低冗余。

【实验结果 / Results】
GSDD在CIFAR-10、CIFAR-100、Tiny ImageNet等标准基准上达到竞争性或最先进的性能，在ImageNet-1K上每类仅用10张图像时显著优于现有方法。视频蒸馏实验表明该方法可扩展到时序数据，且综合基准测试显示其具有低计算开销、小内存占用和良好的跨架构泛化能力。

【应用价值 / Applications】
GSDD适用于需要高效数据压缩的场景，如边缘设备部署、隐私保护的数据共享、以及大规模预训练数据的高效存储。其高斯参数化表示特别适合存储受限但需要保留丰富训练信息的应用，同时可扩展至视频理解、持续学习等需要处理高维数据的任务。
