---
title: "SODIUM: From Open Web Data to Queryable Databases"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18447"
published: "2026-03-20"
summarized: "2026-03-20T16:08:14.583848"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SODIUM任务，将开放网络数据形式化为潜在数据库，需通过系统化的实例化来支持下游查询。研究构建了包含105个任务的SODIUM-Bench基准测试，涵盖6个学术领域，用于评估系统自动探索网络、收集并整合多源数据为结构化表格的能力。现有AI代理在该基准上表现不佳（最佳基线仅46.5%准确率），而作者开发的SODIUM-Agent多代理系统通过ATP-BFS算法和缓存管理机制，实现了91.1%的准确率，较最强基线提升约2倍。

【方法概述 / Method】
SODIUM-Agent采用双组件多代理架构，包含网络探索器（web explorer）和缓存管理器（cache manager）。核心创新为ATP-BFS（Assumed to be some form of optimized Breadth-First Search）算法，结合缓存源和导航路径的原则化管理，实现深度全面的网络探索与结构一致的信息提取。

【实验结果 / Results】
在SODIUM-Bench基准测试中，6个先进AI代理均表现不佳，最强基线准确率仅为46.5%。SODIUM-Agent达到91.1%的准确率，较最强基线提升约2倍，较最弱基线提升高达73倍，展现出显著的性能优势。

【应用价值 / Applications】
该研究可广泛应用于学术研究、商业情报分析等领域，帮助领域专家自动整合分散的网络数据，大幅减少数据搜集与预处理时间。其技术方案为构建自动化知识库和智能数据集成系统提供了可复用的框架，特别适用于需要从海量异构网络源中提取结构化信息的场景。
