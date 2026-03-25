---
title: "Alibaba XuanTie C950 – A powerful, RVA23-complaint 64-bit RISC-V core for Edge AI computing"
source: "CNX Software"
url: "https://www.cnx-software.com/2026/03/25/alibaba-xuantie-c950-a-powerful-rva23-complaint-64-bit-risc-v-core-for-edge-ai-computing/"
published: "2026-03-25"
summarized: "2026-03-26T07:00:33.493739"
ai_provider: "openai"
---

【是什么 / What it is】

阿里巴巴发布了玄铁C950，一款面向边缘AI计算的高性能64位RISC-V处理器核心IP。该核心采用乱序超标量微架构，符合RVA23规范，支持所有可选RISC-V扩展指令集，并集成了专有的矩阵扩展（AME）和可对接张量处理引擎（TPE）AI协处理器。

Alibaba has released the XuanTie C950, a high-performance 64-bit RISC-V processor core IP designed for edge AI computing. It features an out-of-order superscalar microarchitecture, is RVA23-compliant, supports all optional RISC-V extensions, and integrates proprietary Matrix Extension (AME) with connectivity to the Tensor Processing Engine (TPE) AI coprocessor.

---

【为什么重要 / Why it matters】

C950在3.2GHz下Specint2006得分达70，创下RISC-V核心性能新纪录，性能是前代C920的三倍，标志着RISC-V架构正式跨入高性能计算和AI推理领域。同时，其对Qwen3-256B和DeepSeek V3-671B等大模型的原生支持，以及5nm工艺量产，显示中国厂商在开放指令集生态中已具备与ARM/x86竞争的技术实力。

The C950 achieves a record-breaking Specint2006 score of 70 at 3.2GHz—three times faster than its predecessor C920—marking RISC-V's official entry into high-performance computing and AI inference. Its native support for large models like Qwen3-256B and DeepSeek V3-671B, combined with 5nm manufacturing readiness, demonstrates Chinese vendors' competitive technical strength against ARM/x86 in the open ISA ecosystem.

---

【我能用什么 / How I can use it】

开发者可关注玄铁C950的GNU/LLVM工具链和QEMU仿真支持，提前在软件层面适配RISC-V高性能生态；AI工程师可研究AME扩展与TPE协处理器的协同编程模型，为边缘LLM推理优化算子；芯片设计企业可评估其CHI.E/CHI.F总线接口与多核集群方案，用于定制化AI SoC架构设计。

Developers can leverage its officially supported GNU/LLVM toolchain and QEMU emulation to adapt software for the high-performance RISC-V ecosystem early; AI engineers can study the AME-TPE coprocessor programming model to optimize operators for edge LLM inference; chip design firms can evaluate its CHI.E/CHI.F bus interfaces and multi-cluster configurations for custom AI SoC architectures.
