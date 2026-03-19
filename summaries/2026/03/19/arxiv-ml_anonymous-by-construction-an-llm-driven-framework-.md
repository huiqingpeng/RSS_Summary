---
title: "Anonymous-by-Construction: An LLM-Driven Framework for Privacy-Preserving Text"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17217"
published: "2026-03-19"
summarized: "2026-03-19T13:10:23.670895"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种本地部署的LLM驱动文本匿名化框架，通过将个人身份信息(PII)替换为真实且类型一致的替代内容来实现隐私保护。该方法完全在组织边界内执行，防止数据外泄的同时保持文本流畅性和任务相关语义。实验表明，该框架在隐私-效用-可训练性综合前沿上超越了基于规则的业界标准（Microsoft Presidio、Google DLP）和最先进的ZSTS方法，实现了负责任的AI数据使用。

【方法概述 / Method】
该框架采用本地大语言模型构建端到端的替换流水线，将PII实体替换为上下文连贯、类型保持的替代文本，而非简单的脱敏标记。评估协议采用多指标跨技术对比，通过微调紧凑型编码器（BERT+LoRA）量化隐私保护下的可训练性损失，并测试匿名化层插入问答代理后的响应质量。

【实验结果 / Results】
在Action-Based Conversation Dataset上的系统评估显示，该方法达到最先进的隐私保护水平，同时实现最小主题漂移、强事实效用和低可训练性损失。相比规则基线和NER基线以及ZSTS变体，本方法在隐私-效用-可训练性综合权衡上全面领先，下游微调性能退化有限。

【应用价值 / Applications】
该研究为组织内部部署问答代理提供了隐私保障方案，确保敏感内容不会暴露给第三方API，支持负责任的代理式AI部署。生成的匿名化语料库可直接用于下游模型微调，在医疗、金融等敏感领域具有重要应用价值，实现了数据可用性与合规性的平衡。
