---
title: "GeneTEK: Low-power, high-performance and scalable FPGA architecture for exact unit-cost edit distance"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2509.01020"
published: "2026-03-26"
summarized: "2026-03-27T07:13:15.463114"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了GeneTEK，一种基于FPGA的低功耗、高性能可扩展加速器架构，用于计算精确单位代价编辑距离。该架构采用Myers算法和高层次综合技术，支持最长1000 bp的序列比对，相比领先的CPU和GPU解决方案，执行速度提升高达113%，能耗降低达111倍。同时，GeneTEK的比较矩阵容量比现有FPGA脉动阵列方案大13倍，验证了FPGA在成对序列比对中的能效优势。

【方法概述 / Method】
GeneTEK采用软硬件协同设计方法，基于worker架构实现多层次并行化和高效内存利用。该模板使用高层次综合（HLS）技术实现Myers算法，通过灵活的FPGA加速器设计克服长序列比对时的硬件资源限制，实现了对长达1000 bp序列的可扩展支持。

【实验结果 / Results】
在Xilinx Zynq UltraScale+ FPGA上的实例化测试表明，GeneTEK相比主流CPU和GPU方案实现了最高113%的加速比和111倍的能耗降低。其硬件资源利用效率显著提升，可容纳的比较矩阵规模达到此前FPGA脉动阵列方案的13倍，突破了长序列比对的扩展性瓶颈。

【应用价值 / Applications】
该研究为下一代测序（NGS）数据分析中的成对序列比对步骤提供了高能效硬件加速方案，适用于基因组学大数据处理场景。GeneTEK可集成于生物信息学流程中，帮助研究人员在降低计算能耗的同时处理更长的测序读段，对推动精准医疗、大规模基因组研究等应用具有重要价值。
