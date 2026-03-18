---
title: "Muon Converges under Heavy-Tailed Noise: Nonconvex H\"{o}lder-Smooth Empirical Risk Minimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15059"
published: "2026-03-18"
summarized: "2026-03-18T17:07:48.907258"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本论文研究了 Muon 优化器在非凸 Hölder 光滑经验风险最小化问题中的收敛性理论。作者证明了在存在重尾随机噪声（而非传统有界方差假设）的实际机器学习场景下，Muon 仍能收敛到平稳点。此外，理论分析表明 Muon 的收敛速度优于小批量随机梯度下降（SGD），为其在大规模深度神经网络中的高效稳定训练提供了理论保证。

【方法概述 / Method】

论文采用非凸优化理论分析方法，将 Muon 优化器建模为在 Stiefel 流形上的正交投影梯度更新过程。作者建立了适用于重尾噪声的有限性条件（boundedness condition），替代传统的有界方差假设，并在此框架下推导收敛性证明。

【实验结果 / Results】

理论结果表明，在重尾噪声和非凸 Hölder 光滑条件下，Muon 能够保证收敛到经验风险的平稳点。与 mini-batch SGD 相比，Muon 展现出更快的收敛速率，验证了该优化器在实际深度学习训练中的效率优势。

【应用价值 / Applications】

该研究为 Muon 优化器在大规模深度学习模型训练中的应用提供了坚实的理论基础，特别是在噪声呈现重尾特性的实际场景中。研究成果有助于指导开发更鲁棒的优化算法，提升深度神经网络训练的稳定性和效率，对大型语言模型等需要大规模优化的应用具有重要参考价值。
