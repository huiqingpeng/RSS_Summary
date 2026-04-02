---
title: "A Security-Aware Nonlinearity Study of FPGA-Based Time-to-Digital Converters for Quantum Key Distribution Systems"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2604.00229"
published: "2026-04-02"
summarized: "2026-04-03T07:15:12.529208"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了FPGA时间数字转换器（TDC）固有非线性特性对量子密钥分发（QKD）系统安全性的影响，指出传统校准后评估方法忽略了原始延迟线不均匀性对符合计时和量子比特误码率（QBER）的潜在影响。作者建立了结合随机定时不确定性与确定性非线性的系统级保守模型，并提出基于LUT辅助延迟整形和布局约束的芯片级缓解策略。实验在低成本的Zynq-7000 FPGA上复现了两个开源TDC，实现了积分非线性（INL）降低14%-21%，秘密分数提升3.7%-14.2%，表明原始FPGA-TDC非线性在定时敏感的QKD实现中值得明确考虑。

【方法概述 / Method】
论文采用系统级建模方法，将FPGA-TDC的随机定时不确定性与确定性非线性相结合，分析非线性如何传播至QKD定时指标。提出的缓解策略利用查找表（LUT）辅助延迟整形和布局约束，在不依赖统计校准的情况下减少严重的码宽不规则性。

【实验结果 / Results】
在Zynq-7000 FPGA上对两个开源TDC进行复现实验，优化设计相比非优化设计实现了14%-21%的积分非线性（INL）降低，从而减少了QBER贡献，估计秘密分数提升3.7%-14.2%。

【应用价值 / Applications】
该研究对基于低成本FPGA的QKD系统实现具有重要价值，为量子密码设备的安全设计和性能优化提供了实用指导，特别是在需要高精度定时测量的量子通信网络节点部署中具有应用前景。
