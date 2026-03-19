---
title: "Feature Space Renormalization for Semi-supervised Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2311.04055"
published: "2026-03-19"
summarized: "2026-03-19T13:17:39.604675"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种特征空间重归一化（FSR）机制用于半监督学习，该机制通过对特征表示而非标签施加一致性约束，使模型学习更具判别性的特征。为此设计了双分支FSR模块，可无缝嵌入现有SSL框架中。实验表明，FSR模块能帮助基础SSL框架（如CRMatch和FreeMatch）在多个标准基准数据集上提升性能，且不增加计算时间和GPU内存开销。

【方法概述 / Method】
FSR机制的核心是将一致性正则化从预测标签空间转移到特征表示空间。具体实现采用双分支FSR模块，包含双分支头部（dual-branch header）和FSR块（FSR block），通过重归一化操作对特征进行约束，增强特征的判别性和稳定性。

【实验结果 / Results】
FSR模块在多个标准半监督学习基准数据集上验证了有效性，能够一致性地提升CRMatch和FreeMatch等基础框架的性能。关键优势在于性能提升的同时，没有引入额外的计算时间开销和GPU内存消耗。

【应用价值 / Applications】
该研究可广泛应用于标签数据稀缺但无标签数据丰富的场景，如医学影像分析、自然语言处理等领域，帮助在有限标注预算下提升模型性能。FSR模块的即插即用特性使其易于集成到现有SSL系统中，具有良好的实用性和可扩展性。
