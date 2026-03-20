---
title: "Capturing reduced-order quantum many-body dynamics out of equilibrium via neural ordinary differential equations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.13913"
published: "2026-03-20"
summarized: "2026-03-20T14:09:18.505499"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究利用神经常微分方程（neural ODE）来学习非平衡量子多体系统中两粒子约化密度矩阵（2RDM）的动力学演化。研究发现，神经ODE能够在仅依赖瞬时两粒子累积量、不含显式三粒子信息的情况下重现2RDM动力学，但仅限于两粒子与三粒子累积量之间Pearson相关性较强的参数区域。该工作将神经ODE确立为一种模型无关的诊断工具，用于界定累积量展开方法的适用范围，并指导非局域闭合方案的开发。

【方法概述 / Method】

作者采用神经ODE模型，直接从精确的2RDM时间序列数据中学习动力学演化，无需进行维度约减或显式引入三粒子信息。通过训练神经网络来近似2RDM的时间导数，从而构建一个时间局域的闭合泛函，并系统性地检验该数据驱动方法在不同动力学区域的有效性。

【实验结果 / Results】

神经ODE的成功与否与两粒子-三粒子累积量的Pearson相关性密切相关：在正相关区域预测准确，而在反相关或无相关区域则失效。时间平均的三粒子关联累积量大小是预测成功的主要指标——中等累积量时神经ODE与现有TD2RDM重构方法均准确，但较强累积量导致系统性失效，表明此时必须引入记忆依赖的核函数。

【应用价值 / Applications】

该研究为量子多体系统的快速数据驱动模拟开辟了新途径，特别适用于强关联量子物质的非平衡动力学研究。神经ODE框架可作为诊断工具，帮助研究者识别何时需要发展包含记忆效应的非局域闭合方案，从而指导更高效的量子动力学计算方法的设计。
