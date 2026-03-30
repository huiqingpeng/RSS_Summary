---
title: "CGRA4ML: A Hardware/Software Framework to Implement Neural Networks for Scientific Edge Computing"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2408.15561"
published: "2026-03-30"
summarized: "2026-03-31T07:17:22.485162"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CGRA4ML，一个面向科学边缘计算的开源模块化框架，用于生成可参数化的粗粒度可重构阵列（CGRA）加速器。该框架针对科学应用中的常见机器学习计算模式，提供从Python API到SystemVerilog硬件、TCL工具流和C运行时的全栈基础设施，支持通过AXI兼容接口和开源DMA组件实现无缝系统集成，并自动生成加速器固件。研究展示了该框架在ASIC和FPGA设计流程中实现常见科学边缘神经网络的有效性。

【方法概述 / Method】
CGRA4ML采用硬件/软件协同设计方法，生成可综合的SystemVerilog RTL代码，支持参数化配置以适应不同的神经网络架构。框架包含完整的验证套件和运行时固件栈，通过AXI标准接口确保与多样化SoC平台的兼容性，并提供自动化工具链简化从高层模型到硬件部署的转换流程。

【实验结果 / Results】
论文通过ASIC和FPGA设计流程验证了CGRA4ML在实现常见科学边缘神经网络方面的有效性。框架展示了高度的模块化特性，能够支持不同规模和应用场景的加速器生成，同时保持了高性能与可编程性的平衡，为科学计算任务提供了高效的近传感器处理能力。

【应用价值 / Applications】
CGRA4ML适用于需要近传感器实时处理的科学边缘计算场景，如物理实验中的异常检测、天文观测的模式识别以及环境监测中的实时决策等。该框架使科研人员能够专注于算法创新而非底层硬件优化，显著降低了科学机器学习加速器的设计门槛和开发周期。
