---
title: "Generative Adversarial Perturbations with Cross-paradigm Transferability on Localized Crowd Counting"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24821"
published: "2026-03-27"
summarized: "2026-03-28T07:17:20.406916"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种新型对抗攻击框架，首次实现了对人群计数领域两种主流范式（密度图估计和点回归）的跨范式攻击。通过多任务损失优化，该框架在保持视觉隐蔽性的同时，显著提升了对抗扰动的迁移能力，平均使7个SOTA模型的绝对误差提升7倍，迁移率可达0.55至1.69。

【方法概述 / Method】
该框架采用多任务损失优化策略：针对点回归模型，使用场景密度特定的高置信度logit抑制；针对密度图模型，采用峰值目标密度图抑制；同时结合模型无关的感知约束确保扰动的隐蔽性。两种攻击目标通过统一优化实现协同作用。

【实验结果 / Results】
实验表明，该攻击在保持竞争性视觉质量的同时，平均使Mean Absolute Error提升7倍；在7个SOTA人群计数模型上实现了0.55至1.69的迁移率，在攻击有效性与不可感知性之间取得了优于现有迁移攻击策略的平衡。

【应用价值 / Applications】
该研究揭示了人群计数系统在跨范式场景下的安全漏洞，为安防监控等关键应用领域提供了鲁棒性评估基准；所提方法可用于AI系统的对抗训练与防御加固，同时也警示了物理世界人群分析系统面临的潜在对抗风险。
