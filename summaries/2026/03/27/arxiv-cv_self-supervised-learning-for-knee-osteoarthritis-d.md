---
title: "Self-Supervised Learning for Knee Osteoarthritis: Diagnostic Limitations and Prognostic Value of Uncurated Hospital Data"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24903"
published: "2026-03-27"
summarized: "2026-03-28T07:18:22.495383"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究评估了自监督学习（SSL）相对于ImageNet预训练初始化在膝骨关节炎（OA）诊断和预后建模中的改进效果。研究发现，尽管基于未筛选医院数据的多模态图像-文本SSL在诊断任务（Kellgren-Lawrence分级）中因数据偏倚（93%为KL 3级）表现不佳，但其在预后建模（4年结构发病和进展预测）中显著优于ImageNet基线，外部验证AUROC达0.701（对比0.599），表明未筛选医院数据虽不适合诊断任务，但对预后预测具有重要价值。

【方法概述 / Method】
研究比较了两种自监督预训练策略：（1）基于OAI、MOST和NYU队列膝关节X光片的图像-only SSL；（2）基于未筛选医院膝关节X光片与放射科医师报告配对的多模态图像-文本SSL。通过在冻结编码器（线性探测）和完全微调两种设置下评估模型性能，并与ImageNet预训练基线进行对比。

【实验结果 / Results】
诊断任务中，图像-only SSL在线性探测时提升准确率，但完全微调时未超越ImageNet预训练；多模态SSL因预训练数据严重偏倚（93% KL 3级）未能改善分级性能。预后任务中，多模态SSL在10%标注数据条件下显著优于ImageNet基线，外部验证集（MOST）AUROC达0.701 vs. 0.599。

【应用价值 / Applications】
该研究为医学影像AI开发提供了重要启示：未筛选的真实医院数据虽因疾病分布偏倚不适用于诊断模型训练，但可有效用于预后预测任务。这一发现有助于降低医学AI开发对昂贵、精心标注数据集的依赖，推动利用大规模未筛选临床数据构建预后预测模型。
