---
title: "ZipServ: Fast and Memory-Efficient LLM Inference with Hardware-Aware Lossless Compression"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.17435"
published: "2026-03-19"
summarized: "2026-03-19T12:03:59.205358"
ai_provider: "openai"
---

【论文摘要 / Abstract】
ZipServ 是一个面向 GPU 的硬件感知无损压缩框架，旨在解决大语言模型（LLM）推理中的内存和带宽瓶颈问题。该研究提出了一种固定长度的张量核心感知三重位图编码（TCA-TBE）格式，实现了常数时间并行解码，并设计了融合解压缩-GEMM 内核（ZipGEMM），可直接将压缩权重解压到 Tensor Core 寄存器中。实验表明，ZipServ 可将模型大小减少高达 30%，相比 NVIDIA cuBLAS 实现 2.21 倍的内核级加速，端到端推理相比 vLLM 平均提速 1.22 倍，是首个在 GPU 上同时实现存储节省和显著加速的无损压缩系统。

【方法概述 / Method】
ZipServ 采用"加载压缩、计算解压"的协同设计策略，核心包括 TCA-TBE 编码格式和 ZipGEMM 融合内核。TCA-TBE 通过固定长度位流设计避免了传统熵编码的变长问题，从而保持 GPU 的 SIMT 并行性；ZipGEMM 则将解压缩操作与矩阵乘法融合，直接在 Tensor Core 寄存器中完成解压，消除了中间缓冲区并最大化计算强度。

【实验结果 / Results】
ZipServ 在模型压缩方面实现了最高 30% 的体积缩减；在内核层面，相比 NVIDIA cuBLAS 获得最高 2.21 倍加速；在端到端推理场景下，相比主流推理框架 vLLM 平均提速 1.22 倍。这些结果表明 ZipServ 成功突破了无损压缩通常伴随推理延迟增加的瓶颈。

【应用价值 / Applications】
ZipServ 可广泛应用于云端和边缘场景的 LLM 推理服务，尤其适用于显存受限或带宽紧张的高性能 GPU 部署环境。该技术能够在保证模型比特级精确性的前提下降低存储成本、提升推理吞吐量，对需要严格数值一致性的金融、医疗等关键领域具有重要价值，同时为大规模模型的高效部署提供了新的基础设施方案。
