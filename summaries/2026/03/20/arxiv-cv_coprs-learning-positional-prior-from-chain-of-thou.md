---
title: "CoPRS: Learning Positional Prior from Chain-of-Thought for Reasoning Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.11173"
published: "2026-03-20"
summarized: "2026-03-20T16:14:44.449604"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出 CoPRS，一种基于多模态思维链（MCoT）的位置感知模型，用于解决推理分割任务中可解释性和语义细节不足的问题。该模型通过可微分的heatmap形式学习位置先验，将语言推理与分割任务桥接起来，使推理过程更加清晰可解释。在RefCOCO系列和ReasonSeg数据集上，CoPRS在验证集和测试集上均达到或超过现有最优性能，并证明了思维链轨迹、生成的heatmap与解码mask之间存在强正相关性。

【方法概述 / Method】

CoPRS采用多模态思维链（MCoT）生成可解释的位置先验，以heatmap形式显式表达推理过程中的空间注意力分布。模型引入可学习的concentration token，聚合图像特征与推理文本特征来生成该位置先验，再通过轻量级解码器将其转换为精确的分割mask，实现了推理过程与分割结果之间的直接可微连接。

【实验结果 / Results】

在RefCOCO系列数据集和ReasonSeg基准测试中，CoPRS在各类标准划分下均达到或超越了现有最优方法的性能指标。实验表明，生成的heatmap与最终mask具有高度一致性，验证了思维链推理与空间定位之间的有效对齐，同时模型展现出更强的目标区域集中能力和更精确的边界预测效果。

【应用价值 / Applications】

CoPRS可应用于需要复杂语言推理引导的图像分割场景，如自动驾驶中的自然语言指令理解、医疗影像的文本描述定位、以及机器人视觉中的交互式目标指定等任务。该方法通过提供可解释的推理-分割对齐机制，有助于提升系统在关键应用中的可靠性和故障诊断能力。
