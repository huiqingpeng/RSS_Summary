---
title: "Survival In-Context: Prior-fitted In-context Learning Tabular Foundation Model for Survival Analysis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29475"
published: "2026-04-01"
summarized: "2026-04-02T07:18:36.843240"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了Survival In-Context (SIC)，首个针对生存分析的prior-fitted上下文学习表格基础模型。研究构建了一个灵活的生存数据生成框架，通过显式控制协变量和时间-事件分布来定义丰富的生存先验。SIC完全基于合成数据进行预训练，能够在单次前向传播中生成个体化生存预测，无需任务特定训练或超参数调优。在多个真实世界生存数据集上的广泛评估表明，SIC在中等数据规模场景下表现优于或媲美经典和深度生存模型，验证了prior-fitted基础模型在生存分析中的潜力。

【方法概述 / Method】

SIC采用prior-fitted范式，首先构建了一个可控的合成生存数据生成框架，通过参数化分布（如Weibull、Log-Normal等）对时间-事件关系和协变量效应进行显式建模，形成丰富的生存先验分布。基于此先验，模型通过元学习在大量合成数据集上进行预训练，学习从上下文示例到生存函数的映射，最终实现对任意新任务的零样本推理。

【实验结果 / Results】

SIC在多个真实生存数据集（包括METABRIC、SUPPORT、FLCHAIN等）上与Cox比例风险模型、DeepSurv、DeepHit等经典和深度方法进行了对比。实验表明，SIC在中等样本量（数百至数千样本）场景下表现尤为突出，在C-index和Brier Score等指标上达到竞争性或更优性能，同时显著降低了计算开销，无需针对新数据集进行微调。

【应用价值 / Applications】

SIC可直接应用于临床预后预测、患者风险评估等医疗场景，特别适合数据量有限但需快速部署的临床环境。由于模型无需任务特定训练和超参数调优，能够大幅降低医疗AI系统的开发门槛和部署成本，为资源受限的医疗机构提供即插即用的生存分析工具，推动精准医疗的普及化应用。
