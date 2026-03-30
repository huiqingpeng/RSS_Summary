---
title: "Maintaining Difficulty: A Margin Scheduler for Triplet Loss in Siamese Networks Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26389"
published: "2026-03-30"
summarized: "2026-03-31T07:23:55.401104"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了孪生网络（Siamese Networks）中三元组边界排序损失（Triplet Margin Ranking Loss）的边界参数μ对训练过程的影响。作者发现，当观察到足够多违反边界的三元组时，许多三元组的有效边界往往会超过预定义的μ值，这表明固定边界可能限制学习过程。基于此，论文提出了一种边界调度器，根据每个epoch观察到的简单三元组比例动态调整μ值，以维持训练难度。实验结果表明，该策略在四个不同数据集上均取得了比固定边界和单调递增边界方案更好的验证性能。

【方法概述 / Method】
论文提出了一种自适应边界调度器，通过监控训练过程中"简单三元组"（即已经满足边界约束的三元组）的比例来动态调整边界参数μ。当简单三元组比例过高时，调度器增大μ以提升训练难度；反之则适当降低μ，从而在整个训练过程中保持适度的学习挑战。

【实验结果 / Results】
在四个不同数据集上的实验表明，所提出的边界调度策略相比固定边界和单调递增边界方案均取得了性能提升，验证性能（verification performance）获得了一致的改善，证明了动态维持训练难度的有效性。

【应用价值 / Applications】
该研究可广泛应用于基于距离度量学习（DML）的任务，如人脸识别、图像检索、行人重识别和签名验证等孪生网络应用场景。通过动态调整训练难度，该方法有助于提升模型的泛化能力和最终识别准确率，为实际部署提供更可靠的度量学习解决方案。
