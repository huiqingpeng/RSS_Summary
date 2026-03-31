---
title: "A 64-Spin All-to-All CMOS Ising Machine with Landscape Perturbation Achieving 2.28 nJ/Edge-Bit Energy-to-Solution"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.27402"
published: "2026-03-31"
summarized: "2026-04-01T07:15:56.146148"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文在65nm CMOS工艺中实现了一种64自旋全连接电流模式耦合伊辛机，芯片面积为0.943 mm²，支持31个系数级别，并达到了2.28 nJ/edge-bit的求解能量效率（ETS）。该设计采用连续编程刷新技术，不仅缓解了漏电流问题，还提供了一种确定性能量景观扰动机制，显著提升了求解成功率。

【方法概述 / Method】
该伊辛机采用全连接电流模式耦合架构实现64自旋系统，通过连续编程刷新机制动态更新权重系数。这一机制兼具双重功能：一方面补偿漏电流导致的精度损失，另一方面通过确定性方式扰动能量景观，帮助系统跳出局部最优解。

【实验结果 / Results】
芯片在0.943 mm²面积内实现了31级系数精度，能量效率达到2.28 nJ/edge-bit。实验表明，启用能量景观扰动后，求解成功率相比无扰动操作模式有显著提升，证明了该机制在改善解质量方面的一致有效性。

【应用价值 / Applications】
该高能效伊辛机可应用于组合优化问题的加速求解，如旅行商问题、图划分、调度优化等NP难问题。其超低能耗特性使其适用于边缘计算和嵌入式场景，为专用优化硬件在物联网、物流规划和金融建模等领域的实际部署提供了可行方案。
