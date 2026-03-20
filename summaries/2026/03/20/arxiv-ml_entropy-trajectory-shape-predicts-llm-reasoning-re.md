---
title: "Entropy trajectory shape predicts LLM reasoning reliability: A diagnostic study of uncertainty dynamics in chain-of-thought"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18940"
published: "2026-03-20"
summarized: "2026-03-20T13:18:06.543319"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究发现，大语言模型在链式思维（CoT）推理过程中的不确定性动态轨迹形状可以预测推理可靠性。研究者提出"熵轨迹单调性"指标——若推理链每步的答案分布熵持续递减则为单调链，实验表明单调链的准确率显著高于非单调链（GSM8K上+21.9个百分点，Mistral-7B上+34.7个百分点）。关键的是，总熵降幅而非单调性本身并不具有预测性，揭示了"形状优于幅度"的分离现象。

【方法概述 / Method】
研究者通过每步采样少量答案补全来捕捉推理步骤间的不确定性动态，计算每步答案分布的熵值形成熵轨迹，并定义"熵轨迹单调性"作为诊断指标。该方法仅需约1,500个token/问题，成本仅为40链自洽性方法的1/8。

【实验结果 / Results】
在GSM8K数据集（n=300）上，Qwen2.5-7B-Instruct的单调链准确率达68.8%，非单调链仅46.8%；违反单调性的次数为0/1/2时，准确率分别为68.8%/50.8%/28.6%。传统token对数概率置信度随推理深度校准性恶化（ECE从0.186升至0.312）。结果在Mistral-7B上成功复现，单调链优势更显著（+34.7个百分点）。

【应用价值 / Applications】
该研究为低成本检测LLM推理失败提供了新工具，可应用于实时推理质量监控、自适应计算资源分配（如对非单调链触发额外验证），以及提升复杂多步推理系统的可靠性和效率，特别适合资源受限场景下的推理可靠性评估。
