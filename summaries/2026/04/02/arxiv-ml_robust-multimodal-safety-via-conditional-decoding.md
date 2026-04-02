---
title: "Robust Multimodal Safety via Conditional Decoding"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00310"
published: "2026-04-02"
summarized: "2026-04-03T07:20:21.403212"
ai_provider: "openai"
---

【论文摘要 / Abstract】
多模态大语言模型（MLLMs）在面临利用跨模态交互的有害查询时，安全对齐性能往往会下降。本文提出了一种简单的条件解码策略CASA（Classification Augmented with Safety Attention），利用MLLMs的内部表示在生成响应前预测二元安全标记，并引入新颖的安全注意力模块增强恶意查询检测能力。CASA在不依赖外部分类器、辅助头或模态特定安全微调的情况下，将跨模态和跨攻击类型的平均攻击成功率降低超过97%，同时保持对良性输入的强实用性。

【方法概述 / Method】
CASA通过提取MLLMs的内部隐藏表示，在解码阶段前预测一个二元安全标记来判断输入查询的安全性；核心创新是安全注意力模块，该模块专门设计用于增强模型检测恶意多模态查询的能力，且完全内置于模型内部无需额外组件。

【实验结果 / Results】
在MM-SafetyBench、JailbreakV-28k和对抗性音频测试等多样化基准上，CASA将平均攻击成功率降低超过97%，覆盖多种模态和攻击类型；同时通过自动化评估和13名训练有素的标注员进行的人工评估验证，CASA在良性输入上保持了强大的实用性。

【应用价值 / Applications】
CASA可广泛应用于部署多模态大语言模型的实际场景，如内容审核、对话系统和视觉-语言助手等，为防范跨模态越狱攻击提供即插即用的安全防护；其无需外部组件和模态特定微调的特性使其具备良好的通用性和部署便捷性。
