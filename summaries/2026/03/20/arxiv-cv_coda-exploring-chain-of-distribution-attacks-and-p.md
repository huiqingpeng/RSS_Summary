---
title: "CoDA: Exploring Chain-of-Distribution Attacks and Post-Hoc Token-Space Repair for Medical Vision-Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18545"
published: "2026-03-20"
summarized: "2026-03-20T15:11:40.668943"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CoDA（Chain-of-Distribution Attacks）框架，用于系统评估医学视觉-语言模型（MVLMs）在临床工作流程中面临的分布偏移威胁。研究发现，由采集、重建、显示和传输等环节组成的链式分布攻击比单一环节攻击更能显著降低CLIP风格MVLMs的零样本性能。此外，主流多模态大语言模型在作为医学图像质量审计器时表现不佳，而本文提出的基于教师引导的token空间自适应修复策略可有效提升模型对攻击后图像的鲁棒性。

【方法概述 / Method】
CoDA通过组合采集类阴影、重建与显示重映射、传输与导出退化等阶段，构建临床合理的分布偏移；在掩码结构相似性约束下，联合优化各阶段组合与参数以在保持视觉合理性的同时诱导模型失效。修复阶段采用教师引导的token空间自适应方法，结合patch级对齐机制恢复模型性能。

【实验结果 / Results】
在脑部MRI、胸部X光和腹部CT三种医学影像模态上，CoDA链式攻击使CLIP风格MVLMs的零样本性能显著下降，且组合攻击效果优于任何单一阶段；专有MLLMs在CoDA偏移样本上表现出审计可靠性下降和高置信度错误，而医学专用MLLMs在图像质量审计方面存在明显缺陷；所提修复策略在归档的CoDA输出上有效提升了准确率。

【应用价值 / Applications】
本研究为MVLMs在临床部署中的可靠性评估提供了贴近真实工作流的威胁建模框架，有助于识别医学AI系统的脆弱环节；提出的轻量级token空间修复方法可部署于现有系统以增强鲁棒性，同时警示临床实践中需谨慎依赖通用或医学专用MLLMs进行图像质量验证。
