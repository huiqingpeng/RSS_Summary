---
title: "NutVLM: A Self-Adaptive Defense Framework against Full-Dimension Attacks for Vision Language Models in Autonomous Driving"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.13293"
published: "2026-03-19"
summarized: "2026-03-19T16:31:08.116942"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了NutVLM，一种面向自动驾驶视觉语言模型（VLMs）的自适应防御框架，用于应对从局部物理补丁到全局不可感知扰动的全维度对抗攻击。该框架通过NutNet++实现统一的三分类检测-净化机制，并采用专家引导的对抗提示调优（EAPT）技术生成纠正性驾驶提示，在无需全模型重训练的情况下重新聚焦VLM注意力。在Dolphins基准测试上，NutVLM在准确率、语言得分和GPT得分等综合指标上实现了4.89%的整体性能提升。

【方法概述 / Method】

NutVLM采用双阶段防御架构：第一阶段部署NutNet++作为哨兵网络，对输入样本进行三分类（良性样本/局部补丁/全局扰动）检测；第二阶段根据威胁类型执行差异化净化——局部威胁通过高效灰度掩码去除，全局扰动则触发EAPT机制，该机制通过基于梯度的潜在优化和离散投影生成纠正性提示，以轻量级提示工程替代昂贵的全参数微调。

【实验结果 / Results】

在Dolphins自动驾驶基准数据集上的评估表明，NutVLM在综合指标（包括Accuracy、Language Score和GPT Score）上取得4.89%的整体提升，有效验证了该框架在保持干净样本性能的同时显著提升对抗鲁棒性，实现了鲁棒性与干净准确性的较好平衡。

【应用价值 / Applications】

NutVLM为智能交通系统提供可扩展的安全解决方案，特别适用于依赖VLMs进行环境感知与决策的自动驾驶场景。其轻量化的提示调优机制降低了部署成本，使实时安全防护在计算资源受限的车载平台上具备实际可行性，有助于推动高可靠自动驾驶技术的商业化落地。
