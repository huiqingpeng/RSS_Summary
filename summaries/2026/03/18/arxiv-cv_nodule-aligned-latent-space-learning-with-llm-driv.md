---
title: "Nodule-Aligned Latent Space Learning with LLM-Driven Multimodal Diffusion for Lung Nodule Progression Prediction"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15932"
published: "2026-03-18"
summarized: "2026-03-18T18:03:25.680172"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Nodule-Aligned Multimodal (Latent) Diffusion (NAMD)框架，用于预测肺结节进展并生成1年随访CT图像。该方法创新性地引入结节对齐的潜在空间，使潜在向量距离直接对应结节属性变化，并利用大语言模型驱动的控制机制融合患者电子健康档案信息。在NLST数据集上，NAMD生成的随访图像在肺结节恶性预测任务中达到AUROC 0.805和AUPRC 0.346，显著优于基线扫描和现有合成方法，接近真实随访扫描的性能（AUROC: 0.819, AUPRC: 0.393）。

【方法概述 / Method】
NAMD采用多模态扩散模型架构，以基线CT扫描和患者EHR数据为条件生成随访图像。核心创新包括：构建结节对齐的潜在空间实现属性可解释的潜在表示，以及设计LLM驱动的控制机制将非结构化的患者临床数据有效嵌入扩散过程。

【实验结果 / Results】
在NLST大规模肺癌筛查数据集上，NAMD合成的随访图像在恶性预测任务中取得AUROC 0.805和AUPRC 0.346，较基线扫描和传统合成方法有显著提升；与真实随访扫描的性能差距仅约1.7%（AUROC）和12%（AUPRC），证明其捕获了临床相关的结节进展特征。

【应用价值 / Applications】
该研究可应用于肺癌早期筛查的临床决策支持，通过预测结节未来形态辅助医生评估恶性风险，减少不必要的活检或手术；同时支持个性化随访策略制定，优化医疗资源分配，并可用于医学教育中的疾病进展可视化演示。
