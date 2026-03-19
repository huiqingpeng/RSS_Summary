---
title: "Echo Planning for Autonomous Driving: From Current Observations to Future Trajectories and Back"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2505.18945"
published: "2026-03-19"
summarized: "2026-03-19T16:24:29.205641"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Echo Planning（EchoP），一种用于端到端自动驾驶的新型自校正框架，通过建立Current-Future-Current（CFC）循环来解决现有规划器缺乏时间一致性的问题。核心洞见是合理的未来轨迹应具有双向一致性：既能从当前观测生成，也能反向重建当前状态。该框架无需额外监督，通过循环损失强制原始BEV表征与重建BEV表征的一致性，从而内在地惩罚物理不可信或不对齐的轨迹。实验表明，该方法在nuScenes上降低了L2误差和碰撞率，并在Bench2Drive闭环评估中达到26.54%的成功率。

【方法概述 / Method】
EchoP采用Bird's-Eye-View（BEV）场景表征作为中间表示，首先基于当前BEV预测未来轨迹，然后将这些轨迹逆映射回当前BEV状态以完成重建。通过设计循环一致性损失（cycle loss）约束原始BEV与重建BEV之间的差异，使CFC机制成为无需额外标注的归纳偏置，稳定长时程规划。

【实验结果 / Results】
在nuScenes开环评估中，EchoP相比单次规划器将平均L2误差降低0.04米，碰撞率降低0.12%；在Bench2Drive闭环基准测试中取得26.54%的成功率。这些改进验证了CFC循环机制在提升轨迹预测物理合理性和时间一致性方面的有效性。

【应用价值 / Applications】
EchoP为安全关键型自动驾驶系统提供了一种简单且可部署的可靠性提升路径，其自监督特性避免了昂贵的额外标注成本。该方法可无缝集成至现有端到端自动驾驶架构中，特别适用于需要长时程稳定规划的高速公路巡航、城市复杂交互等场景，有助于减少早期预测误差的累积效应。
