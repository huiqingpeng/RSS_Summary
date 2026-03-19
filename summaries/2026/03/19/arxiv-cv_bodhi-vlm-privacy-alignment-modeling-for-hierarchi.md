---
title: "Bodhi VLM: Privacy-Alignment Modeling for Hierarchical Visual Representations in Vision Backbones and VLM Encoders via Bottom-Up and Top-Down Feature Search"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.13728"
published: "2026-03-19"
summarized: "2026-03-19T17:03:44.522348"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 **Bodhi VLM**，一种用于**层级神经表示的隐私对齐建模框架**，旨在解决隐私保护学习系统中噪声注入与隐私预算对齐的可解释性问题。该框架通过 NCP 和 MDAV 聚类将敏感概念与层间分组关联，利用**自底向上（BUA）和自顶向下（TDA）策略**定位多尺度表示中的敏感特征区域，并通过**期望最大化隐私评估（EMPA）模块**生成可解释的预算对齐信号。研究在目标检测器（YOLO、PPDPTS、DETR）和视觉语言模型编码器（CLIP、LLaVA、BLIP）上验证了框架的有效性，为隐私对齐的层级表示提供了可学习的建模视角，而非仅事后审计。

---

【方法概述 / Method】

论文提出了一种**双向特征搜索策略**：自底向上（BUA）从低层特征逐步聚合敏感信息，自顶向下（TDA）从高层语义指导敏感区域定位，两者在层级特征结构（如特征金字塔或视觉编码器层）上协同工作。核心组件 EMPA 模块采用**期望最大化机制**，将拟合的敏感特征分布与评估者指定的参考分布（如尺度为 $c/\epsilon$ 的 Laplace 或 Gaussian 分布）进行比较，输出参考相对的预算对齐信号。

---

【实验结果 / Results】

实验表明，**BUA 和 TDA 呈现出可比较的偏差趋势**，验证了双向搜索策略的一致性；EMPA 在报告设置下提供了**稳定的对齐信号**。与通用差异基线（Chi-square、K-L、MMD）和任务相关基线（MomentReg、NoiseMLE、Wass-1）相比，Bodhi VLM 展现出优势。结果以多种子均值±标准差形式报告，置信区间见补充材料。

---

【应用价值 / Applications】

该研究适用于需要**隐私保护的可解释视觉 AI 系统**，如医疗影像分析、人脸识别和自动驾驶中的敏感视觉数据处理，帮助开发者在模型设计和部署阶段主动评估隐私-效用权衡。框架的通用性使其可扩展至多种视觉骨干网络和视觉语言模型，为隐私合规的 AI 产品开发提供实用工具。
