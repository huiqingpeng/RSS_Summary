---
title: "Jackknife ARAIM: Efficient GNSS Integrity Monitoring for Simultaneous Faults under Non-Gaussian Errors"
source: "arXiv Information Theory"
url: "https://arxiv.org/abs/2507.04284"
published: "2026-03-18"
summarized: "2026-03-18T19:10:34.031686"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种扩展的Jackknife检测器，能够在非高斯名义误差条件下检测多个同时发生的故障，并基于此开发了Jackknife ARAIM完整性监测算法。该方法在理论上被证明与解分离（SS）ARAIM具有等效的监测性能，但在单故障非高斯误差场景下计算效率显著更高，多故障场景下则保持与SS ARAIM相近的效率。全球仿真验证表明，该方法在单GPS星座下可将99.5%垂直保护等级（VPL）降至45米以下，在GPS-Galileo双星座下VPL保持在40米以下，显著优于基于高斯模型的传统ARAIM算法。

【方法概述 / Method】
该研究通过系统利用Jackknife检测器在测距域的特性，构建了Jackknife ARAIM完整性监测算法框架。核心方法包括：扩展Jackknife检测器以处理多故障并发情况，以及在非高斯误差条件下建立等效于解分离方法的监测统计量，同时避免高斯过界保守性带来的性能损失。

【实验结果 / Results】
基于真实实验数据模拟非高斯名义误差的全球仿真显示：单GPS星座下，Jackknife ARAIM将99.5% VPL降至45米以下，优于高斯ARAIM的50米；GPS-Galileo双星座下，高斯ARAIM因Galileo重尾误差导致VPL膨胀超过60米，而该方法维持VPL低于40米，对35米垂直告警限实现92%以上正常运行率。计算效率方面，单星座场景下中位处理时间较SS ARAIM降低59.4%。

【应用价值 / Applications】
该研究为航空精密进近、无人机导航等对完整性要求严苛的应用提供了更高效的GNSS监测方案，特别是在多星座融合导航中能有效应对非高斯误差导致的保护等级膨胀问题。方法可提升GNSS在垂直引导进近（LPV）等操作中的可用性，降低因保守误差建模带来的服务中断风险，具有显著的民用航空导航应用价值。
