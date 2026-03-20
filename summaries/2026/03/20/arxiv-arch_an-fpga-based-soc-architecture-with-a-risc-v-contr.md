---
title: "An FPGA-Based SoC Architecture with a RISC-V Controller for Energy-Efficient Temporal-Coding Spiking Neural Networks"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.18054"
published: "2026-03-20"
summarized: "2026-03-20T12:03:47.696580"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种面向时序编码脉冲神经网络（SNN）的紧凑型片上系统（SoC）架构，通过集成RISC-V控制器与事件驱动SNN核心，利用二值化权重将乘法运算替换为位运算，并引入脉冲时间排序器和事件跳过机制来降低计算开销。该设计在Xilinx Artix-7 FPGA上实现了全片上运行，权重存储减少16倍，在MNIST和FashionMNIST数据集上分别达到97.0%和88.3%的准确率，为边缘端实时神经形态推理提供了高效可扩展的平台。

【方法概述 / Method】
该架构采用RISC-V软核处理器作为系统控制器，配合专用硬件加速的事件驱动SNN核心；通过权值二值化将复杂乘法转换为简单的位运算操作，并设计了脉冲时间排序模块仅处理活跃脉冲，同时动态跳过非信息性事件以减少无效计算。

【实验结果 / Results】
在Xilinx Artix-7 FPGA上的完整实现表明，该设计相比传统方案实现了最高16倍的权重存储压缩，显著降低了计算开销和推理延迟；在标准图像分类基准测试中，MNIST准确率达97.0%，FashionMNIST准确率达88.3%，验证了其在资源受限场景下的有效性和实用性。

【应用价值 / Applications】
该自包含SoC设计适用于电池供电的边缘AI设备，如可穿戴健康监测、智能传感器节点和物联网终端，能够在极低功耗预算下完成实时模式识别任务；其可扩展架构也为未来更复杂的神经形态计算系统提供了参考设计模板。
