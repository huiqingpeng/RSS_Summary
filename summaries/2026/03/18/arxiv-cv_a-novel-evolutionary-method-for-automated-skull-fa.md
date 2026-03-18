---
title: "A Novel Evolutionary Method for Automated Skull-Face Overlay in Computer-Aided Craniofacial Superimposition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.00170"
published: "2026-03-18"
summarized: "2026-03-18T18:33:22.286255"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种名为Lilium的自动化进化方法，用于解决颅面叠加（Craniofacial Superimposition）中的关键步骤——颅骨-面部叠加（Skull-Face Overlay, SFO）。该方法通过三维锥体表示显式建模软组织厚度变异性，并利用差分进化算法优化参数，同时结合解剖学、形态学和摄影学合理性约束，在准确性和鲁棒性方面均优于现有最先进方法。

【方法概述 / Method】

Lilium采用基于三维锥体的软组织厚度表示模型，将软组织变异性量化为可优化的几何参数；通过差分进化（Differential Evolution）算法对这些参数进行全局优化搜索，并整合多种约束条件（包括标志点匹配、相机参数一致性、头部姿态对齐、颅骨包含于面部边界内以及区域平行性）来模拟法医专家的实际操作流程。

【实验结果 / Results】

实验结果表明，Lilium在颅骨-面部叠加任务中的准确性和鲁棒性均显著优于现有最先进方法；该方法能够有效处理个体间软组织厚度差异带来的不确定性，在多种复杂场景下保持稳定的叠加性能。

【应用价值 / Applications】

该研究主要应用于法医人类学领域，可辅助鉴定无名遗骸身份，为刑事侦查和灾难受害者识别提供可靠的计算机辅助工具；自动化特性有望减少法医专家的主观判断差异，提高颅面叠加分析的标准化程度和效率。
