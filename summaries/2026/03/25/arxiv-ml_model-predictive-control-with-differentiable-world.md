---
title: "Model Predictive Control with Differentiable World Models for Offline Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22430"
published: "2026-03-25"
summarized: "2026-03-26T07:14:40.590123"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种用于离线强化学习的推理时自适应框架，该框架结合了模型预测控制（MPC）与可微分世界模型（DWM）。与现有方法仅在训练阶段使用学习到的动力学模型或在推理时采样候选计划不同，本方法能够在推理时通过想象轨迹的端到端梯度计算来实时优化策略参数。在D4RL连续控制基准测试（MuJoCo locomotion任务和AntMaze）上的评估表明，利用推理时信息优化策略参数能够持续优于强离线强化学习基线方法。

【方法概述 / Method】
该方法构建了一个可微分世界模型（DWM）管道，将预训练策略与学习到的状态转移和奖励模型相结合。核心创新在于实现了想象轨迹rollout的端到端可微分计算，使得模型预测控制能够在推理阶段通过梯度下降实时优化策略参数，而非固定使用离线训练得到的策略。

【实验结果 / Results】
算法在D4RL基准测试的MuJoCo locomotion任务和AntMaze环境中进行了评估。实验结果表明，该方法通过利用推理时信息动态优化策略参数，相比现有强离线强化学习基线方法取得了稳定且一致的性能提升。

【应用价值 / Applications】
该研究适用于机器人控制、自主导航等需要离线学习但部署时环境动态可能变化的场景。推理时自适应能力使策略能够根据当前状态实时调整，提高了离线训练策略在实际部署中的鲁棒性和适应性，同时避免了昂贵的在线环境交互成本。
