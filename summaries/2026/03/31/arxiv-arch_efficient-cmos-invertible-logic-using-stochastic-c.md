---
title: "Efficient CMOS Invertible Logic Using Stochastic Computing"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.27030"
published: "2026-03-31"
summarized: "2026-04-01T07:15:50.668276"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种基于随机计算（Stochastic Computing）的可逆逻辑（Invertible Logic）CMOS实现方案。可逆逻辑具有双向运算能力：正向模式下根据输入产生输出，反向模式下则根据固定输出求解相容的输入值。作者设计了一种可逆随机门的设计方法，仅需少量CMOS硬件即可实现，并成功扩展构建了可逆随机加法器和乘法器电路。实验验证了该设计在乘法和因数分解任务中的正确操作，并展示了可逆乘法器ASIC的实测结果。

【方法概述 / Method】
该研究采用基于脉冲神经网络的随机计算架构来实现可逆逻辑功能，通过设计可逆随机门（invertible stochastic gates）作为基本构建单元。这些门电路利用随机比特流表示概率值，通过简单的CMOS晶体管级电路实现双向推理能力，并可级联组合成复杂算术电路。

【实验结果 / Results】
实验结果表明，所设计的可逆随机电路能够正确执行乘法和因数分解运算，验证了反向模式求解输入值的有效性。研究团队还完成了可逆乘法器电路的ASIC流片与实测，证实了该方案在物理硬件上的可行性和正确性。

【应用价值 / Applications】
该研究为因数分解、组合优化等NP难问题提供了高能效的硬件加速方案，可应用于密码学分析、运筹优化和人工智能推理等领域。基于标准CMOS工艺的实现方式使其具有良好的可扩展性和产业化潜力，为后摩尔时代的新型计算范式提供了实用化的技术路径。
