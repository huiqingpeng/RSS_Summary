---
title: "A Novel Framework using Intuitionistic Fuzzy Logic with U-Net and U-Net++ Architecture: A case Study of MRI Bain Image Segmentation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18042"
published: "2026-03-20"
summarized: "2026-03-20T13:08:03.654368"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究针对MRI脑图像分割中的不确定性问题，提出了一种将直觉模糊逻辑（Intuitionistic Fuzzy Logic, IFL）与U-Net和U-Net++架构相结合的新框架IFS U-Net和IFS U-Net++。该框架通过直觉模糊表示处理输入数据，有效应对由部分容积效应引起的组织模糊性和边界不确定性。在IBSR和OASIS两个公开MRI脑数据集上的实验表明，所提出的架构在准确率、Dice系数和IoU等评估指标上均实现了性能提升。

【方法概述 / Method】
论文将直觉模糊逻辑集成到经典的U-Net和U-Net++深度学习架构中，构建IFS U-Net和IFS U-Net++模型。核心创新在于使网络能够直接接受直觉模糊表示形式的输入数据，从而在特征提取和分割过程中显式建模图像中的不确定性和模糊性，而非依赖传统确定性表示。

【实验结果 / Results】
实验在两个公开MRI脑数据集（IBSR和OASIS）上进行，采用准确率（Accuracy）、Dice系数和交并比（IoU）作为定量评估指标。结果表明，所提出的IFS U-Net和IFS U-Net++架构通过有效处理不确定性，在所有评估指标上均一致性地提升了分割性能，优于标准U-Net和U-Net++基线模型。

【应用价值 / Applications】
该研究在神经疾病诊断和脑图像分析领域具有重要应用价值，可提高MRI脑组织分割的准确性，辅助医生进行更精准的病灶检测和定量分析。此外，该框架可推广至其他存在固有不确定性的医学影像分割任务，如肿瘤边界模糊、低对比度区域分割等场景。
