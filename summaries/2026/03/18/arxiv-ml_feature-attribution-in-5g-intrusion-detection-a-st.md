---
title: "Feature Attribution in 5G Intrusion Detection: A Statistical vs. Logic-Based Comparison"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.10206"
published: "2026-03-18"
summarized: "2026-03-18T17:11:33.026459"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本论文针对5G网络入侵检测场景，系统比较了统计方法与逻辑方法在特征归因（feature attribution）上的差异。研究选取SHAP（统计方法代表）和VoTE-XAI（逻辑方法代表）两种解释技术，在三个5G相关数据集（5G-NIDD、MSA、PFCP）上分析XGBoost模型的安全警报解释。核心发现表明：逻辑归因方法在稀疏性（解释简洁度）和稳定性（同类攻击样本间一致性）方面表现更优，且两种方法存在显著特征选择分歧——SHAP选出的顶级特征均被VoTE-XAI覆盖，但反之不成立。

【方法概述 / Method】

研究采用对比实验设计，以XGBoost作为基础入侵检测模型，分别在涵盖多种攻击场景的5G-NIDD、MSA和PFCP数据集上生成警报。通过SHAP（基于Shapley值的统计特征归因）与VoTE-XAI（基于形式化逻辑的符号推理方法）分别解释模型输出，并从稀疏性、稳定性、效率三个维度量化评估解释质量。

【实验结果 / Results】

实验结果显示逻辑归因方法在稀疏性和稳定性指标上 consistently 优于统计方法。关键发现是两种方法存在显著的特征选择分歧，但SHAP识别的顶级特征全部被VoTE-XAI捕获，表明逻辑方法具有更完备的特征覆盖能力。此外，研究验证了两种方法在高维5G环境（478维特征）下的实时处理可行性。

【应用价值 / Applications】

该研究为5G网络安全运营中的可解释AI部署提供决策依据：逻辑归因方法更适合需要高可靠性和一致性的安全编排与自动化响应（SOAR）场景，而统计方法可作为快速筛选的辅助手段。研究成果有助于推动从"检测恶意活动"向"提供可执行缓解 verdict"的5G安全范式转变，支持关键基础设施的实时安全监控需求。
