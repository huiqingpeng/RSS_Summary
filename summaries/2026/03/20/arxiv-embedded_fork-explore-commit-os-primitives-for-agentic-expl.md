---
title: "Fork, Explore, Commit: OS Primitives for Agentic Exploration"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2602.08199"
published: "2026-03-20"
summarized: "2026-03-20T12:03:41.212272"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了"分支上下文"(branch context)这一新型操作系统抽象，专为AI智能体的探索性任务设计。该抽象支持智能体并行探索多个解决方案路径，并仅提交成功的路径。论文实现了两个互补组件：基于FUSE的文件系统BranchFS（已开源）和提议的Linux系统调用branch()。实验表明，BranchFS可在350微秒内完成分支创建，且提交开销与修改规模成正比。

【方法概述 / Method】
论文设计了分支上下文的三阶段生命周期：fork（创建独立环境）、explore（并行探索）、commit/abort（原子提交或回滚）。BranchFS通过用户空间FUSE实现copy-on-write隔离的文件系统视图，无需root权限；branch()系统调用则在内核层提供进程组隔离和"首次提交获胜"的协调机制，支持嵌套式层次化探索。

【实验结果 / Results】
BranchFS的初步评估显示：分支创建时间低于350微秒，且与基础文件系统大小无关；提交开销与修改量成正比，小规模修改的提交时间低于1毫秒。性能数据表明该方案适用于高频次的智能体探索场景。

【应用价值 / Applications】
该研究直接服务于AI代码生成、自动化软件工程、科学计算实验等需要大规模并行试错的应用场景。分支上下文为智能体提供了安全、高效、可回滚的沙箱环境，避免了传统容器或虚拟机方案的开销，有望成为下一代智能体操作系统的基础原语。
