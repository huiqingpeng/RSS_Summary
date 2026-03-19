---
title: "Shielded Reinforcement Learning Under Dynamic Temporal Logic Constraints"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17152"
published: "2026-03-19"
summarized: "2026-03-19T13:09:37.296306"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种将序列控制障碍函数（Sequential Control Barrier Functions）与无模型强化学习（RL）相结合的框架，用于在强化学习过程中强制执行信号时序逻辑（STL）任务。该方法突破了传统安全约束的局限，能够处理包含动态目标追踪的复杂时空规范，确保智能体在整个学习过程中满足给定的时序逻辑约束。通过仿真实验验证了该框架在处理具有未知轨迹的动态目标时的有效性。

【方法概述 / Method】
该方法核心是将STL规范的鲁棒度（robustness）转化为控制障碍函数（CBF）约束，构建序列化的安全滤波器（shield）来干预RL策略，防止违反时序逻辑规范的行为。框架采用模型无关的强化学习作为基础策略，通过在线求解二次规划（QP）问题，在保证STL满足的前提下最大化学习回报。

【实验结果 / Results】
论文通过多种仿真场景验证了框架的有效性，包括需要周期性充电、限时访问特定区域等复杂STL任务。实验表明该方法能够在学习过程中持续满足动态时序约束，同时保持良好的任务完成性能和学习效率，相比无保护机制的标准RL显著降低了规范违反率。

【应用价值 / Applications】
该研究可直接应用于移动机器人、自主无人机等需要执行复杂时空任务的物理系统，特别适用于物流仓储中的周期性巡检、应急救援中的限时目标搜索等场景。框架为安全强化学习在真实机器人部署提供了理论保障，有助于推动RL从仿真走向实际工业应用。
