---
title: "From Physics to Surrogate Intelligence: A Unified Electro-Thermo-Optimization Framework for TSV Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29268"
published: "2026-04-01"
summarized: "2026-04-02T07:17:20.446836"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究针对2.5D/3D异构集成中的高密度硅通孔（TSV）网络，提出了一个可扩展的电-热建模与优化框架，以解决传统全波有限元方法（FEM）在大规模设计空间探索中计算成本过高的问题。该框架融合了物理信息解析建模、图神经网络（GNN）代理模型和全波签核验证，实现了对反射系数、插入损耗、串扰（NEXT/FEXT）和有效热导率的多目标帕累托优化。实验表明，该框架可在数分钟内探索数百万种TSV配置，单次设计评估时间较FEM降低超过六个数量级，同时保持与Ansys HFSS和Mechanical的高度一致性。

【方法概述 / Method】

论文采用三层级联架构：（1）基于多导体传输线理论的解析模型，计算TSV阵列的宽带S参数和有效各向异性热导率；（2）物理信息图神经网络代理模型（TSV-PhGNN），先以解析数据预训练，再以HFSS仿真数据微调，实现向更大阵列尺寸的泛化；（3）将代理模型嵌入多目标优化循环，结合全波签核验证确保最终设计可靠性。

【实验结果 / Results】

解析模型在15×15阵列尺寸内达到5%-10%的相对Frobenius误差（RFE）；TSV-PhGNN代理模型在更大阵列上的RFE低于2%且方差几乎恒定。优化框架可在数分钟内完成数百万种TSV配置的探索，最终设计经Ansys HFSS和Mechanical验证显示高度一致，单次评估时间从FEM的数小时缩短至毫秒级，实现超百万倍的加速比。

【应用价值 / Applications】

该框架适用于先进封装中TSV阵列的快速电-热协同设计，可支撑芯片设计早期阶段的大规模布局与几何参数优化，显著缩短设计周期并降低计算资源消耗。其方法学可推广至其他需要多物理场耦合优化的微纳尺度互连结构，为2.5D/3D集成技术的可靠性和信号完整性设计提供高效工具支撑。
