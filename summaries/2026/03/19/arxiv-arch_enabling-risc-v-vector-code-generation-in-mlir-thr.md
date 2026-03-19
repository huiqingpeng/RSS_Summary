---
title: "Enabling RISC-V Vector Code Generation in MLIR through Custom xDSL Lowerings"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.17800"
published: "2026-03-19"
summarized: "2026-03-19T12:03:36.835765"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种将MLIR与xDSL结合的编译方案，以填补RISC-V向量（RVV）扩展代码生成中缺失的 lowering 阶段。通过自定义中间表示和转换流程，将高层操作系统性地转换为调用RVV内联函数的硬件感知C代码。在K230和BananaPi F3两个真实RISC-V平台上对GEMM内核的评估表明，该方法相比OpenBLAS最高可达12.2 GFLOPS（基线为5.1 GFLOPS），性能提升10%-35%，为RISC-V平台提供了可移植的优化代码生成路径。

【方法概述 / Method】
论文采用MLIR与xDSL相结合的编译框架，通过xDSL实现自定义中间表示（IR）和转换通道（transformation passes），建立从高层抽象到RVV内联函数的完整 lowering 路径。生成的内核以可移植C函数形式输出，可直接集成到现有应用中，无需修改周边软件栈即可实现渐进式采用。

【实验结果 / Results】
在K230和BananaPi F3平台上，该方法生成的GEMM微内核在方阵基准测试和BERT-Large派生的Transformer工作负载中均持续优于OpenBLAS。峰值性能达到12.2 GFLOPS，相比OpenBLAS的5.1 GFLOPS提升显著，在所有评估工作负载上实现10%-35%的性能改进。

【应用价值 / Applications】
该研究为高性能计算和科学计算领域提供了面向RISC-V向量扩展的实用编译工具链，特别适用于需要优化矩阵运算内核（如深度学习推理中的GEMM）的场景。生成的可移植C代码支持增量式集成到现有代码库，降低了在RISC-V平台上部署生产级优化内核的门槛。
