---
title: "Multi-Modal Multi-Agent Reinforcement Learning for Radiology Report Generation: Radiologist-Like Workflow with Clinically Verifiable Rewards"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16876"
published: "2026-03-19"
summarized: "2026-03-19T12:18:48.098604"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MARL-Rad，一种新颖的多模态多智能体强化学习框架，用于放射学报告生成。该框架通过协调多个区域特异性智能体和一个全局整合智能体，并利用临床可验证的奖励进行优化。与先前单模型强化学习或对独立训练模型进行事后智能体化的方法不同，本方法联合训练多个智能体并通过强化学习优化整个智能体系统。在MIMIC-CXR和IU X-ray数据集上的实验表明，MARL-Rad在临床有效性指标（如RadGraph、CheXbert和GREEN分数）上持续改进，达到了最先进的临床性能。

【方法概述 / Method】
MARL-Rad采用多智能体强化学习架构，包含多个专注于特定解剖区域的区域智能体和一个负责整合全局信息的全局智能体。系统通过临床可验证的奖励函数进行端到端训练，使多个智能体能够协同优化，模拟放射科医生的工作流程。

【实验结果 / Results】
在MIMIC-CXR和IU X-ray两个标准数据集上的实验显示，MARL-Rad在临床有效性（CE）指标上取得显著提升，RadGraph、CheXbert和GREEN分数均达到当前最优水平。进一步分析证实，该方法增强了报告的双侧一致性（laterality consistency），并生成更准确、细节更丰富的诊断报告。

【应用价值 / Applications】
该研究可直接应用于临床放射学工作流程自动化，辅助放射科医生高效生成高质量、临床可验证的诊断报告。通过模拟专家级放射科医生的多区域分析流程，MARL-Rad有望减少漏诊风险、提高报告标准化程度，并缓解医疗资源短缺地区的诊断压力。
