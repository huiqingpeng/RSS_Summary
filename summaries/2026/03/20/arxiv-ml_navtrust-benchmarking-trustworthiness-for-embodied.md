---
title: "NavTrust: Benchmarking Trustworthiness for Embodied Navigation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19229"
published: "2026-03-20"
summarized: "2026-03-20T14:03:34.635385"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了NavTrust，首个统一评估具身导航智能体可信度的基准测试框架。该框架系统性地对RGB图像、深度图和自然语言指令等输入模态施加真实场景中的损坏（corruptions），以评估其对导航性能的影响。通过对七种最先进方法的广泛评估，研究发现现有方法在真实损坏条件下性能显著下降，暴露出严重的鲁棒性缺陷。此外，作者还评估了四种缓解策略，并在真实移动机器人上验证了改进效果。

【方法概述 / Method】
NavTrust构建了一个统一的损坏评估框架，涵盖RGB-Depth图像损坏（如噪声、模糊、遮挡等）和指令变体（如语义改写、指令截断等）两大类别。该基准在Vision-Language Navigation (VLN) 和 Object-Goal Navigation (OGN) 两种主流导航任务上进行测试，并采用Uni-NaVid和ETPNav作为基础模型进行系统性分析。

【实验结果 / Results】
实验表明，现有最先进方法在真实损坏条件下出现显著性能退化，揭示了关键鲁棒性缺口。四种缓解策略（包括数据增强、对抗训练等）有效提升了模型对RGB-Depth损坏和指令变体的鲁棒性。在真实移动机器人部署中，经过优化的模型展现出更强的抗损坏能力。

【应用价值 / Applications】
NavTrust为开发更可信的具身导航系统提供了标准化评估工具和明确的改进路线图，对服务机器人、自动驾驶、搜救机器人等需要在复杂真实环境中可靠运行的应用场景具有重要价值。该基准有助于推动从实验室理想条件向真实世界部署的可靠迁移。
