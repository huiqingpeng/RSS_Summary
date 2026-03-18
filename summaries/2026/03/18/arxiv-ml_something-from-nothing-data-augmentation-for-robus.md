---
title: "Something from Nothing: Data Augmentation for Robust Severity Level Estimation of Dysarthric Speech"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15988"
published: "2026-03-18"
summarized: "2026-03-18T16:09:10.567564"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对构音障碍语音质量评估（DSQA）中标注数据稀缺的问题，提出了一种三阶段训练框架，利用无标注构音障碍语音和大规模典型语音数据集进行扩展训练。该方法通过教师模型生成伪标签，并采用标签感知对比学习策略进行弱监督预训练，最终在五个跨病因和跨语言的未见数据集上取得了平均SRCC 0.761的优异性能，显著优于现有最先进方法。

【方法概述 / Method】
论文提出三阶段框架：首先使用教师模型为无标注构音障碍样本生成伪标签；然后采用标签感知对比学习（label-aware contrastive learning）进行弱监督预训练，使模型接触多样化的说话人和声学条件；最后对预训练模型进行下游DSQA任务的微调。该框架基于Whisper架构构建。

【实验结果 / Results】
实验在五个未见数据集上进行验证，涵盖多种病因和语言。Whisper基线模型已显著优于现有SOTA方法（如SpICE）；完整三阶段框架进一步将性能提升至平均Spearman秩相关系数（SRCC）0.761，展现出强大的跨数据集泛化能力和鲁棒性。

【应用价值 / Applications】
该研究为临床构音障碍诊断提供了可扩展的自动化评估工具，降低了对昂贵主观评价的依赖；同时支持包容性语音技术的发展，有助于改善言语障碍患者的辅助沟通设备体验，并可在多语言、多病因的临床场景中广泛部署。
