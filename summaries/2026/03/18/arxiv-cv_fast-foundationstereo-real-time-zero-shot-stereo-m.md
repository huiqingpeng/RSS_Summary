---
title: "Fast-FoundationStereo: Real-Time Zero-Shot Stereo Matching"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.11130"
published: "2026-03-18"
summarized: "2026-03-18T18:31:02.305927"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Fast-FoundationStereo，首次实现了强零样本泛化能力与实时帧率的双目立体匹配。通过知识蒸馏、分块神经网络架构搜索和结构化剪枝的分治加速策略，模型比FoundationStereo快10倍以上，同时保持相近的零样本精度。研究还构建了包含140万对野外立体图像的自动伪标签流水线以补充训练数据。

【方法概述 / Method】
论文采用三阶段分治加速策略：（1）知识蒸馏将混合骨干网络压缩为单一高效学生网络；（2）分块神经网络架构搜索在延迟约束下自动发现最优代价过滤设计，指数级降低搜索复杂度；（3）结构化剪枝消除迭代精修模块中的冗余。同时引入自动伪标签流水线生成大规模野外训练数据。

【实验结果 / Results】
Fast-FoundationStereo在运行速度上超过FoundationStereo 10倍以上，同时紧密匹配其零样本精度，在实时方法中建立了新的最先进水平。分块架构搜索显著降低了神经架构搜索的计算复杂度，结构化剪枝有效去除了迭代精修模块的冗余参数。

【应用价值 / Applications】
该研究解决了立体基础模型计算成本过高、无法实时应用的瓶颈，可广泛应用于自动驾驶、机器人导航、增强现实等需要实时深度估计的场景。零样本泛化能力消除了昂贵的逐领域微调需求，大幅降低了实际部署成本。
