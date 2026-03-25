---
title: "Balancing Safety and Efficiency in Aircraft Health Diagnosis: A Task Decomposition Framework with Heterogeneous Long-Micro Scale Cascading and Knowledge Distillation-based Interpretability"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22885"
published: "2026-03-25"
summarized: "2026-03-26T07:18:03.362377"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对通用航空整机诊断面临的数据不确定性、任务异构性和计算效率低下三重挑战，提出诊断分解框架（DDF），将诊断任务显式解耦为异常检测（AD）和故障分类（FC）两个子任务。通过长程-微观尺度诊断器（LMSD）实现"长程全局筛查与微观局部精准诊断"的策略，并引入基于知识蒸馏的关键性提取层（KEL）提供物理可追踪的解释。在NGAFID真实航空数据集上的实验表明，该方法在多类别加权惩罚指标（MCWPM）上较基线提升约4-8%，同时显著减少训练时间。

【方法概述 / Method】
DDF框架采用异构长-微观尺度级联架构：ConvTokMHSA模块用于全局运行模式判别，MMK Net网络用于局部故障特征提取，实现不同感受野需求的分离。通过解耦训练将"大样本轻量级"与"小样本复杂"优化路径分离，降低计算开销；KEL层通过知识蒸馏从教师网络向学生网络传递决策关键性信息，实现可解释性设计。

【实验结果 / Results】
在NGAFID真实世界航空数据集上的验证显示，所提方法在MCWPM指标上较基线方法提升约4-8%，同时训练时间大幅减少。实验结果证实了该方法在任务适应性、可解释性和效率方面的综合优势，有效平衡了安全性与效率的权衡。

【应用价值 / Applications】
该研究为通用航空健康管理系统提供了一种可部署的方法论，特别适用于计算资源受限且对安全性和实时性要求高的航空诊断场景。其任务解耦与可解释性设计有助于维护人员理解模型决策依据，提升故障排查效率，对推动智能航空维护系统的实际落地具有重要工程价值。
