---
title: "SJD-PAC: Accelerating Speculative Jacobi Decoding via Proactive Drafting and Adaptive Continuation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18599"
published: "2026-03-20"
summarized: "2026-03-20T15:12:50.581090"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SJD-PAC，一种加速自回归文本到图像生成的增强型推测雅可比解码框架。针对视觉生成中高熵区域导致的草稿token接受率低这一瓶颈，该研究通过主动起草策略和自适应延续机制两大创新，显著提高了每步的平均接受长度。实验表明，SJD-PAC在标准文本到图像基准上实现了3.8倍加速，同时严格保持目标分布并确保图像质量无损。

【方法概述 / Method】
SJD-PAC包含两个核心组件：一是主动起草策略（proactive drafting），通过优化高熵复杂区域的局部接受率来提升草稿质量；二是自适应延续机制（adaptive continuation），在初始拒绝后继续序列验证而非完全重新采样。两种机制协同工作，突破了传统SJD遇到拒绝即中断的局限。

【实验结果 / Results】
在标准文本到图像基准测试中，SJD-PAC实现了3.8倍的推理加速，且严格保持了目标分布的无损特性。该方法通过显著提高每步的平均接受长度，有效克服了高熵区域带来的吞吐量瓶颈，在加速性能上取得了突破性进展。

【应用价值 / Applications】
该研究可直接应用于实时文本到图像生成系统，如AI绘画工具、交互式图像编辑平台和创意内容生产流水线，大幅降低推理延迟和计算成本。其无损加速特性特别适合对生成质量要求严格的商业应用场景，为大规模部署高效的自回归视觉生成模型提供了可行方案。
