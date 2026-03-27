---
title: "No Single Metric Tells the Whole Story: A Multi-Dimensional Evaluation Framework for Uncertainty Attributions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24524"
published: "2026-03-27"
summarized: "2026-03-28T07:11:28.997242"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对不确定性归因（uncertainty attributions）评估缺乏统一标准的问题，将不确定性归因与成熟的Co-12可解释AI评估框架对齐，提出了正确性、一致性、连续性和紧凑性四个属性的具体实现，并创新性地引入"传递性"（conveyance）属性以评估认知不确定性的可控增长能否可靠传播到特征级归因。实验表明，基于梯度的方法在一致性和传递性上持续优于基于扰动的方法，而Monte-Carlo dropconnect在多数指标上优于Monte-Carlo dropout；同时发现不同方法间的一致性较低，说明单一指标不足以全面评估不确定性归因质量。

【方法概述 / Method】

作者将Co-12框架中的五个属性（正确性、一致性、连续性、紧凑性、传递性）转化为可计算的评估指标，设计了八种具体度量方法，涵盖输入扰动、模型参数扰动和归因稳定性等维度。该框架支持组合不同的不确定性量化方法（如MC dropout、MC dropconnect）与特征归因方法（如梯度、扰动）进行系统性评估。

【实验结果 / Results】

在表格数据和图像数据上的实验显示：梯度类方法（如Gradient、Integrated Gradients）在一致性和传递性指标上显著优于扰动类方法（如LIME、SHAP）；MC dropconnect在大多数指标上优于MC dropout；虽然多数指标对方法的排名在不同样本间保持一致，但方法间的整体一致性较低，验证了多维度评估的必要性。

【应用价值 / Applications】

该评估框架为不确定性归因方法的系统比较和开发奠定了基础，可应用于高风险决策场景（如医疗诊断、自动驾驶）中模型不确定性的可信解释，帮助从业者选择合适的不确定性归因方法，并指导新方法的研发方向，提升AI系统在关键领域的可靠性和可解释性。
