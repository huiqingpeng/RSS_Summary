---
title: "ADAPT: Attention Driven Adaptive Prompt Scheduling and InTerpolating Orthogonal Complements for Rare Concepts Generation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19157"
published: "2026-03-20"
summarized: "2026-03-20T16:05:00.036562"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ADAPT框架，一个无需训练的方法，用于解决文本到图像扩散模型中罕见组合概念生成的挑战。该方法通过注意力分数和正交分量，确定性地规划语义对齐的提示调度，为罕见概念的组合提供一致的引导。实验表明，ADAPT在RareBench基准测试中显著提升了罕见概念的生成性能，实现了确定性和精确的控制，同时不损害视觉质量。

【方法概述 / Method】
ADAPT采用注意力驱动的自适应提示调度策略，利用扩散模型去噪过程中的注意力分数来指导提示切换的时机和内容。该方法通过插值正交补空间（orthogonal complements）来保持语义对齐，避免随机语言模型带来的方差问题，实现确定性的生成控制。

【实验结果 / Results】
ADAPT在RareBench基准测试中取得了优异性能，显著提升了罕见组合概念的生成质量。实验表明该方法能准确反映罕见属性的语义信息，与现有方法（如R2F）相比，提供了更确定性和精确的生成控制，且无需额外的训练或微调。

【应用价值 / Applications】
该研究适用于需要精确控制罕见概念组合的场景，如创意设计、广告生成和个性化内容创作。ADAPT的确定性特性使其特别适合需要可重复结果的商业应用，同时其无需训练的特性降低了部署成本，便于集成到现有的文本到图像生成系统中。
