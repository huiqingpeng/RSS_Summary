---
title: "MagicWorld: Towards Long-Horizon Stability for Interactive Video World Exploration"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2511.18886"
published: "2026-03-19"
summarized: "2026-03-19T16:28:20.507686"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MagicWorld，一种基于自回归框架的交互式视频世界模型，旨在解决现有方法在复杂多主体环境中存在的运动漂移问题，以及长程交互中的误差累积问题。论文设计了流引导运动保持约束、历史缓存检索策略和增强型交互训练策略三种核心技术，并构建了RealWM120K真实世界数据集。实验结果表明，MagicWorld显著提升了运动真实感并有效缓解了长程交互中的误差累积。

【方法概述 / Method】
MagicWorld采用自回归生成框架，通过三种关键机制实现稳定的长程交互：首先，引入流引导运动保持约束（flow-guided motion preservation constraint），利用光流信息约束动态主体的运动模式；其次，设计历史缓存检索策略，在生成长序列时主动检索并强化历史场景状态；最后，采用多镜头聚合蒸馏与双奖励加权的增强交互训练策略，提升模型的长期稳定性。

【实验结果 / Results】
论文在自建RealWM120K数据集及多个基准上进行评估，结果显示MagicWorld在运动真实性和长程一致性方面显著优于现有方法。具体而言，流引导约束有效减少了复杂场景中动态主体的运动漂移，而历史缓存与增强训练策略的组合使模型在长程交互中保持了更好的结构一致性和语义连贯性，误差累积问题得到明显缓解。

【应用价值 / Applications】
该研究可广泛应用于交互式虚拟环境探索、游戏世界模拟、机器人策略学习的数据生成，以及沉浸式虚拟现实体验等场景。MagicWorld的长程稳定性使其特别适合需要持续多步交互的应用，如开放式世界游戏AI、自动驾驶仿真训练和可交互的数字孪生系统，为构建可靠的交互式视频世界模型提供了重要技术基础。
