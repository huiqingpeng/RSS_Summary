---
title: "FoMo X: Modular Explainability Signals for Outlier Detection Foundation Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17570"
published: "2026-03-19"
summarized: "2026-03-19T12:13:52.189680"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 FoMo-X，一个模块化框架，为表格异常检测（OD）基础模型（特别是 Prior-Data Fitted Networks, PFNs）提供内在、轻量的可解释性诊断能力。该框架通过在预训练 PFN 的冻结嵌入层上附加辅助诊断头（Severity Head 和 Uncertainty Head），将计算昂贵的属性（如基于蒙特卡洛 dropout 的认知不确定性）蒸馏为确定性单步推理，实现了零样本异常检测中的风险分层和校准置信度估计。在 ADBench 等基准上的评估表明，FoMo-X 能够以高保真度恢复真实诊断信号，且推理开销可忽略不计。

【方法概述 / Method】

FoMo-X 的核心方法是利用预训练 PFN  backbone 的冻结嵌入层中已编码的丰富上下文关系信息，离线训练辅助诊断头来提取可解释信号。具体而言，Severity Head 将异常分数离散化为可解释的风险等级，Uncertainty Head 提供经过校准的置信度度量，两者均通过与 backbone 相同的生成式模拟器先验进行训练，从而实现计算昂贵属性的高效蒸馏。

【实验结果 / Results】

在合成数据集和 ADBench 真实世界基准上的广泛评估显示，FoMo-X 能够以高保真度恢复真实诊断信号，同时保持可忽略的推理开销。该方法成功将基于蒙特卡洛 dropout 的认知不确定性等复杂属性转化为确定性单步推理，在零样本异常检测场景下实现了可靠的严重程度分层和不确定性量化。

【应用价值 / Applications】

FoMo-X 为安全关键决策场景中的零样本异常检测提供了可信赖的解决方案，适用于需要实时部署且对模型透明度要求高的工业监测、金融风控和医疗诊断等领域。该框架通过弥合基础模型性能与操作可解释性之间的差距，为构建可扩展、可信赖的异常检测系统开辟了新路径。
