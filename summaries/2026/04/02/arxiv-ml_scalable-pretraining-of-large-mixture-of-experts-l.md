---
title: "Scalable Pretraining of Large Mixture of Experts Language Models on Aurora Super Computer"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00785"
published: "2026-04-02"
summarized: "2026-04-03T07:24:54.881416"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文展示了在Aurora超级计算机上进行大规模语言模型预训练的研究，该系统拥有127,488个Intel PVC GPU tiles。研究团队开发了Optimus训练库，成功在数千个GPU tiles上完成了从10亿参数密集模型到2200亿参数MoE模型的系列预训练，最大规模达到12,288个GPU tiles并保持约90%的扩展效率，同时通过定制GPU内核和EP-Aware分片优化器实现了最高1.71倍的训练加速。

【方法概述 / Method】
作者开发了名为Optimus的内部训练库，支持标准大模型训练技术，包括针对MoE模型的专家计算定制GPU内核，以及一种新颖的EP-Aware（Expert Parallelism-Aware）分片优化器；此外还集成了完善的可靠性和容错机制以保障大规模训练的稳定性。

【实验结果 / Results】
研究团队在3072个GPU tiles上完成了Mula-1B（10亿密集参数）和Mula-7B-A1B（70亿MoE）模型的完整4万亿token预训练，并完成了Mula-20B-A2B、Mula-100B-A7B和Mula-220B-A10B三个大型MoE模型各1000亿token的预训练；在Mula-220B-A10B上从384扩展到12,288个GPU tiles时达到了约90%的扩展效率，训练速度提升最高达1.71倍。

【应用价值 / Applications】
该研究为在ExaScale级超级计算机上进行高效、可扩展的LLM预训练提供了实践范例和技术方案，特别是针对MoE架构的优化方法可广泛应用于未来更大规模模型的训练；Optimus库及其可靠性特性对需要长期稳定运行的大规模AI训练任务具有重要参考价值，有助于降低大规模预训练的计算成本和时间开销。
