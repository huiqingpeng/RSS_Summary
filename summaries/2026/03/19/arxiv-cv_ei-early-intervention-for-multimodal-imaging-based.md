---
title: "EI: Early Intervention for Multimodal Imaging based Disease Recognition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17514"
published: "2026-03-19"
summarized: "2026-03-19T15:12:21.551571"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Early Intervention (EI)框架，用于解决多模态医学影像疾病识别中的两大挑战：传统"单模态嵌入后融合"范式无法充分利用多模态数据的互补信息，以及医学影像与自然图像的领域差异阻碍视觉基础模型(VFMs)的直接应用。EI框架通过将参考模态的高层语义token作为干预token，在目标模态嵌入的早期阶段进行引导。同时，作者提出了Mixture of Low-varied-Ranks Adaptation (MoR)参数高效微调方法，通过多秩低秩适配器和权重松弛路由器实现VFM的医学领域适应。在三个公开数据集上的实验验证了该方法的有效性。

【方法概述 / Method】
EI框架采用"早期干预"策略，将一种模态设为目标模态，其余模态作为参考模态，提取参考模态的高层语义token作为干预token，在目标模态的嵌入早期阶段注入这些语义信息以引导特征学习。MoR方法则采用一组不同秩的低秩适配器(low-rank adapters)配合权重松弛路由器(weight-relaxed router)，实现视觉基础模型的高效参数微调，减少计算开销的同时提升领域适应能力。

【实验结果 / Results】
本文在三个公开多模态医学影像数据集上进行了广泛实验，包括视网膜疾病分类、皮肤病变分类和膝关节异常分类任务。实验结果表明，EI框架配合MoR微调方法在多个竞争基线方法上取得了显著性能提升，验证了早期干预策略和参数高效微调在多模态医学影像分析中的有效性。

【应用价值 / Applications】
该研究可广泛应用于多模态医学影像辅助诊断系统，如结合眼底彩照与OCT图像的视网膜疾病筛查、皮肤镜与临床照片融合的皮肤癌诊断，以及X光与MRI联合的骨科疾病识别等场景。EI框架通过早期融合互补模态信息提升诊断准确性，MoR方法降低大模型微调成本，使先进的视觉基础模型能够高效部署于医疗资源受限的临床环境。
