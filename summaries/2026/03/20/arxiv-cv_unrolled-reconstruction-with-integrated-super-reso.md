---
title: "Unrolled Reconstruction with Integrated Super-Resolution for Accelerated 3D LGE MRI"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18309"
published: "2026-03-20"
summarized: "2026-03-20T15:07:26.742432"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种混合展开重建框架，用于加速3D晚期钆增强（LGE）MRI成像。该方法将增强深度超分辨率（EDSR）网络嵌入到模型优化循环的每次迭代中，替代传统的近端算子，实现超分辨率增强与数据一致性约束的联合优化。实验表明，该方法在不同加速因子下均优于压缩感知、MoDL和自引导DIP等基线方法，在PSNR、SSIM指标以及左心房精细结构分割性能上均有显著提升。

【方法概述 / Method】

作者将EDSR超分辨率网络集成到展开式模型驱动重建框架中，作为迭代优化过程的近端算子，使网络在保持物理数据一致性的同时进行端到端训练。该方法在预临床3D LGE数据集上进行回顾性欠采样训练，实现了重建与超分辨率的协同优化。

【实验结果 / Results】

与标准展开重建相比，所提方法在各加速因子下持续提高PSNR和SSIM指标，并能更好地保留心脏细微结构。此外，该方法显著提升了左心房（LA）分割性能，验证了其在下游临床任务中的有效性。

【应用价值 / Applications】

该研究为加速3D LGE MRI提供了更高效的重建方案，可在减少扫描时间的同时保持图像质量，适用于心律失常等心脏疾病的临床诊断。其集成超分辨率的展开框架思路也可推广至其他需要高分辨率重建的快速MRI应用场景。
