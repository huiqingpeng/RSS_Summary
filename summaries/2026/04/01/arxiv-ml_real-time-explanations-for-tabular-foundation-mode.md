---
title: "Real-Time Explanations for Tabular Foundation Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29946"
published: "2026-04-01"
summarized: "2026-04-02T07:21:18.214720"
ai_provider: "openai"
---

【论文摘要 / Abstract】
可解释性对科学机器学习至关重要，但现有解释方法（如SHAP）计算成本高昂，限制了交互式探索。本文提出ShapPFN，一种将Shapley值回归直接集成到架构中的表格基础模型，可在单次前向传播中同时生成预测和解释。在标准基准测试中，ShapPFN实现了具有竞争力的性能，同时以超过1000倍的速度（0.06秒 vs 610秒）生成高保真解释（R²=0.96，余弦相似度=0.99）。

【方法概述 / Method】
ShapPFN将Shapley值计算嵌入模型架构本身，通过基础模型的设计实现预测与解释的一体化生成。该方法避免了传统事后解释方法所需的大量模型重训练或采样计算，使解释生成成为模型推理的自然副产品。

【实验结果 / Results】
ShapPFN在预测性能上与现有方法相当，同时解释质量达到R²=0.96和余弦相似度0.99的高保真度。计算效率方面，相比KernelSHAP的610秒，ShapPFN仅需0.06秒即可完成解释生成，实现了超过1000倍的加速。

【应用价值 / Applications】
该研究适用于需要实时交互式模型解释的科学发现场景，如生物医学假设生成、金融风控决策支持等表格数据密集型领域。其高效性使研究人员能够在探索性数据分析中即时获得模型解释，加速假设验证和知识发现流程。
