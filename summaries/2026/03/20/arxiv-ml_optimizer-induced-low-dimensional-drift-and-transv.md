---
title: "Optimizer-Induced Low-Dimensional Drift and Transverse Dynamics in Transformer Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.23696"
published: "2026-03-20"
summarized: "2026-03-20T14:11:50.105852"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究分析了Transformer模型在使用AdamW优化器训练时的累积参数轨迹，发现存在一个主导的"骨干"低维漂移方向，能够捕获初始化后60-80%的长期位移。该方向在滚动训练窗口中高度稳定，但在不同阶段（特别是目标重加权后）会逐渐重新定向。研究表明，每批梯度与骨干方向几乎呈噪声级对齐，而优化器积分更新则强烈对齐该方向，说明这种结构源于累积优化器动态而非瞬时梯度几何。

【方法概述 / Method】
论文通过分析累积参数轨迹来研究Transformer训练动态，对比了AdamW与SGD类优化器的行为差异，并通过调整β₂参数进行消融实验。此外，研究设计了"再加热"实验来探测横向模式的可激发性。

【实验结果 / Results】
SGD类优化器完全消除了上述低维结构，而降低β₂参数会平滑地削弱骨干主导性和再加热恢复能力。再加热实验表明，横向探测模式可以被短暂重新激发，而不会显著改变已累积的骨干漂移。

【应用价值 / Applications】
该研究为理解神经网络训练动态提供了轨迹层面的几何特征刻画，将研究焦点从瞬时梯度性质转向累积更新动态，有助于优化器设计、训练过程监控以及模型微调策略的改进。
