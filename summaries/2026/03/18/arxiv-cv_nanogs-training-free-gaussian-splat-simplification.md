---
title: "NanoGS: Training-Free Gaussian Splat Simplification"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16103"
published: "2026-03-18"
summarized: "2026-03-18T18:05:38.414148"
ai_provider: "openai"
---

【论文摘要 / Abstract】
NanoGS 提出了一种无需训练的轻量级 3D 高斯点云（3DGS）简化框架，通过将简化问题转化为稀疏空间图上的局部成对合并，避免了传统方法依赖 GPU 密集型训练优化的局限。该方法采用质量守恒的矩匹配技术将两个高斯合并为单一基元，并通过有原则的合并代价函数评估合并质量。NanoGS 可直接在现有 3DGS 模型上运行，在 CPU 上高效执行，同时保持标准 3DGS 参数化，实现了存储成本大幅降低与高渲染保真度的兼顾。

【方法概述 / Method】
NanoGS 将高斯基元简化表述为稀疏空间图上的局部成对合并问题，通过限制合并候选为局部邻域并高效选择兼容配对来降低计算复杂度。核心操作包括：使用质量守恒的矩匹配（mass preserved moment matching）将两个高斯近似为单一基元，以及通过原始混合分布与其近似之间的合并代价（merge cost）来评估合并质量。

【实验结果 / Results】
实验表明，NanoGS 能够显著减少高斯基元数量（primitive count），同时保持较高的渲染保真度；由于完全在 CPU 上运行且无需图像监督的优化，该方法在计算效率上具有明显优势，可直接应用于现有预训练的高斯点云模型。

【应用价值 / Applications】
NanoGS 为 3D 高斯点云的存储压缩和传输优化提供了实用解决方案，特别适用于需要快速部署的边缘设备、网络传输受限的远程渲染场景，以及需要处理大量预训练 3DGS 资产的内容生产管线；其无需训练、即插即用的特性使其易于集成到现有的实时渲染系统中。
