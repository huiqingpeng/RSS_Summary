---
title: "Towards the Vision-Sound-Language-Action Paradigm: The HEAR Framework for Sound-Centric Manipulation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16086"
published: "2026-03-18"
summarized: "2026-03-18T18:23:12.718359"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Vision-Sound-Language-Action (VSLA)范式，将声音作为实时控制信号而非静态提示，以解决现有VLA模型在声音中心操作中因开环执行导致的"盲执行间隔"问题。作者设计了HEAR框架，包含流式音频历史模块、多感官推理模块、音频世界模型和流匹配策略四个组件。实验表明，因果持续性建模和显式时间学习对鲁棒的声音中心操作至关重要，该工作为具身智能体的多感官基础模型提供了实用路径。

【方法概述 / Method】
HEAR框架由四个核心组件构成：Historizer通过流式处理在动作执行间隙维持紧凑的因果音频上下文；Envisioner基于全模态基础模型实现视觉-语言-音频-本体感觉的多感官推理；Advancer作为音频世界模型，通过预测未来音频码学习时间动态；Realizer采用流匹配策略生成平滑的动作块。该框架专门针对延迟决策循环下的连续控制进行优化。

【实验结果 / Results】
为支持VSLA研究，作者构建了预训练数据集OpenX-Sound和首个具有严格因果时序规则的声音中心操作基准HEAR-Bench。实验验证了HEAR在需要实时声音反馈的精细操作任务中的有效性，证明因果音频持久化和显式时间动态学习显著提升了系统在动态声学环境中的操作鲁棒性。

【应用价值 / Applications】
该研究适用于需要精细听觉反馈的机器人操作场景，如易碎物品抓取（通过碰撞声判断接触状态）、液体倾倒（通过声音判断液位）、工具使用（通过声学反馈调整力度）等动态交互任务。HEAR框架使机器人能够在视觉受限或需要多模态验证的环境中实现更可靠的操作，为家庭服务机器人、工业装配和医疗辅助机器人等应用提供了技术基础。
