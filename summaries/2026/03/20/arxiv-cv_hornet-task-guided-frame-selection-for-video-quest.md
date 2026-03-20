---
title: "HORNet: Task-Guided Frame Selection for Video Question Answering with Vision-Language Models"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18850"
published: "2026-03-20"
summarized: "2026-03-20T15:17:03.037951"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了HORNet，一种轻量级的视频帧选择策略，通过Group Relative Policy Optimization（GRPO）训练来学习冻结的视觉语言模型（VLM）回答问题时所需的关键帧。HORNet仅用不到100万可训练参数，即可将输入帧减少99%、VLM处理时间降低93%，同时在短视频问答基准（MSVD-QA）上提升1.7% F1分数，在时间推理任务（NExT-QA）上比均匀采样提升7.3分。研究还形式化了"Select Any Frames（SAF）"任务，将视觉输入策划与VLM推理解耦，并证明GRPO训练的选择策略比监督学习和PPO方法具有更好的分布外泛化能力。

【方法概述 / Method】
HORNet采用强化学习框架，以GRPO作为训练算法，直接优化帧选择策略以最大化VLM回答正确性。该方法将帧选择形式化为SAF任务，使轻量级选择器与冻结的VLM解耦，选择器仅根据任务目标（问题）和候选帧特征输出选择决策，无需访问VLM内部梯度。

【实验结果 / Results】
在涵盖341,877个问答对和114.2小时视频的六个基准测试上，HORNet实现了高达99%的帧压缩率和93%的VLM处理时间缩减。该策略可跨不同VLM答案器迁移而无需重新训练，与更强模型配对时额外获得8.5%的相对性能提升，且在分布外泛化方面优于监督学习和PPO替代方案。

【应用价值 / Applications】
HORNet为视频问答系统提供了一种实用的高效推理方案，特别适用于需要实时处理或计算资源受限的边缘设备场景。该方法通过优化"看什么"而非"如何生成"来提升VLM效率，可广泛应用于智能监控、视频内容分析、教育视频交互等需要长视频理解的领域，同时为视觉-语言模型的输入优化提供了可迁移的通用框架。
