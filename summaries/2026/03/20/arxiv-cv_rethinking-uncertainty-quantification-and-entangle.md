---
title: "Rethinking Uncertainty Quantification and Entanglement in Image Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18792"
published: "2026-03-20"
summarized: "2026-03-20T15:16:27.660580"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文系统研究了图像分割中的不确定性量化（UQ）问题，特别关注偶然不确定性（AU）与认知不确定性（EU）的分解及其纠缠现象。作者通过大规模实证研究评估了多种AU-EU模型组合，提出了一种量化不确定性纠缠程度的新指标，并发现不同下游任务中最优模型存在差异：集成方法在分布外检测中表现最佳且纠缠最低，而softmax/SSN方法在模糊性建模和校准任务中更具优势。研究还分析了不确定性纠缠的潜在来源，并提出了缓解策略。

【方法概述 / Method】
论文采用全面的实证研究框架，系统组合了多种AU建模方法（如Probabilistic UNet、Diffusion模型）与EU建模方法（如集成学习、MC Dropout），构建了丰富的AU-EU模型组合矩阵。核心创新在于提出了一种新的评估指标，用于量化AU与EU之间的纠缠程度，并在多个下游UQ任务中进行交叉验证。

【实验结果 / Results】
实验表明，集成方法（ensembles）在分布外检测任务中始终保持较低的纠缠度和最优性能；对于模糊性建模和校准任务，最优模型因数据集而异，其中基于softmax/SSN的方法表现良好，而Probabilistic UNets的纠缠程度相对较低。值得注意的是，softmax集成在所有任务中均展现出卓越的综合性能，成为最稳健的选择。

【应用价值 / Applications】
该研究对医疗图像分割等安全关键领域具有重要实践意义，为从业者提供了模型选择的实证依据：需要根据具体应用场景（分布外检测、模糊性建模或校准）权衡AU-EU方法组合。研究提出的纠缠量化指标和缓解方向有助于开发更可靠、更可解释的不确定性量化系统，提升深度学习模型在高风险决策中的可信度。
