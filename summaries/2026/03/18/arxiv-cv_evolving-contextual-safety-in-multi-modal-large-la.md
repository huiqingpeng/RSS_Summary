---
title: "Evolving Contextual Safety in Multi-Modal Large Language Models via Inference-Time Self-Reflective Memory"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.15800"
published: "2026-03-18"
summarized: "2026-03-18T17:18:34.552854"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对多模态大语言模型（MLLMs）的安全性问题，提出上下文安全（contextual safety）这一关键挑战——即模型需要区分表面相似但安全意图截然不同的场景。作者构建了MM-SafetyBench++基准测试，通过最小修改构造安全/不安全对照样本，并设计了无需训练的EchoSafe框架，利用自反思记忆库存储和检索安全经验，实现了推理时的上下文感知安全推理与持续进化。

【方法概述 / Method】
EchoSafe采用训练自由的推理时框架，核心机制是维护一个自反思记忆库（self-reflective memory bank），用于积累历史交互中的安全洞察；在推理阶段，系统检索相关过往经验并整合到当前提示中，引导模型进行上下文感知的安全决策，实现安全行为的动态演化。

【实验结果 / Results】
在多个多模态安全基准测试上的广泛实验表明，EchoSafe一致性地取得了优越性能，显著提升了模型对上下文细微差异的区分能力；该框架无需额外训练即可有效增强现有MLLMs的上下文安全性，为相关研究建立了强有力的基线。

【应用价值 / Applications】
该研究对部署MLLMs的实际应用具有重要价值，如内容审核、智能助手、教育辅导等场景，可避免模型因缺乏上下文理解而过度拒绝合法请求或误放过危险内容；EchoSafe的训练自由特性使其能够快速集成到现有系统中，为构建更可靠、更自适应的安全防护机制提供实用解决方案。
