---
title: "Adversarial Vulnerabilities in Neural Operator Digital Twins: Gradient-Free Attacks on Nuclear Thermal-Hydraulic Surrogates"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22525"
published: "2026-03-25"
summarized: "2026-03-26T07:15:08.830315"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究首次系统揭示了神经算子（neural operators）作为核热工数字孪生核心预测模型时的对抗脆弱性。研究发现，神经算子对极稀疏（少于1%输入点）、物理合理的边界条件扰动极为敏感，可导致相对L₂误差从约1.5%的验证精度骤升至37-63%，而标准验证指标完全无法检测此类攻击。作者提出基于Jacobian的有效扰动维度d_eff诊断指标，建立了双因素脆弱性模型，解释了为何极端敏感度集中的架构并非最易受攻击，同时证明无梯度搜索在存在梯度病理的架构上优于基于梯度的攻击方法。

【方法概述 / Method】

研究采用无梯度差分进化（differential evolution）算法，在四种神经算子架构（包括POD-DeepONet、S-DeepONet等）上搜索对抗扰动，以绕过梯度消失/爆炸等梯度病理问题。引入有效扰动维度d_eff作为架构脆弱性诊断工具，该指标通过Jacobian矩阵分析敏感度在输入空间的集中程度，结合敏感度幅值构建脆弱性评估框架。

【实验结果 / Results】

实验表明，单点攻击成功率达100%且全部通过z-score异常检测；同等幅值的随机扰动成功率接近零，证实漏洞具有结构性特征。无梯度攻击在存在梯度病理的架构上显著优于PGD等梯度基方法。POD-DeepONet（d_eff≈1）因低秩输出投影限制了最大误差，而S-DeepONet（d_eff≈4）凭借适度的敏感度集中与充分放大效应表现出最高的攻击成功率。

【应用价值 / Applications】

该研究为核能与能源系统中安全关键型数字孪生的部署提供了重要安全警示，强调神经算子模型在标准验证之外需要额外的鲁棒性保证。研究成果可指导高可靠性工程应用中 surrogate 模型的安全评估流程设计，推动发展针对物理信息神经网络的对抗防御机制，对核电站实时监测、预测性维护等场景具有直接的安全工程价值。
