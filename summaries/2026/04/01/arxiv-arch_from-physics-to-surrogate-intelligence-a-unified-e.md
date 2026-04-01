---
title: "From Physics to Surrogate Intelligence: A Unified Electro-Thermo-Optimization Framework for TSV Networks"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.29268"
published: "2026-04-01"
summarized: "2026-04-02T07:11:56.564838"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对高密度硅通孔（TSV）阵列在2.5D/3D异构集成中面临的信号完整性和热可靠性挑战，提出了一种可扩展的电-热建模与优化框架。该框架融合物理信息解析建模、图神经网络（GNN）代理模型和全波验证，实现了从物理分析到智能代理的统一电-热优化。TSV-PhGNN代理模型在大型阵列上的相对Frobenius误差低于2%，并将单次设计评估时间缩短超过六个数量级，使数百万种TSV配置的快速探索成为可能。

【方法概述 / Method】
论文采用三层递进式方法：首先建立多导体解析模型计算宽带S参数和各向异性等效热导率；继而构建物理信息图神经网络（TSV-PhGNN），以解析数据预训练、HFSS仿真微调；最终将代理模型集成至多目标帕累托优化框架，同时优化反射系数、插入损耗、串扰（NEXT/FEXT）和等效热导率。

【实验结果 / Results】
解析模型在15×15阵列规模内达到5%-10%相对Frobenius误差；TSV-PhGNN经微调后泛化至更大阵列，误差降至2%以下且方差近乎恒定。优化框架可在数分钟内探索数百万种TSV配置，最终设计经Ansys HFSS和Mechanical验证显示高度一致。

【应用价值 / Applications】
该框架适用于先进封装中TSV阵列的快速电-热协同设计，解决了传统FEM仿真在设计空间探索中的计算瓶颈。其方法可扩展至其他多物理场耦合的互连结构优化，为2.5D/3D集成电路的敏捷开发提供关键支撑。
