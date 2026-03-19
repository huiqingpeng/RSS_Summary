---
title: "HeiSD: Hybrid Speculative Decoding for Embodied Vision-Language-Action Models with Kinematic Awareness"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17573"
published: "2026-03-19"
summarized: "2026-03-19T13:14:02.215007"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对具身视觉-语言-动作（VLA）模型推理速度慢的问题，提出了一种混合推测解码框架HeiSD。作者通过分析机器人轨迹模式发现，基于草稿模型的推测解码（drafter-based SD）和基于检索的推测解码（retrieval-based SD）应混合使用而非单独应用。HeiSD通过引入验证-跳过机制和序列级宽松接受策略优化检索式SD，并提出基于运动学的融合指标来自动确定两种SD的混合边界，实现了最高2.45倍的加速比，同时保持高任务成功率。

【方法概述 / Method】
HeiSD框架包含两个核心组件：一是针对检索式SD的优化方法，包括验证-跳过机制（verify-skip）和序列级宽松接受策略（sequence-wise relaxed acceptance），以解决草稿拒收和持续误差问题；二是基于运动学的融合指标（kinematic-based fused metric），利用机器人运动学特征自动划分drafter-based SD和retrieval-based SD的适用边界，实现动态混合调度。

【实验结果 / Results】
在仿真基准测试中，HeiSD实现了最高2.45倍的加速；在真实机器人场景中，加速比达到2.06倍至2.41倍。更重要的是，该框架在显著提升推理速度的同时，维持了较高的任务成功率，证明了混合策略在效率与准确性之间的有效平衡。

【应用价值 / Applications】
该研究可直接应用于需要实时响应的机器人控制场景，如家庭服务机器人、工业协作机械臂和自动驾驶系统等，解决VLA模型部署时的延迟瓶颈。HeiSD的混合设计思想和运动学感知机制也为其他具身智能模型的加速优化提供了可迁移的技术范式。
