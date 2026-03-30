---
title: "Preventing Data Leakage in EEG-Based Survival Prediction: A Two-Stage Embedding and Transformer Framework"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25923"
published: "2026-03-30"
summarized: "2026-03-31T07:19:54.302706"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究识别了多阶段脑电图（EEG）建模流程中一种此前被忽视的数据泄露问题——当长时程EEG记录被分割为短窗口并在多个训练阶段重复使用时，模型可能隐式编码并传播标签信息。为此，作者提出了一种防泄露的两阶段框架，实验表明该框架能在严格的临床约束下实现稳定且可泛化的性能，尤其在高特异性阈值下保持高敏感性。

【方法概述 / Method】
该框架采用两阶段架构：第一阶段使用带ArcFace目标的卷积神经网络将短时EEG片段转换为嵌入表示；第二阶段采用基于Transformer的模型聚合这些嵌入以生成患者级预测，并通过严格的训练队列隔离消除泄露路径。

【实验结果 / Results】
在大型心脏骤停后患者EEG数据集上的实验表明，所提框架在 clinically relevant constraints 下实现了稳定且可泛化的性能，特别是在严格特异性阈值下仍能保持高敏感性；同时证明违反患者级严格分离会显著虚高验证指标并导致独立测试数据性能大幅下降。

【应用价值 / Applications】
该研究为昏迷患者心脏骤停后的可靠EEG结局预测提供了实用解决方案，强调了严格数据划分在医疗AI中的关键重要性，有助于推动深度学习模型从研究向临床实践的可靠转化。
