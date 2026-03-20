---
title: "DriveVLM-RL: Neuroscience-Inspired Reinforcement Learning with Vision-Language Models for Safe and Deployable Autonomous Driving"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18315"
published: "2026-03-20"
summarized: "2026-03-20T16:08:07.952096"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了DriveVLM-RL，一种受神经科学启发的强化学习框架，通过双通路架构将视觉语言模型（VLM）整合到自动驾驶中，以解决传统RL方法依赖人工设计奖励或稀疏碰撞信号、以及VLM高延迟和幻觉问题。该框架在离线训练时使用VLM学习语义奖励，部署时移除VLM组件以确保实时可行性。在CARLA模拟器中的实验表明，该方法在碰撞避免、任务成功率和跨场景泛化方面均有显著提升，即使在无显式碰撞惩罚的设置下也表现出强鲁棒性。

【方法概述 / Method】
DriveVLM-RL采用双通路架构：静态通路使用基于CLIP的对比语言目标进行连续空间安全评估，动态通路利用轻量检测器和大型VLM进行注意力门控的多帧语义风险推理。通过分层奖励合成机制融合语义信号与车辆状态，并采用异步训练管道将昂贵的VLM推理与环境交互解耦。

【实验结果 / Results】
在CARLA模拟器的实验中，DriveVLM-RL在碰撞避免、任务成功率方面取得显著改进，并在多样化交通场景中展现出良好的泛化能力。特别地，该方法在无显式碰撞惩罚的设定下仍保持强鲁棒性，验证了语义奖励学习的有效性。

【应用价值 / Applications】
该研究为将基础模型（如VLM）集成到自动驾驶系统提供了实用范式，在确保实时部署可行性的同时提升安全性。其"离线训练-在线部署"的解耦思路可推广至其他需要高计算成本语义理解但要求低延迟决策的机器人应用场景。
