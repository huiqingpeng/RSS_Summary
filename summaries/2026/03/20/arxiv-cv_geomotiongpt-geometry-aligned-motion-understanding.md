---
title: "GeoMotionGPT: Geometry-Aligned Motion Understanding with Large Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.07632"
published: "2026-03-20"
summarized: "2026-03-20T16:17:05.824428"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了GeoMotionGPT框架，旨在解决现有运动-语言模型中运动量化与语义嵌入学习脱节的问题。作者指出，传统方法仅通过token ID连接两个模态，无法有效对齐运动空间的内在几何结构与嵌入空间，从而限制了大型语言模型（LLM）的细粒度运动推理能力。为此，该研究创新性地在运动码本和LLM嵌入空间上显式施加正交约束，使两者的关系结构自然镜像，实验表明在HumanML3D和KIT-ML数据集上分别比最强基线提升22.4%和14.4%。

【方法概述 / Method】
该框架采用三阶段设计实现几何对齐：首先使用基于Gumbel-Softmax的解码器专用量化器进行可微分训练并实现码本的均衡使用；其次通过稀疏投影将运动码映射到LLM嵌入空间，同时保持正交性；最后采用两阶段正交正则化调度，在分词器训练和LLM微调阶段分别施加软约束，在维持几何对齐的同时不阻碍语义适应。

【实验结果 / Results】
在HumanML3D和KIT-ML两个标准运动理解数据集上，GeoMotionGPT在聚合平均指标上分别比最强基线提升22.4%和14.4%。消融实验验证了分词器设计、投影机制和正则化策略各组件的有效性，证明了几何显式对齐对运动-语言推理的关键作用。

【应用价值 / Applications】
该研究为人体运动理解与生成、机器人动作规划、虚拟现实交互等需要精确运动-语言对齐的领域提供了新的技术范式。通过使LLM能够"理解"运动的几何结构而非仅记忆token序列，该方法有望提升智能体在物理世界中的运动推理和指令跟随能力，推动具身智能的发展。
