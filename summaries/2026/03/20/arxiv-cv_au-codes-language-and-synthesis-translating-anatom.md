---
title: "AU Codes, Language, and Synthesis: Translating Anatomy to Text for Facial Behavior Synthesis"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18588"
published: "2026-03-20"
summarized: "2026-03-20T15:12:23.789153"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种将面部动作单元（AUs）转化为自然语言描述的新方法，用于解决面部行为合成中传统one-hot编码无法处理冲突AUs的问题。作者构建了首个大规模图文配对数据集BP4D-AUText，并开发了VQ-AUFace生成模型，实现了从文本描述生成高保真面部行为。实验表明，该方法在解剖学合理性、行为丰富性和感知真实性方面均显著优于现有方法，尤其在处理冲突AUs的复杂场景下表现突出。

【方法概述 / Method】

该研究采用基于规则的动态AU文本处理器（Dynamic AU Text Processor）将BP4D和BP4D+数据集中的AU标注转换为自然语言描述，构建了BP4D-AUText数据集。在此基础上，提出VQ-AUFace生成模型，利用面部结构先验知识，通过文本驱动的方式合成真实且多样化的面部行为，突破了传统线性组合AUs的局限性。

【实验结果 / Results】

大量定量实验和用户研究表明，该方法在面部行为合成任务上显著优于现有方法，能够有效生成解剖学合理、行为丰富且感知上令人信服的面部表情。特别是在涉及冲突AUs（即激活相同面部肌肉但产生相反动作的AUs）的挑战性条件下，该方法展现出卓越的性能，避免了传统方法产生的解剖学不合理伪影和不自然运动叠加问题。

【应用价值 / Applications】

该研究为数字人、虚拟角色动画、人机交互和情感计算等领域提供了更精细的面部行为控制工具。通过将解剖学基础的AU系统与自然语言相结合，该方法支持非专业人员以直观的方式描述复杂面部表情，有望推动影视制作、游戏开发、心理健康辅助诊断及社交机器人等应用场景的发展。
