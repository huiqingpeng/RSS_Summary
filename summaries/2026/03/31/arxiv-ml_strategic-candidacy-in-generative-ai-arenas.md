---
title: "Strategic Candidacy in Generative AI Arenas"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26891"
published: "2026-03-31"
summarized: "2026-04-01T07:20:31.568916"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了生成式AI竞技场（如Chatbot Arena）中的策略性候选问题：模型生产者通过提交多个克隆模型来人为提升其顶级模型的排名。作者从理论和模拟两方面证明了这种操纵行为的可行性，并提出了一种名为"You-Rank-We-Rank"（YRWR）的新排名机制。该机制要求生产者提交其自有模型的内部排名，并利用这些信息修正统计估计，证明其具有近似克隆鲁棒性，且能提升整体排名准确性。

【方法概述 / Method】
论文提出的YRWR机制要求模型生产者在提交多个模型时，同时提供这些模型的内部排序信息。该机制将这些自排序作为先验信息，用于校正基于成对用户偏好的模型质量统计估计，从而区分真实质量差异与随机噪声。

【实验结果 / Results】
基于LMArena真实数据校准的模拟实验表明，YRWR机制确实具有近似克隆鲁棒性——生产者无法通过提交克隆模型显著提升自己的排名；同时，即使生产者对其模型存在一定程度的误排，该机制仍能量化提升整体排名准确性。

【应用价值 / Applications】
该研究可直接应用于AI模型评估平台（如Chatbot Arena、Hugging Face Leaderboard等），通过机制设计防止模型生产者滥用系统漏洞，确保排名系统的公平性和可靠性，从而维护用户对AI模型评估结果的信任。
