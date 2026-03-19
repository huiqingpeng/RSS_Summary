---
title: "Learning Permutation Distributions via Reflected Diffusion on Ranks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17353"
published: "2026-03-19"
summarized: "2026-03-19T12:10:10.411793"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了Soft-Rank Diffusion，一种新的离散扩散框架，用于学习对称群S_n上的概率分布。该方法通过将离散排列提升为连续的软秩（soft-rank）表示来替代传统的基于洗牌（shuffle-based）的噪声添加过程，从而生成更平滑、更易处理的扩散轨迹。同时，作者引入了上下文化广义Plackett-Luce（cGPL）去噪器以增强对序列决策结构的表达能力。实验表明，该方法在排序和组合优化基准测试中 consistently 优于现有扩散基线，尤其在长序列和内在序列化任务中表现突出。

【方法概述 / Method】

该框架的核心创新在于"软秩前向过程"：将离散的排列排名松弛为连续的软排名表示，使得扩散轨迹在连续的排序空间中进行，避免了传统洗牌方法导致的突变式轨迹。反向过程中，cGPL去噪器通过上下文信息对广义Plackett-Luce模型进行参数化，能够更灵活地捕捉排列中的序列依赖结构。

【实验结果 / Results】

实验在排序任务和组合优化基准上进行，Soft-Rank Diffusion在所有测试设置中均优于现有的基于洗牌的扩散基线方法。特别地，该方法在长序列场景（大n）和具有内在序列化特性的任务中展现出显著的性能提升，验证了软秩表示在处理大规模排列空间时的优势。

【应用价值 / Applications】

该研究可广泛应用于需要建模排列分布的实际场景，包括排序学习、组合优化（如旅行商问题）、推荐系统中的排名生成、以及任何涉及离散排列决策的机器学习任务。软秩表示的连续性特征使其特别适合处理大规模排列问题，为复杂组合结构的生成建模提供了新的有效工具。
