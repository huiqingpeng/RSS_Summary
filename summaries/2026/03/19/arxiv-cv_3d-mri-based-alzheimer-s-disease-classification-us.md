---
title: "3D MRI-Based Alzheimer's Disease Classification Using Multi-Modal 3D CNN with Leakage-Aware Subject-Level Evaluation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17304"
published: "2026-03-19"
summarized: "2026-03-19T15:07:51.732663"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究提出了一种多模态3D卷积神经网络用于阿尔茨海默病（AD）分类，利用原始OASIS 1 MRI体积数据，结合T1结构信息与灰质、白质、脑脊液概率图，以捕获互补的神经解剖学信息。该模型在5折受试者级别交叉验证下达到72.34%±4.66%的平均准确率和0.7781±0.0365的ROC AUC。研究还通过对比切片级与受试者级别的评估策略，揭示了数据泄露对性能报告的影响，为体积MRI分析在AD分类中的应用建立了可复现的基准。

【方法概述 / Method】
研究采用多模态3D CNN架构，输入包括原始T1加权MRI体积和通过FSL FAST分割获得的三种组织概率图（灰质、白质、脑脊液），形成四通道输入。模型训练采用严格的受试者级别交叉验证（subject-level cross-validation），确保同一受试者的所有切片不会同时出现在训练集和测试集中，以避免数据泄露。

【实验结果 / Results】
在OASIS 1临床标注队列上，多模态3D方法取得72.34%±4.66%的分类准确率和0.7781±0.0365的ROC AUC。GradCAM可视化显示模型关注于解剖学有意义的区域，包括内侧颞叶和脑室区域——这些区域已知与AD相关的结构变化密切相关。对比实验表明，切片级评估会显著高估性能，而受试者级别评估能提供更真实的泛化能力估计。

【应用价值 / Applications】
该研究为基于MRI的AD计算机辅助诊断提供了可复现的体积分析基准，有助于临床神经影像学从传统的2D切片分析向更全面的3D体积评估转变。研究成果可应用于早期AD筛查、疾病进展监测以及多中心影像研究的标准化分析流程，同时强调了严格评估协议在医学影像AI研究中的重要性。
