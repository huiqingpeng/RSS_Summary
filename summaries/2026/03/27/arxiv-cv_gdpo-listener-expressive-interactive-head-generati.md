---
title: "GDPO-Listener: Expressive Interactive Head Generation via Auto-Regressive Flow Matching and Group reward-Decoupled Policy Optimization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.25020"
published: "2026-03-27"
summarized: "2026-03-28T07:20:37.477298"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了GDPO-Listener框架，用于生成高表现力的对话式3D头部运动（包括说话者和倾听者）。该框架通过自回归流匹配架构实现稳定的监督学习，并引入组奖励解耦策略优化（GDPO）来解决倾听者运动中的"回归均值"问题（即运动趋于静态）。此外，该方法还支持基于语义文本的显式可控响应生成，在Seamless Interaction和DualTalk数据集上取得了优于现有基线的性能。

【方法概述 / Method】
论文采用自回归流匹配（Auto-Regressive Flow Matching）架构作为基础生成模型，确保训练稳定性。针对倾听者运动缺乏表现力的问题，提出GDPO强化学习方法，通过对不同FLAME参数组（如表情、头部姿态等）进行隔离的奖励归一化，显式激励高方差的表现力生成。同时引入语义文本控制机制，实现对非语言响应的定制化。

【实验结果 / Results】
在Seamless Interaction和DualTalk数据集上的大量评估表明，GDPO-Listener在长期运动方差、视觉表现力和语义可控性三个维度上均优于现有基线方法。GDPO有效缓解了倾听者运动趋于静态的问题，生成了更具表现力的复杂非语言动作。

【应用价值 / Applications】
该研究适用于虚拟人合成、实时交互式数字人、远程会议系统等场景，能够生成自然且富有表现力的双向对话头部动画。语义可控特性使其可用于可定制的虚拟助手、游戏角色动画及社交机器人，提升人机交互的真实感和沉浸感。
