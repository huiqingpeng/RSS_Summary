---
title: "Behavior-Centric Extraction of Scenarios from Highway Traffic Data and their Domain-Knowledge-Guided Clustering using CVQ-VAE"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16964"
published: "2026-03-19"
summarized: "2026-03-19T13:07:09.044520"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种基于行为中心的交通场景提取方法，以及利用CVQ-VAE进行领域知识引导的场景聚类技术。研究解决了自动驾驶系统验证中场景提取标准不统一和机器学习聚类缺乏可解释性的两大挑战。通过在highD数据集上的实验，证明了该方法能够可靠地提取高速公路场景，并有效整合领域知识进行聚类，从而为自动驾驶车辆的高效验证提供标准化的场景类别推导流程。

【方法概述 / Method】
论文采用"Scenario-as-Specification"概念实现标准化的场景提取，确保场景定义的一致性。在聚类阶段，使用条件向量量化变分自编码器（CVQ-VAE）作为核心架构，将领域知识以条件向量的形式嵌入到聚类过程中，实现数据驱动与专家知识的结合。

【实验结果 / Results】
实验在highD高速公路数据集上进行，验证了所提场景提取方法的可靠性。结果表明，CVQ-VAE架构能够有效整合领域知识指导聚类过程，生成的场景类别既保持了数据驱动的复杂性处理能力，又具备与专家认知一致的可解释性。

【应用价值 / Applications】
该方法可直接应用于自动驾驶系统的测试验证流程，为从真实交通数据中系统性地构建标准化测试场景库提供技术支撑。通过生成具有明确语义、符合工程直觉的场景类别，有助于监管机构制定统一的自动驾驶安全评估标准，加速自动驾驶技术的商业化落地。
