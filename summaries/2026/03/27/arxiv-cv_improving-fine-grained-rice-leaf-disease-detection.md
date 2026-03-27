---
title: "Improving Fine-Grained Rice Leaf Disease Detection via Angular-Compactness Dual Loss Learning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.25006"
published: "2026-03-27"
summarized: "2026-03-28T07:20:27.117587"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对水稻叶片病害早期检测中的细粒度分类难题，提出了一种结合Center Loss和ArcFace Loss的双损失学习框架。该方法有效解决了植物病理数据集中常见的高类内方差和低类间差异问题，在三种主流骨干网络（InceptionNetV3、DenseNet201、EfficientNetB0）上均取得了99%以上的分类准确率。研究表明，角度边界约束和中心约束能够显著增强特征嵌入的判别能力，且无需大幅修改网络架构，具有良好的实际部署潜力。

【方法概述 / Method】
本研究采用双损失联合优化策略，将Center Loss（用于最小化类内特征分散）与ArcFace Loss（用于最大化类间角度边界）相结合，替代传统的交叉熵损失函数。该方法直接应用于三种预训练的深度卷积神经网络骨干架构，通过端到端训练学习更具判别性的特征表示。

【实验结果 / Results】
在公开水稻叶片数据集上的实验表明，所提方法显著优于基线模型：InceptionNetV3达到99.6%的准确率，DenseNet201和EfficientNetB0均达到99.2%的准确率。消融实验验证了双损失协同作用的有效性，证明角度约束和紧凑性约束的结合能够产生更具区分度的特征嵌入空间。

【应用价值 / Applications】
该研究成果可直接部署于智能农业系统，为农民和农业技术人员提供实时、准确的水稻病害诊断工具，助力早期干预以减少大规模作物损失。由于方法无需复杂的架构修改，计算开销低，特别适合在边缘设备或资源受限的田间环境中推广应用，对保障粮食安全具有重要的经济和社会价值。
