---
title: "Parameter-Efficient Modality-Balanced Symmetric Fusion for Multimodal Remote Sensing Semantic Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17705"
published: "2026-03-19"
summarized: "2026-03-19T15:16:34.532041"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MoBaNet，一种参数高效且模态平衡的对称融合框架，用于多模态遥感语义分割。该方法基于冻结的视觉基础模型（VFM）主干，采用对称双流架构，通过跨模态提示注入适配器（CPIA）实现深度语义交互，并引入差分引导门控融合模块（DGFM）自适应融合特征。此外，模态条件随机掩码（MCRM）策略有效缓解了模态不平衡问题，在ISPRS Vaihingen和Potsdam基准上取得了最先进的性能，且可训练参数显著少于全微调方法。

【方法概述 / Method】
MoBaNet采用对称双流架构，在保持VFM主干大部分冻结的同时最小化可训练参数。核心组件包括：（1）跨模态提示注入适配器（CPIA），通过生成共享提示并注入瓶颈适配器实现深度语义交互；（2）差分引导门控融合模块（DGFM），利用跨模态差异显式指导特征选择，生成紧凑且具有判别性的多模态表示；（3）模态条件随机掩码（MCRM），在训练期间随机掩蔽单一模态并对模态特定分支施加硬像素辅助监督，以缓解模态不平衡。

【实验结果 / Results】
在ISPRS Vaihingen和Potsdam两个标准遥感语义分割基准数据集上，MoBaNet取得了最先进的性能，同时可训练参数数量显著少于全微调方法。实验结果验证了该方法在鲁棒且平衡的多模态融合方面的有效性，表明参数效率与模态平衡可以兼得。

【应用价值 / Applications】
该研究适用于需要融合多源遥感数据（如RGB光学图像与LiDAR/DSM高程数据）的语义分割任务，可应用于城市规划、土地利用分类、灾害监测和环境管理等领域。其参数高效特性使得在计算资源受限的平台上部署大型视觉基础模型成为可能，而模态平衡机制确保了辅助模态的有效利用，提升了场景理解的准确性和鲁棒性。
