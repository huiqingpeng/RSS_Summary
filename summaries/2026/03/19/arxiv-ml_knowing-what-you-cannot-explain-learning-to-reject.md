---
title: "Knowing What You Cannot Explain: Learning to Reject Low-Quality Explanations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2507.12900"
published: "2026-03-19"
summarized: "2026-03-19T14:04:49.642949"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了"学习拒绝低质量解释"（Learning to Reject low-quality eXplanations, LtX）的新框架，扩展了传统的Learning to Reject（LtR）范式。作者指出当前LtR策略仅关注预测性能而忽视解释质量，而低质量解释会严重损害用户信任并导致对错误预测的过度依赖。为此，他们开发了REX（REjector of low-quality eXplanations）方法，通过结合机器自动判断和人类显式标注来学习解释质量评估，并公开发布了包含1050个人工标注机器解释的大规模数据集。

【方法概述 / Method】
REX方法为预测器配备了一个拒绝器（rejector），专门评估基于归因技术的解释质量。该拒绝器通过解释质量标签进行训练，这些标签融合了机器端的客观度量（如解释与模型实际推理的一致性）和人类的显式标注，从而实现对低质量解释的有效识别和拒绝。

【实验结果 / Results】
实验结果表明，REX在多个评估指标上均优于传统的LtR策略以及仅依赖单一解释度量指标的基线方法。该方法能够更准确地识别出那些预测正确但解释质量差的样本，有效避免了因解释不可靠而导致的用户过度信任问题。

【应用价值 / Applications】
该研究在高风险决策场景（如医疗诊断、金融风控、司法辅助等）具有重要应用价值，可确保AI系统在无法提供可靠解释时主动拒绝预测，从而提升系统透明度和用户信任。此外，发布的大规模人工标注数据集为后续可解释AI和解释质量评估研究提供了重要资源。
