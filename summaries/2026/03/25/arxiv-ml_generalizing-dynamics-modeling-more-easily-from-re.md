---
title: "Generalizing Dynamics Modeling More Easily from Representation Perspective"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22655"
published: "2026-03-25"
summarized: "2026-03-26T07:16:05.379045"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了PDEDER（Pre-trained Dynamics EncoDER），一种通用的预训练动态编码器，通过将原始状态观测嵌入到潜在空间来解决神经动力学模型在不同复杂系统间泛化能力差的问题。该方法通过最小化Lyapunov指数目标来预训练语言模型，约束潜在空间中动力学学习的混沌行为，同时结合重建和预测目标避免过度平滑。在12个动态系统的短/长期预测实验中，PDEDER在域内和跨域设置下均展现出有效性和泛化能力。

【方法概述 / Method】
PDEDER利用预训练语言模型（PLM）作为基础架构，通过Lyapunov指数目标函数进行预训练，该目标惩罚嵌入观测的发散性以促进局部稳定的潜在动力学结构。训练过程中同时优化重建损失和预测损失，使用来自23个复杂系统的152组真实与合成观测数据构建预训练语料库。

【实验结果 / Results】
PDEDER在12个动态系统上进行了短/长期预测评估，涵盖域内（in-domain）和跨域（cross-domain）两种设置。实验结果表明该方法在动力学建模的有效性和跨系统泛化能力方面均有显著提升，能够适配多种特定的下游动力学建模方法进行微调。

【应用价值 / Applications】
该研究可广泛应用于气候预测、生态建模、流体系统仿真等需要学习复杂系统动力学的领域。PDEDER的预训练-微调范式降低了为新系统开发动力学模型的成本，为科学计算和工程应用中的通用动态建模提供了可扩展的解决方案。
