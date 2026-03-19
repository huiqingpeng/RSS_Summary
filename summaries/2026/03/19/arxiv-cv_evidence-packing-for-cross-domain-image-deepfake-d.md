---
title: "Evidence Packing for Cross-Domain Image Deepfake Detection with LVLMs"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17761"
published: "2026-03-19"
summarized: "2026-03-19T15:17:34.366785"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为Semantic Consistent Evidence Pack (SCEP)的训练无关框架，用于将大型视觉语言模型(LVLMs)应用于图像深度伪造检测(IDD)。SCEP通过挖掘可疑图像块令牌替代全图推理，结合语义一致性和频率/噪声异常检测，生成紧凑的证据包来引导冻结的LVLM进行推理。实验表明，该方法无需微调即可在多个跨域基准上超越强基线模型，有效解决了传统方法泛化性差和微调成本高的问题。

【方法概述 / Method】
SCEP首先利用视觉编码器的CLS令牌作为全局参考，对图像块特征进行聚类分组；然后设计融合指标（CLS引导的语义不匹配+频率域异常+噪声异常）为各图像块打分。为避免冗余并覆盖分散的篡改痕迹，该方法从每个聚类中采样高置信度图像块，并应用基于网格的非极大值抑制(NMS)，最终形成证据包输入冻结的LVLM完成检测。

【实验结果 / Results】
在多个跨域基准测试上的实验表明，SCEP在不进行LVLM微调的情况下显著优于现有强基线方法；该训练无关框架展现出对多样化、不断演变的伪造手段的良好泛化能力，验证了证据驱动推理策略在深度伪造检测中的有效性。

【应用价值 / Applications】
SCEP可广泛应用于社交媒体内容审核、新闻真实性验证、数字取证等场景，帮助平台快速识别AI生成的虚假图像；其无需微调的特性大幅降低了部署成本，使大型视觉语言模型能够灵活适应新兴的伪造技术，为构建可信的数字内容生态提供实用工具。
