---
title: "Long-LRM++: Preserving Fine Details in Feed-Forward Wide-Coverage Reconstruction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.10267"
published: "2026-03-18"
summarized: "2026-03-18T18:30:45.025068"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了Long-LRM++，一种用于前馈式大场景重建的新方法，旨在解决现有高斯溅射方法在直接预测数百万高斯参数时易产生模糊、特别是细结构（如文字）失真的问题，同时克服隐式表示方法（如LVSM和LaCT）因逐帧计算密集型解压而无法实时渲染的局限。该方法采用半显式场景表示结合轻量级解码器，在DL3DV数据集上达到与LaCT相当的渲染质量，同时实现A100 GPU上14 FPS的实时渲染。此外，该方法可扩展至64张输入图像，并在ScanNetv2上展现出优于直接高斯深度渲染的新视角深度预测能力。

【方法概述 / Method】

Long-LRM++采用半显式场景表示（semi-explicit scene representation），将场景信息编码为紧凑的隐式特征，但通过轻量级解码器而非完整的Transformer或TTT主干网络进行解码，从而在保留隐式表示高保真优势的同时避免逐帧重型计算。该方法支持多达64张950×540分辨率的输入图像，通过单次前向传播实现360°场景级重建。

【实验结果 / Results】

在DL3DV数据集上，Long-LRM++达到了与LaCT相当的渲染质量，同时实现14 FPS的实时渲染速度，显著优于隐式方法的计算效率；该方法成功扩展至64输入视图，展现出良好的输入长度泛化能力；在ScanNetv2数据集上，其新视角深度预测性能优于从高斯直接渲染深度的方法。大量消融实验验证了框架各组件的有效性。

【应用价值 / Applications】

Long-LRM++适用于需要高保真、实时渲染的宽覆盖场景重建应用，如虚拟现实/增强现实内容生成、大型场景快速三维建模、机器人导航中的实时深度感知等。其前馈式推理特性使其特别适合边缘设备部署和需要快速响应的交互式应用，同时支持长视频序列或密集采集数据的高效处理。
