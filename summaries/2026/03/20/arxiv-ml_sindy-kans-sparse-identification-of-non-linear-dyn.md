---
title: "SINDy-KANs: Sparse identification of non-linear dynamics through Kolmogorov-Arnold networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18548"
published: "2026-03-20"
summarized: "2026-03-20T12:13:24.834682"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SINDy-KANs方法，将Kolmogorov-Arnold网络（KANs）与稀疏非线性动力学识别（SINDy）相结合，以提升神经网络的可解释性。该方法在每个激活函数层面应用SINDy，同时保持深度KANs的函数组合能力，克服了KANs解不一定稀疏以及SINDy受限于预定义函数库的缺陷。实验表明，该方法在动态系统等多种符号回归任务中实现了准确的方程发现。

【方法概述 / Method】
SINDy-KANs采用联合训练策略，同时优化KAN网络和类SINDy稀疏表示，在每个激活函数上施加稀疏性约束而非仅在网络输出层。这种设计既保留了KANs通过可学习的单变量激活函数实现深度函数组合的能力，又通过逐层稀疏识别获得了更具可解释性的符号表达式。

【实验结果 / Results】
论文在多个符号回归任务和动态系统上验证了SINDy-KANs的有效性，展示了该方法能够准确发现涵盖广泛系统的控制方程。结果表明，相比单独的KANs或SINDy方法，SINDy-KANs在保持表达灵活性的同时显著提升了学习结果的稀疏性和可解释性。

【应用价值 / Applications】
SINDy-KANs适用于科学发现、物理定律挖掘和动态系统建模等场景，特别需要从观测数据中自动提取简洁、可解释的控制方程的领域。该方法为工程系统分析、计算物理学和自动化科学发现提供了新的工具，有助于构建兼具预测精度与理论透明度的数据驱动模型。
