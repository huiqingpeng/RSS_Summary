---
title: "Transformers Learn Robust In-Context Regression under Distributional Uncertainty"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18564"
published: "2026-03-20"
summarized: "2026-03-20T12:13:31.125931"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了Transformer在分布不确定性下的上下文学习（in-context learning）能力，突破了以往研究中i.i.d.数据、高斯噪声和高斯回归系数等限制性假设。作者系统分析了Transformer在非高斯系数、重尾噪声和非i.i.d.提示等广泛分布偏移场景下的表现，发现Transformer在所有测试设置中均能匹配或超越经典的最优/次优最大似然估计基线方法，证明了其强大的鲁棒自适应能力。

【方法概述 / Method】

研究采用线性回归作为测试平台，在多种分布偏移条件下训练Transformer模型，包括非高斯回归系数分布、重尾噪声分布以及具有时间相关性的非独立同分布提示序列。实验设计将Transformer与对应最大似然准则下的经典最优或次优估计器进行系统性对比。

【实验结果 / Results】

实验结果表明，在所有分布偏移设置下，Transformer始终能够达到或超过经典基线方法的性能，即使在经典方法理论最优的设定中也不例外。这一发现挑战了"Transformer仅能在理想化条件下有效学习"的观点，揭示了其超越传统统计估计器的泛化能力。

【应用价值 / Applications】

该研究为Transformer在实际复杂环境中的应用提供了理论支撑，特别是在金融预测、科学计算和实时决策等数据分布未知且动态变化的场景。研究成果有助于推动更可靠的上下文学习系统部署，减少对数据分布假设的依赖，提升模型在开放世界环境中的鲁棒性。
