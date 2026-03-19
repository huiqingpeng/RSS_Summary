---
title: "Mirror Descent on Riemannian Manifolds"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17527"
published: "2026-03-19"
summarized: "2026-03-19T13:12:44.593225"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文将经典的镜像下降法（Mirror Descent）推广到黎曼流形优化问题，提出了黎曼镜像下降（RMD）框架及其随机变体（stochastic RMD）。作者建立了RMD和随机RMD的非渐近收敛保证，并将该框架应用于Stiefel流形，证明其退化为已有的曲率梯度下降（CGD）方法，同时得到了CGD的随机扩展版本，可有效解决大规模流形优化问题。

【方法概述 / Method】
论文通过重新参数化（reparameterization）技术将欧几里得空间中的镜像下降法推广到黎曼流形，构建了统一的黎曼镜像下降框架。该框架包含确定性版本和随机版本，能够处理带约束的流形优化问题，其中随机变体适用于大规模数据场景。

【实验结果 / Results】
论文主要建立了理论收敛保证：证明了RMD和随机RMD的非渐近收敛速率。在Stiefel流形上的特例分析表明，所提框架与现有CGD方法具有等价性，且随机扩展版本能够有效处理大规模优化问题，为实际应用提供了理论支撑。

【应用价值 / Applications】
该研究可应用于图像处理、策略优化和神经网络训练等涉及流形约束的大规模优化场景。特别是Stiefel流形上的随机扩展为大规模正交约束优化问题（如深度学习的正交权重初始化、子空间学习等）提供了高效且可扩展的优化工具。
