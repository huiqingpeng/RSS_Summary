---
title: "Learning through Creation: A Hash-Free Framework for On-the-Fly Category Discovery"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.13858"
published: "2026-03-18"
summarized: "2026-03-18T19:03:56.630937"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对即时类别发现（On-the-Fly Category Discovery, OCD）任务中离线训练与在线推理之间的优化错位问题，提出了"Learning through Creation (LTC)"框架。该框架通过在线伪未知样本生成器（MKEE）在离线训练阶段直接注入新类别感知能力，无需依赖哈希编码或特征压缩。在七个基准数据集上的实验表明，LTC在所有类别准确率上较先前方法提升1.5%至13.1%。

【方法概述 / Method】
LTC采用完全基于特征的无哈希架构，核心是一个轻量级在线伪未知样本生成器，该生成器通过核能量最小化和熵最大化（MKEE）驱动，并与模型动态协同进化、实时合成伪新类别样本。生成的样本通过带自适应阈值的双最大间隔目标函数融入训练，使模型通过"显式创造"来增强对未知区域的界定和检测能力。

【实验结果 / Results】
LTC在七个基准数据集上 consistently 超越现有方法，所有类别准确率提升幅度为1.5%至13.1%。该方法以可忽略的计算成本实现伪样本的在线生成，避免了传统方法中预生成合成样本或依赖哈希编码带来的表示能力限制。

【应用价值 / Applications】
LTC适用于需要实时识别已知类别同时动态发现新类别的场景，如自动驾驶中的突发障碍物识别、监控系统的异常行为检测、以及开放世界视觉识别系统。该框架的哈希自由和特征驱动特性使其更适合部署于资源受限的边缘设备，为构建自适应、可扩展的开放集识别系统提供了新范式。
