---
title: "VirPro: Visual-referred Probabilistic Prompt Learning for Weakly-Supervised Monocular 3D Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17470"
published: "2026-03-19"
summarized: "2026-03-19T15:11:30.682191"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了视觉参考概率提示学习（VirPro），一种自适应多模态预训练范式，用于弱监督单目3D目标检测。该方法通过生成可学习的场景条件化提示并结合多高斯提示建模，将视觉特征融入文本嵌入以表达视觉不确定性，从而解决手工设计文本描述难以捕捉场景视觉多样性的问题。在KITTI基准上的实验表明，该方法可显著提升基线性能，平均精度提升高达4.8%。

【方法概述 / Method】
VirPro包含三个核心组件：自适应提示库（APB）存储跨场景生成的多样化可学习实例条件提示；多高斯提示建模（MGPM）将场景视觉特征融入对应文本嵌入，使文本提示能够表达视觉不确定性；最后从融合的视觉-语言嵌入中解码提示目标高斯分布，推导统一的对象级提示嵌入，并通过RoI级对比匹配强制模态对齐。

【实验结果 / Results】
在KITTI基准上的大量实验表明，VirPro预训练范式能够持续带来显著性能提升，相比基线方法平均精度（AP）最高提升4.8%，验证了该方法在弱监督单目3D检测中的有效性。

【应用价值 / Applications】
VirPro可无缝集成到多种弱监督单目3D检测框架中，适用于自动驾驶、机器人感知等需要3D场景理解但标注成本高昂的实际应用场景，通过利用视觉-语言预训练减少对大量真实世界标注的依赖，降低3D检测系统的部署成本。
