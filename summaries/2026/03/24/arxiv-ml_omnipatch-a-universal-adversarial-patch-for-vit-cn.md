---
title: "OmniPatch: A Universal Adversarial Patch for ViT-CNN Cross-Architecture Transfer in Semantic Segmentation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20777"
published: "2026-03-24"
summarized: "2026-03-25T07:14:04.188638"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了OmniPatch，一种用于学习通用对抗性补丁的训练框架，该补丁能够在无需访问目标模型参数的情况下，跨图像以及Vision Transformer（ViT）和CNN两种架构进行泛化。现有方法要么生成图像级扰动，要么针对单一架构优化补丁，限制了其实用性和可迁移性，而OmniPatch解决了这一局限性。该研究对自动驾驶等安全关键场景中的语义分割模型鲁棒性具有重要意义。

【方法概述 / Method】
OmniPatch采用训练框架来学习通用对抗性补丁，通过优化使补丁能够同时攻击ViT和CNN架构的语义分割模型。该方法不依赖目标模型的权重信息，实现了黑盒攻击场景下的跨架构迁移能力。

【实验结果 / Results】
（注：论文摘要中未提供具体实验结果和性能指标，需查看完整论文内容才能总结。）

【应用价值 / Applications】
OmniPatch可用于评估自动驾驶系统中语义分割模型的安全性，帮助开发者识别和修复模型漏洞。该研究对提升安全关键AI系统的鲁棒性具有重要价值，同时也为对抗性防御研究提供了新的测试基准。

---

**备注**：您提供的论文内容仅包含摘要部分，缺少方法细节、实验设置和结果数据。如需完整的笔记分析，建议提供论文的完整PDF或更多章节内容。
