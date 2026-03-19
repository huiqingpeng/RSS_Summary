---
title: "A Controlled Comparison of Deep Learning Architectures for Multi-Horizon Financial Forecasting: Evidence from 918 Experiments"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16886"
published: "2026-03-19"
summarized: "2026-03-19T13:05:47.139629"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究对九种深度学习架构（Autoformer、DLinear、iTransformer、LSTM、ModernTCN、N-HiTS、PatchTST、TimesNet、TimeXer）进行了严格控制的比较，涵盖Transformer、MLP、CNN和RNN家族，在加密货币、外汇和股指市场进行4小时和24小时多步价格预测。通过918次实验和五阶段严格协议，研究发现ModernTCN以1.333的平均排名和75%的夺冠率表现最佳，架构差异解释了几乎所有性能方差，而种子随机性影响可忽略。关键发现是MSE训练模型在小时级分辨率上缺乏方向性预测能力，方向准确率接近50%。

【方法概述 / Method】

研究采用五阶段实验协议：固定种子贝叶斯超参数优化、按资产类别冻结配置、多种子重训练、不确定性聚合和统计验证，确保结果的可重复性和统计严谨性。实验覆盖三大市场（加密货币、外汇、股指）和两个预测 horizon（4小时和24小时），系统评估了九种代表性时序预测架构。

【实验结果 / Results】

结果呈现清晰的三层排名结构：ModernTCN（1.333）和PatchTST（2.000）领先，iTransformer（3.667）和TimesNet（4.000）居中，LSTM（7.000）和DLinear（8.333）垫底。尽管24小时 horizon 的误差放大2-2.5倍，排名稳定性仍得以保持。所有配置的方向准确率均接近50%，表明MSE优化无法捕捉价格方向信息。架构选择解释了性能方差的主要来源。

【应用价值 / Applications】

研究为量化金融领域的多步预测提供了可复现的架构选择指南，强调归纳偏置优于参数量堆砌。对投资组合配置、风险管理和算法交易策略开发具有直接指导意义，特别是在需要严格模型验证和不确定性量化的机构投资场景中。发现MSE训练的局限性也提示业界需探索方向感知的损失函数设计。
