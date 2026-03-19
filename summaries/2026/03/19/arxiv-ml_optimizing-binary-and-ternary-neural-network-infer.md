---
title: "Optimizing Binary and Ternary Neural Network Inference on RRAM Crossbars using CIM-Explorer"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2505.14303"
published: "2026-03-19"
summarized: "2026-03-19T14:15:30.837351"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了CIM-Explorer，一个用于优化二值神经网络（BNN）和三值神经网络（TNN）在RRAM（阻变存储器）交叉阵列上进行推理的模块化工具包。该工具集成了端到端编译器栈、多种映射选项和仿真器，支持跨不同交叉阵列参数和映射策略的设计空间探索（DSE）以估计推理精度。研究表明，CIM-Explorer能够伴随从早期精度估计、映射选择到最终芯片编译的完整设计流程，并通过案例研究展示了不同配置下的预期精度表现。

【方法概述 / Method】

CIM-Explorer采用模块化架构，整合了编译、映射、仿真和设计空间探索功能，专门针对RRAM交叉阵列的非理想特性（如单元变异性）进行优化。该方法支持将BNN/TNN高效映射到仅使用低阻态（LRS）和高阻态（HRS）的二值RRAM硬件，突破了传统8位量化的局限。

【实验结果 / Results】

论文通过设计空间探索案例研究，量化了不同映射策略和交叉阵列参数组合下的推理精度表现。实验结果表明，CIM-Explorer能够有效评估多种硬件配置对BNN/TNN推理准确性的影响，为硬件设计决策提供数据支持。

【应用价值 / Applications】

CIM-Explorer可应用于基于RRAM的存内计算（CIM）系统开发全流程，特别适用于边缘AI设备的低功耗神经网络推理加速。该工具开源发布于GitHub，有助于研究人员和工程师优化BNN/TNN在新兴非易失性存储器上的部署，推动突破冯·诺依曼瓶颈的硬件架构实用化。
