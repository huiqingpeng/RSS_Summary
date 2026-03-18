---
title: "Mastering the Minority: An Uncertainty-guided Multi-Expert Framework for Challenging-tailed Sequence Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15708"
published: "2026-03-18"
summarized: "2026-03-18T15:34:31.955369"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对序列学习中的数据不平衡问题，提出了一种基于不确定性的多专家融合网络（UME）框架。该框架通过集成LoRA实现参数高效建模，利用Dempster-Shafer理论引导专家序列专业化，并基于不确定性动态加权融合专家预测。在四个公开层次文本分类数据集上，UME实现了最优性能，在单个类别上较最佳基线提升达17.97%，同时训练参数减少10.32%。

【方法概述 / Method】
UME框架包含三项核心创新：首先采用集成LoRA（Ensemble LoRA）进行参数高效微调；其次引入基于Dempster-Shafer理论的序列专业化机制，使各专家专注于不同的困难尾部类别；最后设计不确定性引导的融合机制，利用DST的确定性度量动态加权专家意见，优先采纳置信度最高的专家预测以解决冲突。

【实验结果 / Results】
在四个公开层次文本分类数据集上的广泛实验表明，UME达到当前最优性能。具体而言，在单个类别上性能提升最高达17.97%，同时将可训练参数数量减少最多10.32%，验证了该框架在提升尾部类别识别能力的同时保持了参数效率。

【应用价值 / Applications】
该研究适用于存在严重类别不平衡的序列学习任务，如层次文本分类、长尾推荐系统和稀有事件检测等场景。UME框架通过不确定性引导的专家协调机制，为处理挑战性尾部序列学习提供了原则性解决方案，对提升模型在真实世界不平衡数据上的泛化能力具有重要实践意义。
