---
title: "TharuChat: Bootstrapping Large Language Models for a Low-Resource Language via Synthetic Data and Human Validation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17220"
published: "2026-03-19"
summarized: "2026-03-19T13:10:42.381910"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对全球南方低资源语言被排除在AI革命之外的问题，以尼泊尔和印度边境地区约170万人使用的塔鲁语（Tharu）为研究对象，开发了专门的指令遵循模型Tharu-LLaMA（3B）。研究构建了TharuChat数据集，通过LLM-to-Human引导流程，利用提示工程化的Gemini模型结合Rana Tharu语法和民间故事合成训练数据。实验表明，尽管数据存在方言混合和印地语残留等不完美之处，小规模合成数据仍能有效降低困惑度（从6.42降至2.88），为在消费级硬件上保护喜马拉雅地区低资源语言提供了概念验证。

【方法概述 / Method】
研究采用LLM-to-Human引导流程构建数据集：首先使用提示工程化的Gemini模型，输入Rana Tharu语法规则和民间故事内容生成合成数据，再通过人工验证确保质量。该数据集以Rana Tharu方言为主（约70%），同时整合Dangaura和Kochila方言元素，反映该地区语言的真实异质性。最终基于该数据集微调得到Tharu-LLaMA（3B）模型。

【实验结果 / Results】
通过严格的消融实验，研究发现合成数据规模与模型性能呈线性关系：将数据集从25%扩展至100%，困惑度从6.42持续下降至2.88。这一结果表明，即使存在方言代码混合和Awadhi/印地语残留等数据不完美性，小规模合成数据仍能显著提升低资源语言模型的性能。

【应用价值 / Applications】
该研究为保护和振兴全球南方濒危土著语言提供了可复现的技术路径，证明在消费级硬件上即可实现低资源语言的LLM开发。TharuChat可作为数字语言档案和教育工具，支持塔鲁语社区的文化传承；其方法论可推广至其他数据稀缺的喜马拉雅语言和全球低资源语言，助力缩小AI数字鸿沟。
