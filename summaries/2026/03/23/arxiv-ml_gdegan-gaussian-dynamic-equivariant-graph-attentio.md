---
title: "GDEGAN: Gaussian Dynamic Equivariant Graph Attention Network for Ligand Binding Site Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19817"
published: "2026-03-23"
summarized: "2026-03-24T07:22:41.994629"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了GDEGAN（高斯动态等变图注意力网络），用于蛋白质配体结合位点预测。该方法通过用自适应高斯核替代传统的点积注意力机制，捕捉相邻残基在化学和几何性质上的变化。实验表明，GDEGAN在COACH420、HOLO4k和PDBBind2020数据集上相比现有方法取得了37-66%的DCC和7-19%的DCA成功率相对提升，为基于结构的计算药物发现提供了更准确的结合位点识别工具。

【方法概述 / Method】
GDEGAN采用等变图神经网络架构，核心创新在于提出了一种基于高斯核的动态注意力机制。该机制利用局部特征分布的统计信息（特别是局部方差）作为自适应带宽参数，并结合可学习的逐头温度参数，使每个蛋白质区域能够动态确定其上下文相关的重要性权重，从而更好地识别结合位点。

【实验结果 / Results】
GDEGAN在三个基准数据集（COACH420、HOLO4k和PDBBind2020）上均显著优于现有最先进方法。具体而言，该方法在DCC（质心距离）指标上实现了37-66%的相对改进，在DCA（原子距离）成功率上实现了7-19%的提升，证明了其在结合位点预测任务上的优越性。

【应用价值 / Applications】
该研究可直接应用于加速蛋白质-配体对接过程，通过准确识别潜在结合位点来辅助治疗靶点识别。这一进展对于结构导向的药物设计和计算药物发现具有重要的实际意义，能够提高虚拟筛选和先导化合物优化的效率。
