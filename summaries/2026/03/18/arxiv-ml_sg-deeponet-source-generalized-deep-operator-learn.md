---
title: "SG-DeepONet: Source-generalized deep operator learning for full waveform inversion"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2408.08005"
published: "2026-03-18"
summarized: "2026-03-18T16:16:29.891172"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对全波形反演（FWI）中深度学习模型对震源条件泛化能力不足的问题，构建了首个系统性变化震源频率和水平位置的新数据集SVFWI，并提出了SG-DeepONet框架。该框架通过分支网络提取多尺度时频特征、主干网络嵌入震源物理参数、交互式解码网络实现非线性融合，显著提升了不同震源条件下的反演精度与鲁棒性。实验表明，SG-DeepONet在SVFWI的三个子集上均优于现有深度学习方法。

【方法概述 / Method】
SG-DeepONet基于DeepONet架构设计编码器-解码器框架：分支网络处理地震观测数据的多尺度时频特征，主干网络显式编码震源频率和位置等物理参数，交互式解码网络通过非线性融合机制实现高保真速度模型重建。该方法将物理参数嵌入与深度算子学习相结合，突破了固定震源假设的限制。

【实验结果 / Results】
在SVFWI数据集的三个子集（频率变化、位置变化及联合变化）上的 extensive 实验表明，SG-DeepONet在震源泛化任务中实现了 superior 的反演精度和鲁棒性。相比现有基于深度学习的FWI方法，该模型在多样化震源条件下展现出更强的泛化能力和更高的重建保真度。

【应用价值 / Applications】
该研究为实际地震勘探中震源条件复杂多变的场景提供了数据驱动解决方案，可提升野外地震数据反演的可靠性。SVFWI数据集为FWI领域的源泛化研究建立了标准化基准，SG-DeepONet框架可扩展至其他需要物理参数嵌入的地球物理反演问题，推动深度学习在勘探地球物理中的实用化进程。
