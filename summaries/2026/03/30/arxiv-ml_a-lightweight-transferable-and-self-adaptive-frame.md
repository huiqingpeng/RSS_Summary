---
title: "A Lightweight, Transferable, and Self-Adaptive Framework for Intelligent DC Arc-Fault Detection in Photovoltaic Systems"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25749"
published: "2026-03-30"
summarized: "2026-03-31T07:26:47.182475"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种轻量级、可迁移、自适应的学习驱动框架（LD-framework），用于光伏系统中智能直流电弧故障检测。该框架通过三个核心组件（LD-Spec、LD-Align、LD-Adapt）分别解决设备端高效推理、跨硬件迁移和长期自适应更新问题。实验结果表明，该方法在超过53,000个样本上达到0.9999的准确率和0.9996的F1分数，在多种干扰条件下实现0%误报率，并能仅用0.5%-1%的目标数据完成跨硬件迁移。

【方法概述 / Method】
LD-framework包含三个层次：LD-Spec在设备端学习紧凑的光谱表示，实现高效推理和精确电弧判别；LD-Align执行跨硬件表示对齐，通过领域自适应技术缓解硬件异构性导致的分布偏移；LD-Adapt采用云边协同的自适应更新机制，检测未见过的运行工况并执行受控模型演化。

【实验结果 / Results】
该方法在53,000多个标注样本上实现近乎完美的检测性能（准确率0.9999，F1分数0.9996），在逆变器启动、电网切换、负载开关和谐波干扰等易误报场景下保持0%误报率。跨硬件迁移仅需0.5%-1%的标注目标数据即可可靠适配，现场自适应实验显示在未见条件下检测精度可从21%恢复至95%。

【应用价值 / Applications】
该研究为住宅光伏系统提供可规模化部署的AFCI解决方案，能够适应不同厂商的逆变器硬件差异和长期运行中的工况漂移，显著降低因电弧故障引发的火灾风险。其轻量级设计适合边缘设备部署，自适应性减少了人工维护需求，对提升光伏系统安全性和可靠性具有重要工程价值。
