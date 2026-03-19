---
title: "Detecting Data Contamination from Reinforcement Learning Post-training for Large Language Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.09259"
published: "2026-03-19"
summarized: "2026-03-19T14:17:17.086103"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文首次系统研究了大型语言模型（LLMs）在强化学习（RL）后训练阶段的数据污染检测问题。作者发现RL训练后模型输出熵分布会坍缩为高度特定的稀疏模式，基于此提出了Self-Critique方法，通过探测策略坍缩（policy collapse）来识别污染数据。实验表明该方法在RL-MIA基准上显著优于基线方法，AUC提升高达30%，而现有方法在此场景下几乎等同于随机猜测。

【方法概述 / Method】
Self-Critique方法的核心是利用RL后训练导致的"策略坍缩"现象——模型收敛到狭窄的推理路径，表现为输出熵的显著降低。该方法通过分析模型输出的分布特性来探测这种熵坍缩，从而识别训练数据中混入的基准测试样本。为验证该方法，作者还构建了专门模拟RL阶段污染场景的RL-MIA基准数据集。

【实验结果 / Results】
在RL-MIA基准上的大量实验表明，Self-Critique在多个模型和污染任务上均显著优于基线方法，AUC提升最高达30%。特别值得注意的是，针对RL后训练阶段的污染检测，现有方法（如Min-K% Prob等）表现接近随机水平（AUC≈0.5），而Self-Critique使有效检测成为可能，证明了专门针对RL阶段设计检测方法的必要性。

【应用价值 / Applications】
该研究对LLM评估的可靠性具有重要价值，特别是在RL后训练日益成为提升模型推理能力关键手段的背景下。Self-Critique可用于审计和验证RL训练数据的质量，防止基准测试数据泄露导致的性能虚高，为学术研究和工业界提供更可信的模型能力评估工具，支撑更负责任的AI模型开发与部署。
