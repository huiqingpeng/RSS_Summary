---
title: "FEEL (Force-Enhanced Egocentric Learning): A Dataset for Physical Action Understanding"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15847"
published: "2026-03-18"
summarized: "2026-03-18T16:08:12.935748"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了FEEL（Force-Enhanced Egocentric Learning），首个大规模结合自定义压阻式手套采集的力测量数据与第一人称视角视频的公开数据集。FEEL包含约300万帧力同步的自然无脚本厨房操作视频，其中45%的帧涉及手-物体接触。作者证明力信息是物理交互的关键基础要素，并通过两项任务验证其价值：时序接触分割与像素级接触物体分割的联合任务，以及以力预测为自监督预训练目标的动作表征学习，在多个基准数据集上取得最先进的接触分割结果和优异的动作理解迁移性能。

【方法概述 / Method】

研究团队开发了可扩展采集的压阻式智能手套，能够同步记录手部施力数据与第一人称视角视频，构建了大规模力-视觉配对数据集。该方法将力测量作为物理交互的核心信号，用于监督接触检测任务，并设计力预测作为自监督预训练目标，无需人工标注即可学习鲁棒的动作表征。

【实验结果 / Results】

在时序接触分割任务上，基于FEEL的方法达到当前最优性能；在像素级接触物体分割任务上取得有竞争力的结果，且无需人工接触物体标注。此外，以力预测为预训练目标在EPIC-Kitchens、Something-Something-V2、EgoExo4D和Meccano等多个动作理解基准上，显著提升了无标签迁移学习的性能。

【应用价值 / Applications】

该研究为机器人操作学习、人机交互和增强现实等领域提供了重要的多模态数据资源，力-视觉融合感知可赋能机器人精细抓取、物理推理和交互式任务学习。自监督力预测预训练方法降低了对大规模人工标注的依赖，为 egocentric 视频理解和具身智能研究开辟了新的技术路径。
