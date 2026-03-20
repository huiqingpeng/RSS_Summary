---
title: "Tackling the Sign Problem in the Doped Hubbard Model with Normalizing Flows"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18205"
published: "2026-03-20"
summarized: "2026-03-20T13:10:33.395857"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对有限化学势下Hubbard模型中的符号问题（sign problem），提出了一种基于归一化流（normalizing flows）的解决方案。作者将先前在半填充条件下发展的归一化流方法扩展到有限化学势情形，通过引入退火方案（annealing scheme）实现了遍历采样。与电荷基下的先进混合蒙特卡洛方法相比，该方法在精确重现精确对角化结果的同时，将统计不确定性降低了一个数量级，为掺杂关联系统的模拟开辟了新途径。

【方法概述 / Method】
论文采用辅助场（auxiliary-field）表述下的自旋基（spin basis），该基组能够缓解符号问题但存在严重的遍历性问题。作者引入归一化流神经网络构建变分波函数，并通过退火方案逐步引导采样过程，从而克服遍历性障碍，实现有效的蒙特卡洛采样。

【实验结果 / Results】
该方法在有限化学势下的Hubbard模型模拟中，成功复现了精确对角化的基准结果。与当前最先进的电荷基混合蒙特卡洛方法相比，统计误差显著降低约一个数量级，证明了其在精度和效率上的优势。

【应用价值 / Applications】
该研究为高温超导、重费米子材料等掺杂关联电子系统的量子模拟提供了新的计算工具。归一化流与退火采样的结合有望推广到其他存在符号问题的强关联系统，推动凝聚态物理中多体量子问题的数值研究。
