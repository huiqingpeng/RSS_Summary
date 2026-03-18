---
title: "Towards Robust Multimodal Physiological Foundation Models: Handling Arbitrary Missing Modalities"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2504.19596"
published: "2026-03-18"
summarized: "2026-03-18T17:10:11.245861"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了PhysioOmni，首个面向多模态生理信号的基础模型，能够处理EEG、ECG、EOG、EMG等多种信号模态。该模型通过解耦多模态分词器建模同质与异质特征，实现了模态无关和模态特定的掩码信号预训练，解决了现有方法在跨数据集泛化和推理时缺失模态处理方面的不足。实验表明，PhysioOmni在情绪识别、睡眠分期分类、运动预测和心理负荷检测四项下游任务上达到最优性能，同时对任意缺失模态保持强鲁棒性。

【方法概述 / Method】
PhysioOmni采用解耦式多模态分词器架构，将多模态信号解耦为通用表示，同时保留模态特定信息；预训练阶段通过模态不变性目标和模态特定目标进行掩码信号学习。为适应多样化且不完整的模态组合，预训练编码器通过原型对齐进行弹性微调，确保在下游任务中的适应能力。

【实验结果 / Results】
在四项下游任务（情绪识别、睡眠分期分类、运动预测、心理负荷检测）的广泛实验表明，PhysioOmni达到当前最优性能；模型在推理时面对任意模态缺失的情况下仍保持强鲁棒性，显著优于依赖专用架构和数据集特定融合策略的现有方法。

【应用价值 / Applications】
PhysioOmni可广泛应用于医疗健康监测（如睡眠分析、情绪障碍评估）、脑机接口系统（运动意图解码）以及认知负荷实时检测等人机交互场景。其处理任意缺失模态的能力使其特别适用于临床和实际部署中传感器故障或采集条件受限的可靠生理信号分析。
