---
title: "Differential Attention-Augmented BiomedCLIP with Asymmetric Focal Optimization for Imbalanced Multi-Label Video Capsule Endoscopy Classification"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17879"
published: "2026-03-19"
summarized: "2026-03-19T16:17:59.742927"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种针对视频胶囊内镜（VCE）的多标签分类框架，专门解决Galar数据集中极端类别不平衡问题（病理发现占比不足0.1%）。该方法通过将BiomedCLIP的标准多头自注意力替换为差分注意力机制来抑制注意力噪声，并结合平方根频率加权采样器、非对称焦点损失、Mixup正则化和逐类阈值优化等多种策略。在包含161,025帧的RARE-VISION测试集上，该方法实现了mAP@0.5为0.2456、mAP@0.95为0.2353的时序检测性能，单GPU推理仅需约8.6分钟。

【方法概述 / Method】
该研究以生物医学视觉-语言基础模型BiomedCLIP为骨干网络，将其标准多头自注意力替换为差分注意力机制——通过计算两个softmax注意力图的差值来抑制噪声。在优化层面，采用平方根频率加权采样器、非对称焦点损失、Mixup正则化和逐类阈值优化来应对严重的类别不平衡问题，并通过中值滤波平滑和间隙合并来增强时序一致性。

【实验结果 / Results】
在包含三次NaviCam检查、共161,025帧的RARE-VISION测试集上，完整流水线实现了时序mAP@0.5为0.2456、mAP@0.95为0.2353的性能指标。整个推理过程在单GPU上仅需约8.6分钟即可完成，证明了该方法在实际临床部署中的高效性。

【应用价值 / Applications】
该研究可直接应用于视频胶囊内镜的自动化病理检测，辅助胃肠科医生快速筛查小肠疾病，显著提高诊断效率并减少漏诊风险。其高效的单GPU推理能力（8.6分钟处理16万帧）使其具备临床实时或近实时部署潜力，同时多标签分类框架可支持多种病理类型的同步识别，适用于大规模人群筛查场景。
