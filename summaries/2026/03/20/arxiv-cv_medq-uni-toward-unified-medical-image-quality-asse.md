---
title: "MedQ-UNI: Toward Unified Medical Image Quality Assessment and Restoration via Vision-Language Modeling"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18465"
published: "2026-03-20"
summarized: "2026-03-20T15:09:38.769654"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出MedQ-UNI，首个统一医学图像质量评估（Med-IQA）与图像复原（Med-IR）的视觉-语言模型，突破现有方法局限于特定模态或退化类型的瓶颈。该模型采用"先评估后复原"范式，通过结构化自然语言描述显式利用质量评估结果指导跨模态、跨退化类型的图像复原。在包含50K配对样本的多模态数据集上训练后，单一MedQ-UNI模型无需任务特定适配即达到所有任务的最优性能，验证了显式质量理解对复原保真度和可解释性的显著提升。

【方法概述 / Method】

MedQ-UNI采用多模态自回归双专家架构，两个专家共享注意力机制：质量评估专家首先生成结构化自然语言退化描述，复原专家随后以该描述为条件执行针对性图像复原。模型通过联合训练Med-IQA与Med-IR任务，实现质量理解与复原操作的深度耦合。

【实验结果 / Results】

实验涵盖CT、MRI、X-ray三种模态及五种复原任务（包括去噪、超分辨率、金属伪影去除等）。MedQ-UNI在全部任务上取得当前最优性能，同时生成质量更高的退化描述；单一统一模型超越各任务专用模型，证明了跨任务泛化能力。

【应用价值 / Applications】

该研究为临床影像处理提供通用智能平台，可自动识别并修复多模态医学图像中的各类退化问题，减少人工筛选和专用模型部署成本。生成的结构化质量描述增强了AI决策透明度，有助于临床质量控制和影像诊断流程优化，推动医学影像AI的标准化应用。
