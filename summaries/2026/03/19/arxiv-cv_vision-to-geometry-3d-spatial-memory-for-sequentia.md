---
title: "Vision to Geometry: 3D Spatial Memory for Sequential Embodied MLLM Reasoning and Exploration"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.02458"
published: "2026-03-19"
summarized: "2026-03-19T16:29:16.973465"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了具身智能体在序列任务中的核心挑战：如何复用先前探索积累的空间知识来指导后续推理与探索。作者提出了3DSPMR框架，利用视野（FoV）覆盖作为显式几何先验来增强智能体的记忆、推理和探索能力。同时引入了SEER-Bench基准测试，涵盖可行与不可行任务，用于全面评估序列具身问答（EQA）和多模态导航（EMN）任务。实验表明3DSPMR在两项序列任务上均取得显著性能提升。

【方法概述 / Method】

3DSPMR框架通过将视野覆盖建模为显式几何约束，构建3D空间记忆以支持序列推理。该方法将多模态大语言模型（MLLM）与几何先验相结合，使智能体能够基于历史探索的FoV覆盖信息，进行高效的空间推理和主动探索决策。

【实验结果 / Results】

在SEER-Bench基准上，3DSPMR在序列具身问答（EQA）和具身多模态导航（EMN）任务中均实现了大幅性能提升。实验验证了FoV覆盖作为几何先验能有效增强智能体对空间环境的记忆与推理能力，特别是在处理包含不可行目标（如搜索不存在物体）的复杂序列任务时表现突出。

【应用价值 / Applications】

该研究适用于家庭服务机器人、智能导览系统等需要在动态未知环境中连续执行多项任务的具身智能应用。通过建立可复用的3D空间记忆，智能体能够避免重复探索、高效处理用户连续指令，提升人机协作效率，对实际部署的具身AI系统具有重要价值。
