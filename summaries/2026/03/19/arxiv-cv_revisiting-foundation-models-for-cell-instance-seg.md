---
title: "Revisiting foundation models for cell instance segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17845"
published: "2026-03-19"
summarized: "2026-03-19T16:17:28.382254"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文系统评估了多种基础模型在细胞实例分割任务上的表现，包括专门针对显微图像的细胞分割模型（CellPoseSAM、CellSAM、μSAM）和通用分割模型（SAM、SAM2、SAM3）。作者提出了一种名为自动提示生成（APG）的新策略，能够显著提升基于SAM的显微图像分割效果，使μSAM达到与当前最先进模型CellPoseSAM相竞争的性能。该研究为SAM风格模型在显微图像领域的适配策略提供了重要见解，并为构建更强大的显微图像基础模型指明了方向。

【方法概述 / Method】
论文在多样化的（光）显微图像数据集上对细胞、细胞核和类器官分割任务进行了全面基准测试。核心创新是提出自动提示生成（APG）策略，通过自动生成提示来优化SAM系列模型的分割性能，该方法以μSAM作为基础模型进行改进。

【实验结果 / Results】
APG策略在μSAM上持续提升了分割效果，使其性能与当前最先进的CellPoseSAM模型相媲美。研究还揭示了SAM、SAM2、SAM3等通用基础模型与专门化细胞分割模型在不同显微图像任务上的性能差异，为模型选择提供了实证依据。

【应用价值 / Applications】
该研究为生物医学图像分析领域提供了经过验证的模型选择指南和实用的模型改进策略，可直接应用于细胞生物学、药物筛选和组织工程中的自动化细胞定量分析。APG方法可集成到现有的显微图像分析流程中，提升分割精度并减少对人工标注的依赖。
