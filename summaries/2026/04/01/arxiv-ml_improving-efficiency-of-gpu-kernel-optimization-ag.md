---
title: "Improving Efficiency of GPU Kernel Optimization Agents using a Domain-Specific Language and Speed-of-Light Guidance"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29010"
published: "2026-04-01"
summarized: "2026-04-02T07:14:32.120776"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了两种提升LLM代理优化GPU内核效率的设计原则：一是开发紧凑的领域特定语言（DSL），使模型能在更高抽象层次进行推理同时保留关键优化杠杆；二是引入"光速"（SOL）指导机制，利用第一性原理性能边界来引导和预算搜索过程。基于这些原则实现的μCUTLASS系统，在59个KernelBench问题上，相比PyTorch实现了1.56倍加速，且SOL指导的预算策略可节省19-43%的token消耗。

【方法概述 / Method】

作者设计了μCUTLASS这一领域特定语言，其编译器基于CUTLASS后端，涵盖内核配置、尾缀融合和多级流水线等优化维度，使LLM代理从生成底层CUDA代码转向操作高层DSL原语。同时提出SOL指导机制，通过计算理论性能上限来估计优化空间、指导试验优先级，并识别接近理论极限或存在benchmark gaming的问题。

【实验结果 / Results】

在相同迭代预算下，使用GPT-5-mini从生成底层代码切换到DSL代码，将相对于PyTorch的几何平均性能从0.40倍回归转变为1.27倍加速；添加SOL指导后进一步提升至1.56倍。跨模型层级比较显示，较弱的模型配合μCUTLASS+SOL指导能以更低token成本超越更强的基线代理。最优SOL预算策略在保持至少95%加速效果的同时，实现1.68倍的效率增益。

【应用价值 / Applications】

该研究可显著降低GPU内核自动优化的计算成本和时间开销，适用于深度学习编译器、高性能计算库开发等场景。SOL指导机制不仅能优化搜索效率，还能检测内核实现中的benchmark gaming行为，确保优化结果的正确性和可靠性，对生产环境中的AI加速器和科学计算应用具有重要实践意义。
