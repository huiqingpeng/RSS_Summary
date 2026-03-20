---
title: "Sharpness-Aware Minimization in Logit Space Efficiently Enhances Direct Preference Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18258"
published: "2026-03-20"
summarized: "2026-03-20T12:09:38.460768"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了直接偏好优化（DPO）中存在的"挤压效应"（squeezing effect），即训练过程中偏好响应的概率意外下降的现象。作者建立了logit空间中的坐标动态理论框架，揭示了负梯度更新导致残差在高曲率方向快速膨胀是挤压效应的根本原因，而Sharpness-Aware Minimization（SAM）可通过曲率正则化效应抑制该行为。基于此，作者提出了仅扰动输出层的高效变体logits-SAM，在多个模型和数据集上验证了其对DPO效果的稳定提升。

【方法概述 / Method】
本文通过理论分析建模DPO在logit空间的坐标动态，识别出高曲率方向残差膨胀与挤压效应的关联。进而提出logits-SAM方法，将SAM的扰动机制限制在输出层logits上，避免了标准SAM带来的巨大计算开销，实现了与DPO的无缝集成。

【实验结果 / Results】
实验在Pythia-2.8B、Mistral-7B和Gemma-2B-IT模型上，使用多个数据集和基准测试进行验证。结果表明logits-SAM能持续增强DPO的效果，且计算开销可忽略不计，同时可与其他DPO变体（如IPO、KTO等）有效结合。

【应用价值 / Applications】
该研究为大语言模型的人类偏好对齐提供了更稳定高效的训练方案，logits-SAM的低计算成本特性使其易于在实际生产环境中部署。研究成果可广泛应用于对话系统、内容生成等需要高质量偏好对齐的场景，提升模型输出的人类偏好符合度。
