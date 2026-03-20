---
title: "Quine: Realizing LLM Agents as Native POSIX Processes"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2603.18030"
published: "2026-03-20"
summarized: "2026-03-20T12:03:27.327340"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了Quine，一种将LLM智能体实现为原生POSIX进程的运行时架构。与现有在应用层实现隔离、调度和通信的智能体框架不同，Quine将智能体身份映射为PID、接口映射为标准流和退出状态、状态映射为内存/环境变量/文件系统、生命周期映射为fork/exec/exit。通过将智能体抽象建立在操作系统进程模型之上，Quine直接从内核继承了隔离性、组合性和资源控制能力，同时自然支持递归委托、通过exec进行上下文更新以及与shell原生集成。

【方法概述 / Method】

Quine采用单一可执行文件设计，该文件通过递归生成自身的新实例来实现智能体模型。核心方法是将LLM智能体的抽象概念与POSIX进程语义进行显式一一映射，利用操作系统原生机制而非应用层编排器来管理智能体的生命周期和交互。

【实验结果 / Results】

论文主要贡献在于架构设计和概念验证，而非传统意义上的性能基准测试。作者通过参考实现展示了该模型的可行性，并深入分析了POSIX进程模型作为认知运行时的局限性，指出两个需要扩展的方向：任务相对世界（task-relative worlds）和可修订时间（revisable time）。

【应用价值 / Applications】

该研究为LLM智能体部署提供了更轻量、更原生的系统集成方案，特别适用于需要与现有Unix/Linux工具链深度结合的场景。通过消除应用层编排开销，Quine有望提升智能体系统的可组合性和资源效率，为构建更可靠、更易调试的智能体基础设施奠定基础。
