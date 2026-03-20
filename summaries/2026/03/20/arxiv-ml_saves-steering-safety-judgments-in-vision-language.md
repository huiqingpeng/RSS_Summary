---
title: "SAVeS: Steering Safety Judgments in Vision-Language Models via Semantic Cues"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19092"
published: "2026-03-20"
summarized: "2026-03-20T13:19:59.437542"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了视觉-语言模型（VLMs）在多模态安全决策中的行为机制，发现其安全判断高度依赖于语义线索而非基于视觉内容的真正理解。作者提出了一个语义引导框架，通过文本、视觉和认知干预来控制VLMs的安全行为，并构建了SAVeS基准测试来评估情境安全性。实验表明，安全决策对语义线索极为敏感，且自动化引导流程可利用这一机制，揭示了多模态安全系统的潜在漏洞。

【方法概述 / Method】
作者设计了一个语义引导框架，在不改变底层场景内容的前提下，对VLMs施加受控的文本、视觉和认知干预。同时提出了SAVeS（Situational Safety under Semantic cues）基准测试及评估协议，将行为拒绝、基于 grounded 的安全推理和错误拒绝三者分离，以精确衡量语义线索对安全判断的影响。

【实验结果 / Results】
实验在多个VLMs及额外最先进的基准测试上进行，结果显示安全决策对语义线索高度敏感，表明模型依赖习得的视觉-语言关联而非真正的视觉理解。研究进一步证明，自动化引导管道可以有效利用这些机制来操控模型的安全判断，凸显了现有系统的脆弱性。

【应用价值 / Applications】
该研究对部署VLMs的真实世界和具身应用场景（如自动驾驶、机器人决策）具有重要警示意义，揭示了当前多模态安全系统可能被恶意语义操控的风险。研究成果可用于开发更鲁棒的安全对齐机制，帮助设计能够抵御语义攻击的VLM系统，提升AI安全性的可靠性。
