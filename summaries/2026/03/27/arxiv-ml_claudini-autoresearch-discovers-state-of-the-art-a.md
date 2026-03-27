---
title: "Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24511"
published: "2026-03-27"
summarized: "2026-03-28T07:10:58.149502"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文展示了基于Claude Code的"自主研究"（autoresearch）流程能够自动发现针对大语言模型的新型白盒对抗攻击算法。这些自动发现的算法在越狱攻击和提示注入评估中显著优于30多种现有方法，在CBRN查询上对GPT-OSS-Safeguard-20B的攻击成功率高达40%（现有算法≤10%），且在迁移到Meta-SecAlign-70B时达到100%攻击成功率。该研究为使用LLM智能体自动化增量式安全研究提供了早期实证。

【方法概述 / Method】
研究采用基于Claude Code的自主研究流程，从现有攻击实现（如GCG）出发，通过迭代优化自动生成新算法。该流程利用白盒对抗红队测试的密集量化反馈作为优化目标，使智能体能够持续改进攻击策略。

【实验结果 / Results】
发现的算法在GPT-OSS-Safeguard-20B的CBRN查询上实现40%攻击成功率，远超现有算法的≤10%；攻击在替代模型上优化后直接迁移到 held-out 模型，对Meta-SecAlign-70B达到100%攻击成功率，而最佳基线仅56%。

【应用价值 / Applications】
该研究为自动化AI安全研究提供了可行范式，可加速对抗攻击和防御方法的发现周期；同时揭示的强迁移攻击能力对LLM安全对齐评估具有重要警示意义，有助于推动更鲁棒的安全防护机制开发。研究团队已开源所有发现的攻击、基线实现及评估代码。
