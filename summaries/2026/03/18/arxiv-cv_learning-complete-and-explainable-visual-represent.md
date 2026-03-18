---
title: "Learning complete and explainable visual representations from itemized text supervision"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.11141"
published: "2026-03-18"
summarized: "2026-03-18T18:31:11.604447"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ItemizedCLIP框架，用于从条目化文本监督中学习完整且可解释的视觉表示。该框架通过交叉注意力模块生成文本条目条件化的视觉嵌入，并设计专门的目标函数来确保条目独立性（不同条目对应不同区域）和表示完整性（覆盖所有条目）。在四个具有自然条目化文本监督的领域（脑部MRI、头部CT、胸部CT、遥感）以及一个合成数据集上，ItemizedCLIP在零样本性能和细粒度可解释性方面显著优于基线方法。

【方法概述 / Method】
ItemizedCLIP采用交叉注意力机制，使每个文本条目能够关注图像中的特定区域，从而生成条件化的视觉嵌入。该方法设计了联合优化目标，包括条目独立性损失（确保不同文本条目激活图像的不同区域）和表示完整性损失（确保所有文本条目都被充分覆盖），以实现语义解耦和完整的视觉表示学习。

【实验结果 / Results】
在脑部MRI、头部CT、胸部CT和遥感四个真实数据集以及一个合成数据集上，ItemizedCLIP相比标准CLIP及其他基线方法取得了显著的零样本分类性能提升。该方法生成的视觉表示具有语义可解释性，能够清晰区分不同文本条目对应的图像区域，实现了细粒度的视觉-文本对齐。

【应用价值 / Applications】
该研究对医学影像分析（如放射学报告中的多病灶描述）和遥感图像理解等条目化文本标注场景具有重要价值。ItemizedCLIP的可解释性特征有助于临床决策支持系统，使医生能够验证模型关注区域与报告描述的一致性，提升AI辅助诊断的透明度和可信度。
