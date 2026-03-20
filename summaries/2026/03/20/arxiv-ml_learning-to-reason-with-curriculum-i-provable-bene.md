---
title: "Learning to Reason with Curriculum I: Provable Benefits of Autocurriculum"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18325"
published: "2026-03-20"
summarized: "2026-03-20T12:10:29.525883"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了自课程学习（autocurriculum）在推理模型训练中的理论优势。作者证明，通过让模型根据自身表现自适应地选择训练样本，可以显著降低监督微调（SFT）和强化学习（RL）的训练成本。具体而言，自课程学习在SFT中能将所需的推理示范数量从指数级减少到线性级，在RL中则能将计算成本与参考模型质量解耦，使其仅成为与目标精度无关的启动成本。

【方法概述 / Method】
该研究采用理论分析方法，借鉴了集成学习（boosting）和从反例中学习（learning from counterexamples）的经典技术，为自课程学习建立了严格的理论保证。核心机制是让模型自适应地识别并聚焦于当前表现较差的困难样本，而非均匀采样或使用固定分布。

【实验结果 / Results】
对于监督微调，自课程学习相比非自适应微调需要指数级更少的推理演示（demonstrations），因为它将教师监督集中在当前模型 struggling 的提示上。对于强化学习微调，自课程学习将计算成本与参考模型质量解耦，后者仅成为几乎与目标精度无关的启动成本（burn-in cost）。这些改进纯粹来自自适应数据选择，无需对提示的分布或难度做任何假设。

【应用价值 / Applications】
该研究为降低大语言模型推理能力的训练成本提供了理论指导，可应用于需要大量思维链数据的高效模型训练场景。自课程学习机制可整合到现有的SFT和RL训练流程中，帮助研究者和工程师在数据收集和计算资源受限的情况下训练更强的推理模型，具有降低AI开发门槛的潜在价值。
