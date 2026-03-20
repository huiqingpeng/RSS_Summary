---
title: "Clipped Gradient Methods for Nonsmooth Convex Optimization under Heavy-Tailed Noise: A Refined Analysis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.23178"
published: "2026-03-20"
summarized: "2026-03-20T14:18:06.722499"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对重尾噪声下的非光滑凸优化问题，对梯度截断随机梯度下降（Clipped SGD）进行了精细化分析。作者提出了"广义有效维度"（generalized effective dimension, $d_{\rm eff}$）的概念，并获得了比现有最优结果更快的收敛速率：对于非光滑凸问题为 $\mathcal{O}(\sigma_{\frak l}d_{\rm eff}^{-1/2{\frak p}}\ln^{1-1/{\frak p}}(1/\delta)T^{1/{\frak p}-1})$，对于强凸问题为 $\mathcal{O}(\sigma_{\frak l}^2d_{\rm eff}^{-1/{\frak p}}\ln^{2-2/{\frak p}}(1/\delta)T^{2/{\frak p}-2})$。研究还将精细化分析推广到期望收敛情形，得到了突破已知下界的新速率，并建立了匹配的高概率和期望收敛下界，证明了期望收敛分析的最优性。

【方法概述 / Method】

本文的核心技术改进体现在两个方面：一是更优地利用Freedman不等式进行概率分析，二是在重尾噪声下对截断误差建立更精细的上界估计。作者通过引入广义有效维度 $d_{\rm eff} \geq 1$ 这一关键量，刻画了问题结构对收敛速率的影响，从而突破了原有分析框架的局限性。

【实验结果 / Results】

理论分析表明，新获得的高概率收敛速率在 $d_{\rm eff}$ 较大时显著优于现有最优结果，分别实现了 $\mathcal{O}(d_{\rm eff}^{-1/2{\frak p}})$ 和 $\mathcal{O}(d_{\rm eff}^{-1/{\frak p}})$ 的加速。在期望收敛方面，新上界突破了此前已知的下界限制，且作者建立的新下界与上界相匹配，证明了所得速率的最优性。

【应用价值 / Applications】

该研究对现代机器学习任务具有重要价值，特别是那些梯度噪声呈现重尾分布的场景（如深度学习中的大规模训练、强化学习、联邦学习等）。通过揭示问题有效维度对收敛速率的影响，该工作为算法设计和超参数调优提供了更精细的理论指导，有助于在实际应用中更高效地处理具有重尾噪声的优化问题。
