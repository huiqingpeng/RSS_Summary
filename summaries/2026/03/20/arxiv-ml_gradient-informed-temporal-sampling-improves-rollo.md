---
title: "Gradient-Informed Temporal Sampling Improves Rollout Accuracy in PDE Surrogate Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18237"
published: "2026-03-20"
summarized: "2026-03-20T12:08:56.801975"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对神经模拟器（neural simulators）训练数据采样这一基础但尚未形式化的问题，提出梯度信息引导的时间采样方法（GITS）。GITS通过联合优化试点模型的局部梯度和集合层面的时间覆盖度，在模型特异性与动态信息之间取得有效平衡。实验表明，与多种采样基线相比，GITS在多个偏微分方程（PDE）系统、模型骨干网络和采样比例下均实现了更低的 rollout 误差，消融研究验证了其两个优化目标的必要性与互补性。

【方法概述 / Method】
GITS 是一种专为神经模拟器设计的数据采样方法，核心在于同时优化两个目标：一是利用试点模型的局部梯度信息捕捉模型敏感的高信息密度区域，二是通过集合层面的时间覆盖度保证采样的多样性。该方法通过梯度引导避免采样塌陷到局部区域，同时保持对动态演化过程的全面覆盖。

【实验结果 / Results】
GITS 在多个 PDE 系统（如流体动力学、热传导等）、不同模型骨干网络（包括 CNN、Transformer 等）以及 varying sample ratios 下均 consistently 优于均匀采样和其他先进采样基线，显著降低了 rollout 误差。消融研究表明，局部梯度优化与时间覆盖度优化缺一不可，二者具有互补性。此外，作者还分析了 GITS 的成功采样模式及其失效的典型场景。

【应用价值 / Applications】
该研究对科学计算和工程仿真领域具有重要价值，可提升基于神经网络的 PDE 求解器在流体力学、气候模拟、材料科学等场景中的长期预测精度和计算效率。通过优化训练数据采样策略，GITS 能够在相同数据预算下训练出更准确的代理模型，降低高保真数值模拟的数据生成成本，加速科学发现与工程设计迭代。
