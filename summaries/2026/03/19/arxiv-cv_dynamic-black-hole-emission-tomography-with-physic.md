---
title: "Dynamic Black-hole Emission Tomography with Physics-informed Neural Fields"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2602.08029"
published: "2026-03-19"
summarized: "2026-03-19T17:05:51.014248"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了PI-DEF（Physics-Informed Differentiable Emissivity Fields），一种基于物理信息神经场的动态黑洞发射层析成像方法，用于从稀疏的射电干涉测量数据中重建黑洞周围气体的四维（时间+三维）发射率场。该方法通过联合重建三维速度场并将其作为软约束施加于发射率动力学，克服了先前BH-NeRF方法在开普勒动力学假设上的局限性。实验表明，PI-DEF在模拟数据上的重建精度显著优于BH-NeRF和纯数据驱动方法，并可用于估计黑洞自旋等物理参数。

【方法概述 / Method】
PI-DEF采用可微分神经渲染技术，将四维发射率场参数化为神经辐射场（NeRF），同时联合优化三维速度场。该方法将速度场作为物理软约束融入发射率的时间演化，通过可微分光线追踪将四维场投影到二维观测平面，以匹配事件视界望远镜（EHT）的稀疏干涉测量数据，无需预设开普勒轨道假设。

【实验结果 / Results】
在模拟EHT观测数据的实验中，PI-DEF相比BH-NeRF和纯神经网络基线方法取得了显著更优的重建精度，能够准确恢复黑洞附近复杂非开普勒动力学下的气体结构。该方法还可从重建的速度场中推断黑洞的物理参数，如自旋，展示了其在参数估计方面的潜力。

【应用价值 / Applications】
该研究为下一代事件视界望远镜（ngEHT）的动态黑洞成像提供了关键技术，可实现对黑洞吸积流的三维实时演化观测，揭示强引力场区域的极端物理过程。其物理信息神经场框架还可推广至其他天体物理层析成像问题，为检验广义相对论和黑洞天体物理学模型提供新的观测手段。
