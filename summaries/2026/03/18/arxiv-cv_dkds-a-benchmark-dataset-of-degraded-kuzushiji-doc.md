---
title: "DKDS: A Benchmark Dataset of Degraded Kuzushiji Documents with Seals for Detection and Binarization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.09117"
published: "2026-03-18"
summarized: "2026-03-18T18:28:42.942278"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了DKDS（Degraded Kuzushiji Documents with Seals）数据集，这是一个专门针对退化古日文草书文档及印章检测与二值化任务的新基准。现有OCR方法在处理干净的Kuzushiji文档时表现良好，但难以应对文档退化和印章噪声等实际挑战，而DKDS填补了这一空白。该数据集由 trained Kuzushiji专家协助构建，包含两个评测赛道：Kuzushiji字符与印章检测、文档二值化，并提供了基于YOLO的检测基线和多种二值化方法的对比结果。

【方法概述 / Method】

论文采用专家辅助的数据集构建流程，系统性地收集并标注了包含退化现象和印章噪声的Kuzushiji历史文档。在检测任务中，使用多个近期YOLO版本作为基线方法；在二值化任务中，综合评估了传统算法、K-means聚类增强的传统算法、两种SOTA GAN方法，以及作者提出的改进条件GAN（cGAN）方法。

【实验结果 / Results】

YOLO系列模型在Kuzushiji字符和印章检测任务上建立了性能基准；在二值化赛道中，改进的cGAN方法相比传统算法和现有GAN方法展现出更优的文档前景背景分离效果。具体量化指标和完整实验对比详见论文原文及开源代码仓库。

【应用价值 / Applications】

DKDS数据集可直接支撑历史文献数字化保护、文化遗产自动转录系统的研发，帮助解决日本前现代草书文献因专家稀缺而面临的理解危机。该基准也为文档图像分析、噪声鲁棒OCR等领域的算法研究提供了标准化的评测平台，推动深度学习在真实退化历史文档处理中的应用落地。
