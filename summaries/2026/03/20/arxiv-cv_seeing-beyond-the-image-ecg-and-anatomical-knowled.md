---
title: "Seeing Beyond the Image: ECG and Anatomical Knowledge-Guided Myocardial Scar Segmentation from Late Gadolinium-Enhanced Images"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.14702"
published: "2026-03-20"
summarized: "2026-03-20T16:15:12.540617"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种多模态框架，通过整合心电图（ECG）电生理信息和AHA-17解剖图谱先验知识，实现基于晚期钆增强（LGE）心脏MRI的心肌瘢痕分割。针对ECG与LGE-MRI非同步采集的问题，作者设计了时间感知特征融合（TAFF）机制，根据采集时间差动态加权融合特征。该方法在Dice分数上从0.6149提升至0.8463，显著优于仅使用图像的基线方法。

【方法概述 / Method】
本研究采用多模态融合策略，将ECG信号提取的电生理特征与LGE-MRI影像特征相结合，并引入AHA-17标准心脏分段图谱作为解剖约束。核心创新是TAFF机制，该机制能够建模ECG与MRI采集时间差的影响，实现跨模态特征的动态自适应融合，确保生理一致性。

【实验结果 / Results】
在临床数据集上的评估表明，该方法相比nnU-Net图像基线取得显著提升：瘢痕分割Dice分数从0.6149提高到0.8463，精确率达到0.9115，敏感度达到0.9043。这一结果证明了融合生理和解剖知识能够有效克服LGE图像对比度变化和伪影带来的分割挑战。

【应用价值 / Applications】
该研究为心脏组织活力评估和心肌梗死诊断提供了更鲁棒的自动化工具，特别适用于临床中LGE图像质量不佳的情况。通过整合常规采集的ECG数据，该方法可提升瘢痕定位的准确性，为临床决策（如血运重建或消融治疗规划）提供更可靠的依据，推动生理引导的精准心脏影像分析发展。
