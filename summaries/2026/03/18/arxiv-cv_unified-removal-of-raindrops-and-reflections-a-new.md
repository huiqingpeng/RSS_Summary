---
title: "Unified Removal of Raindrops and Reflections: A New Benchmark and A Novel Pipeline"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16446"
published: "2026-03-18"
summarized: "2026-03-18T18:13:33.530004"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文首次正式定义了雨滴与反射联合去除（UR³）任务，针对雨天透过玻璃拍摄时雨滴与反射同时出现的复合退化问题。作者构建了首个真实拍摄的RDRF数据集作为新基准，并提出了基于扩散模型的DiffUR³框架。实验表明该方法在基准测试和真实场景图像上均达到最优性能。

【方法概述 / Method】
DiffUR³采用扩散模型框架，利用其强大的生成先验能力同时去除两种退化。框架包含多个针对性设计以应对这一挑战性任务，通过生成式建模恢复被雨滴遮挡和反射干扰的清晰背景。

【实验结果 / Results】
该方法在RDRF基准数据集上取得最先进性能，并在具有挑战性的野外真实图像上展现出良好的泛化能力。实验验证了统一去除两种退化的有效性，相比分别处理或现有全合一模型有显著提升。

【应用价值 / Applications】
该研究可直接应用于智能驾驶挡风玻璃视觉增强、监控摄像头雨天成像恢复、手机透过玻璃拍摄等场景。统一处理框架避免了级联或分别去除两种退化的复杂流程，为实际视觉系统提供了更鲁棒的解决方案。
