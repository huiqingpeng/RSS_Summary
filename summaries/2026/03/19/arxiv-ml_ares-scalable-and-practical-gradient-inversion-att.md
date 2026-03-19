---
title: "ARES: Scalable and Practical Gradient Inversion Attack in Federated Learning through Activation Recovery"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17623"
published: "2026-03-19"
summarized: "2026-03-19T12:15:00.307876"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了ARES（Activation REcovery via Sparse inversion）攻击，一种针对联邦学习的主动梯度反演攻击方法，能够在无需修改模型架构的情况下从大规模训练批次中重建训练样本。该方法将激活恢复问题建模为带噪声的稀疏恢复任务，并利用广义Lasso求解，同时结合imprint方法实现多样本解耦。实验表明ARES在CNN和MLP架构上显著优于现有方法，揭示了中间层激活在联邦学习中构成严重且被低估的隐私风险。

【方法概述 / Method】

ARES通过将激活恢复问题形式化为带噪声的稀疏恢复（noisy sparse recovery）问题，采用广义最小绝对收缩和选择算子（Lasso）进行求解；为扩展至多样本场景，引入imprint方法对混合激活进行解耦，实现可扩展的逐样本重建。该方法无需对目标模型架构做任何修改，具有更强的实用性和可部署性。

【实验结果 / Results】

在CNN和MLP架构上的大量实验表明，ARES在多种数据集上均实现了高保真度的样本重建，尤其在大批次规模和真实联邦学习设置下显著优于现有梯度反演攻击方法。论文还从理论上建立了期望恢复率并推导了重建误差上界，为攻击效果提供了理论保证。

【应用价值 / Applications】

该研究揭示了联邦学习中共享模型更新（特别是中间层激活）带来的严重隐私泄露风险，为设计更强大的隐私防御机制提供了重要依据；同时，ARES作为一种实用的攻击评估工具，可用于审计联邦学习系统的隐私保护强度，推动隐私保护机器学习技术的安全部署与标准化评估。
