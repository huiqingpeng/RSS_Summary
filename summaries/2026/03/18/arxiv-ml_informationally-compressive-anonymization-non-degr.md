---
title: "Informationally Compressive Anonymization: Non-Degrading Sensitive Input Protection for Privacy-Preserving Supervised Machine Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15842"
published: "2026-03-18"
summarized: "2026-03-18T15:36:11.595564"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了信息压缩匿名化（Informationally Compressive Anonymization, ICA）及其VEIL架构，一种通过架构与数学设计而非噪声注入或加密实现隐私保护机器学习的新框架。ICA在可信源环境中将原始输入转换为低维、任务对齐的潜在表示，严格证明这些编码在拓扑和信息论意义上具有结构性不可逆性，即使在理想化攻击假设下也无法还原原始数据。该方法在保持预测效用的同时避免了差分隐私的性能损失和同态加密的计算开销，为企业级安全、高性能且具备后量子安全性的机器学习奠定了新基础。

【方法概述 / Method】

ICA采用监督式多目标编码器，将隐私保护嵌入表示学习过程，通过联合优化重构约束与下游任务目标，生成既压缩又任务对齐的潜在向量。VEIL架构建立严格的信任边界，将编码器隔离于可信源环境，仅向不可信的训练与推理环境输出不可逆的匿名化向量，无需梯度裁剪、噪声预算或推理时加密。

【实验结果 / Results】

论文通过拓扑与信息论严格证明ICA编码的结构性不可逆性：潜在空间的维度压缩导致原像集构成连续流形，攻击者的条件熵趋于发散，重建概率趋近于零。与现有自动编码器隐私保护方法相比，ICA在保持监督学习任务性能的同时实现了低延迟推理，消除了传统隐私保护技术带来的性能退化与计算瓶颈。

【应用价值 / Applications】

ICA/VEIL适用于需要处理敏感数据的企业级机器学习场景，如金融、医疗和跨境数据协作，天然符合隐私设计（privacy-by-design）的监管框架要求。该方法支持可扩展的多区域部署，在应对后量子计算威胁方面具有架构优势，为高隐私需求、高性能要求的生产环境提供了安全且实用的解决方案。
