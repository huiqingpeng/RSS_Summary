---
title: "ResNet-50 with Class Reweighting and Anatomy-Guided Temporal Decoding for Gastrointestinal Video Analysis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17784"
published: "2026-03-19"
summarized: "2026-03-19T13:15:33.105689"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种基于ResNet-50的多标签胃肠道视频分析管道，结合类别重加权与解剖学引导的时间解码技术。该系统能够从336×336分辨率的视频帧中预测17类标签（5类解剖结构+12类病理）。针对罕见病理标签的 severe class imbalance 问题，作者采用裁剪的类别级正样本加权策略；在时间解码阶段，通过融合GT风格的帧级事件组合、解剖学投票平滑及基于解剖学的病理门控机制，显著提升了时序事件检测性能。

【方法概述 / Method】
核心架构采用ResNet-50作为帧级分类器，输入图像尺寸为336×336。训练阶段引入clipped class-wise positive weighting处理类别不平衡问题，对罕见病理类别进行损失加权的同时限制权重上限以保证优化稳定性。推理阶段设计了解剖学引导的时间解码器，整合GT风格的帧级事件合成、解剖学投票平滑以及基于解剖位置约束的病理预测门控策略。

【实验结果 / Results】
在挑战测试集上，最终提交方案将时序mAP从0.3801提升至0.4303，相对提升约13.2%。关键消融表明，直接帧到事件的转换会产生碎片化错配，而所提出的保守滞后解码器（conservative hysteresis decoder）有效改善了时序事件与官方真值的一致性。

【应用价值 / Applications】
该研究可直接应用于计算机辅助胃肠道内镜诊断系统，实现实时解剖定位与病理检测。多标签框架支持临床工作流中的全面病灶记录，而轻量化的ResNet-50骨干网络便于部署至嵌入式医疗设备。解剖学约束机制增强了模型的临床可解释性与预测可靠性。
