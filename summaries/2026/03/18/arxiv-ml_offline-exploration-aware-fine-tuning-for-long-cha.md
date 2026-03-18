---
title: "Offline Exploration-Aware Fine-Tuning for Long-Chain Mathematical Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16206"
published: "2026-03-18"
summarized: "2026-03-18T15:42:08.151601"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了离线探索感知微调（OXA）方法，旨在改进强化学习可验证奖励（RLVR）前的监督微调（SFT）阶段。OXA通过优化两个目标：提升低置信度的验证教师蒸馏数据以学习未捕获的推理模式，同时抑制高置信度的错误自蒸馏数据以重新分配概率质量。在6个基准测试上的实验表明，OXA能显著提升数学推理性能，特别是在Qwen2.5-1.5B-Math上相比传统SFT平均提升+6 Pass@1和+5 Pass@k点，且性能增益在后续RLVR训练中持续保持。

【方法概述 / Method】
OXA采用双目标优化策略：首先识别并提升模型低置信度但经验证正确的教师蒸馏数据，帮助模型内化先前未学习到的推理模式；其次识别并抑制高置信度但实际错误的自蒸馏数据，将概率质量从错误模式重新分配到潜在正确的候选答案上。该方法通过离线方式在SFT阶段主动塑造模型的探索空间。

【实验结果 / Results】
在6个数学推理基准上的实验显示，OXA相比传统SFT在Qwen2.5-1.5B-Math上取得平均+6 Pass@1和+5 Pass@k的显著提升。关键发现是OXA提高了初始策略的熵值，且这一性能优势在后续的RLVR训练中持续存在，表明探索感知的初始化具有长期价值。

【应用价值 / Applications】
OXA可广泛应用于需要长链数学推理的大语言模型训练流程，特别是在资源受限无法大规模运行在线RLVR的场景下，通过改进SFT初始化质量来提升最终性能。该方法为教育AI、自动定理证明和科学计算等领域的推理模型训练提供了更高效的预训练策略，减少了对昂贵在线探索的依赖。
