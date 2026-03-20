---
title: "Elastic Weight Consolidation Done Right for Continual Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18596"
published: "2026-03-20"
summarized: "2026-03-20T12:14:00.875266"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文系统分析了弹性权重巩固（EWC）在持续学习中权重重要性估计的缺陷，首次发现基于Fisher信息矩阵的方法会导致梯度消失和不准确的重要性估计，同时揭示其变体MAS存在对无关参数施加冗余保护的问题。为此，作者提出Logits Reversal（LR）操作，通过反转logit值计算FIM来纠正上述问题，实验表明该方法显著优于现有EWC及其变体。

【方法概述 / Method】
论文从基于梯度的视角对EWC的重要性估计机制进行理论分析，识别出FIM计算中的梯度消失问题和MAS的冗余保护现象。提出的Logits Reversal操作通过在计算FIM时反转输出logit值，使得梯度计算更加稳定准确，从而得到更可靠的权重重要性估计。

【实验结果 / Results】
在多个持续学习任务和数据集上的大量实验表明，EWC-DR显著优于传统的EWC及其变体（包括MAS），有效缓解了灾难性遗忘问题。该方法在保持模型对旧任务性能的同时，提升了在新任务上的学习能力，实现了更优的持续学习整体表现。

【应用价值 / Applications】
该研究为持续学习中的权重正则化方法提供了理论基础和实践改进，可广泛应用于需要模型顺序学习多个任务而不遗忘旧知识的场景，如终身学习系统、个性化推荐、医疗诊断模型更新等领域，有助于构建更稳定可靠的机器学习系统。
