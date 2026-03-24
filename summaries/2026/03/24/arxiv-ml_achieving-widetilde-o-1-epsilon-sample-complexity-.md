---
title: "Achieving $\widetilde{O}(1/\epsilon)$ Sample Complexity for Bilinear Systems Identification under Bounded Noises"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20819"
published: "2026-03-24"
summarized: "2026-03-25T07:14:30.809619"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了离散时间双线性系统在有界对称对数凹扰动下的有限样本集员辨识问题。与现有线性系统的有限样本结果及更强噪声假设下的相关分析相比，该工作考虑了更具挑战性的双线性设定（具有轨迹依赖的回归量），并允许边缘稳定动态和多项式均方状态增长。在此条件下，作者证明了可行参数集的直径以 $\widetilde{O}(1/\epsilon)$ 的样本复杂度收缩，仿真结果验证了理论并展示了所提估计器在不确定性量化方面的优势。

【方法概述 / Method】
本文采用集员辨识（set-membership identification）框架，针对双线性系统设计有限样本分析方法，通过刻画轨迹依赖回归量的统计特性来处理双线性交互项带来的挑战。该方法结合对数凹噪声的几何性质与多项式状态增长的稳定性分析，建立了参数估计误差的上界。

【实验结果 / Results】
理论分析表明，所提估计器实现了 $\widetilde{O}(1/\epsilon)$ 的样本复杂度，这是双线性系统辨识中的一个重要理论突破。数值仿真验证了理论预测，并显示该方法在不确定性量化方面优于传统方法，能够有效约束真实参数所在的集合。

【应用价值 / Applications】
该研究为双线性系统（常见于化学反应过程、电力系统和经济模型等）的鲁棒辨识提供了理论保证，特别适用于噪声有界但分布未知的实际场景。所提方法可用于模型预测控制、自适应控制和安全性验证等需要可靠不确定性量化的应用领域。
