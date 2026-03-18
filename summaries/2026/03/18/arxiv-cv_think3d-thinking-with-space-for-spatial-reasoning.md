---
title: "Think3D: Thinking with Space for Spatial Reasoning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.13029"
published: "2026-03-18"
summarized: "2026-03-18T18:32:20.098422"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了Think3D框架，旨在解决现有视觉语言模型（VLMs）在3D空间推理方面的局限性。通过集成3D操作工具，Think3D使VLM代理具备交互式的3D链式思维推理能力，将被动感知转化为主动空间探索。该框架作为零样本插件可显著提升闭源大模型（如GPT-4.1、Gemini 2.5 Pro）的性能，同时通过Think3D-RL强化学习方法使小型开源模型（如Qwen3-VL-4B）也能自主学习有效的空间探索策略，无需昂贵的人工标注。

【方法概述 / Method】

Think3D框架的核心是为VLM代理配备一系列3D操作工具（如旋转、缩放、视角切换等），使其能够主动操控和探索3D环境，而非仅被动接收2D图像输入。对于小型模型，作者进一步提出Think3D-RL，一种基于强化学习的训练范式，通过奖励机制自主学习最优的空间探索策略，避免了传统模仿学习对大量操作轨迹标注的依赖。

【实验结果 / Results】

在零样本设置下，Think3D为GPT-4.1和Gemini 2.5 Pro带来显著性能提升：在BLINK Multi-view和MindCube基准上绝对增益达+7.8%，在VSI-Bench上达+4.7%。对于Qwen3-VL-4B模型，Think3D-RL将原本微弱的+0.7%增益大幅提升至+10.7%，且学习到的探索策略在质量上可与大型模型的复杂行为相媲美。

【应用价值 / Applications】

Think3D为机器人导航、增强现实、自动驾驶等需要精确3D空间理解的领域提供了新的技术路径。其工具增强的主动探索范式可降低对大规模3D标注数据的依赖，使资源受限场景下的3D推理成为可能，同时该框架的即插即用特性便于快速集成到现有的多模态系统中。
