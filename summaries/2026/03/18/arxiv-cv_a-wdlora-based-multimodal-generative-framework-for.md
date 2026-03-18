---
title: "A WDLoRA-Based Multimodal Generative Framework for Clinically Guided Corneal Confocal Microscopy Image Synthesis in Diabetic Neuropathy"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.13693"
published: "2026-03-18"
summarized: "2026-03-18T18:32:31.104700"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究针对糖尿病周围神经病变（DPN）诊断中角膜共聚焦显微镜（CCM）图像标注数据稀缺的问题，提出了一种基于权重分解低秩自适应（WDLoRA）的多模态生成框架。该框架通过解耦幅度和方向权重更新，使基础生成模型能够独立学习神经拓扑结构和基质对比度，从而生成解剖学上一致的CCM图像。实验表明，该框架在视觉保真度（FID: 5.18）和结构完整性（SSIM: 0.630）方面达到最优，且合成图像保留临床金标准生物标志物，用于训练下游诊断模型可提升准确率2.1%、分割性能2.2%。

【方法概述 / Method】
论文采用WDLoRA参数高效微调机制，将预训练权重分解为幅度和方向两个独立组件，分别对应CCM图像中的强度（基质对比度）和方向（神经拓扑）特征学习。模型联合以神经分割掩码和疾病特异性临床提示为条件，实现跨DPN病程谱系（对照组、T1无DPN、T1有DPN）的解剖学相干图像合成。

【实验结果 / Results】
该框架在CCM图像合成任务上显著优于GAN和标准扩散基线模型，Fréchet Inception Distance达到5.18，Structural Similarity Index Measure达到0.630。合成图像与真实患者数据在统计上等效，成功保留了角膜神经纤维长度、密度等金标准临床生物标志物，验证了医学真实性和临床可用性。

【应用价值 / Applications】
该研究为医学AI领域的数据瓶颈问题提供了有效解决方案，可扩展应用于其他医学影像模态的稀有疾病数据增强。合成CCM图像可用于训练自动化DPN诊断和神经分割模型，提升早期糖尿病神经病变的筛查效率，具有潜在的临床转化价值和公共卫生意义。
