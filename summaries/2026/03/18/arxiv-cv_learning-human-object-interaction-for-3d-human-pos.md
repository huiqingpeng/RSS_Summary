---
title: "Learning Human-Object Interaction for 3D Human Pose Estimation from LiDAR Point Clouds"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16343"
published: "2026-03-18"
summarized: "2026-03-18T18:11:29.510103"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Human-Object Interaction Learning (HOIL)框架，用于从LiDAR点云中进行鲁棒的3D人体姿态估计。该框架针对人机交互中的两个核心挑战——交互区域的空间歧义性和交互部位点云数据的类别不平衡问题，分别设计了人机交互感知对比学习(HOICL)模块和接触感知部位引导池化(CPPool)模块。此外，还引入了基于接触的时间精修机制来优化帧间关键点预测。实验结果表明，HOIL能够有效利用人机交互信息提升姿态估计的准确性。

【方法概述 / Method】
HOIL框架包含三个核心组件：HOICL通过对比学习增强人体与物体点在交互区域的特征区分度，缓解空间歧义问题；CPPool通过自适应压缩过度表示的非交互点、保留交互部位的稀疏信息点来解决类别不平衡；可选的接触基时间精修模块则利用时序接触线索修正单帧预测误差。

【实验结果 / Results】
（注：原文摘要未提供具体数值结果，仅说明方法有效性）实验验证了HOIL在解决交互区域空间歧义和类别不平衡方面的有效性，能够显著提升存在人机交互场景下的3D人体姿态估计性能，代码将开源发布。

【应用价值 / Applications】
该研究直接服务于自动驾驶中的行人安全理解任务，能够在复杂城市场景中准确估计与周围物体（如车辆、自行车、长椅等）发生交互的行人的3D姿态，为自动驾驶系统的决策规划提供更可靠的环境感知信息，降低交通事故风险。
