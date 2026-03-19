---
title: "Domain and Task-Focused Example Selection for Data-Efficient Contrastive Medical Image Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2505.19208"
published: "2026-03-19"
summarized: "2026-03-19T16:24:49.893823"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了PolyCL，一种新颖的自监督对比学习框架，用于医学图像分割。该框架通过创新的代理任务学习上下文感知判别特征，无需像素级标注或复杂的数据增强。研究还创新性地将Segment Anything Model (SAM)集成到框架中，作为后处理精化模块和通过SAM 2的体积分割传播机制。在三个公开CT数据集上的实验表明，PolyCL在低数据和跨域场景下均优于全监督和自监督基线方法。

【方法概述 / Method】
PolyCL采用领域和任务聚焦的样本选择策略进行数据高效的对比学习，通过挖掘不同医学图像间的内在关系来学习分割相关的判别特征。该方法将SAM以两种方式整合：一是利用粗分割输出的边界框提示进行掩膜精化，二是通过SAM 2实现从单张标注2D切片到体积分割的传播。

【实验结果 / Results】
在三个公开CT数据集上的评估显示，PolyCL在低数据标注场景和跨域泛化任务中均显著优于现有的全监督和自监督基线方法。SAM的集成进一步提升了分割精度，特别是在边界细化和体积一致性方面。

【应用价值 / Applications】
该研究可广泛应用于医学影像分析中标注数据稀缺的临床场景，大幅降低像素级标注成本和时间消耗。SAM的集成使该方法能够高效扩展到三维体积分割任务，对放射科诊断、手术规划和病灶量化分析具有重要实用价值。
