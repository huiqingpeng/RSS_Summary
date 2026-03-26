---
title: "Diet Your LLM: Dimension-wise Global Pruning of LLMs via Merging Task-specific Importance Score"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23985"
published: "2026-03-26"
summarized: "2026-03-27T07:19:20.167107"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出DIET（Dimension-wise global pruning via merging Task-wise importance scores），一种无需训练的结构化剪枝方法，用于解决大语言模型部署中的规模挑战。DIET通过仅使用每任务100个样本分析激活幅度，并采用多数投票构建全局掩码，实现了维度级粒度与任务感知选择的结合。在Gemma-2 2B和9B模型上的实验表明，DIET在20%稀疏度下相比现有最优结构化剪枝方法平均准确率提升近10%，且优势在不同稀疏度和模型规模下持续存在。

【方法概述 / Method】

DIET采用训练自由的结构化剪枝策略，通过分析模型在各任务上的激活幅度来评估维度重要性。具体而言，该方法为每个任务计算维度级重要性分数，然后通过多数投票机制合并多任务的重要性分数，生成单一的全局剪枝掩码，从而在无需昂贵预计算或训练成本的情况下实现任务感知的维度选择。

【实验结果 / Results】

实验在七个零样本基准上进行，使用Gemma-2 2B和9B模型验证DIET的有效性。关键结果显示：在20%稀疏度下，Gemma-2 2B模型上DIET相比先前最优结构化剪枝方法平均准确率提升近10%；该性能优势在不同稀疏度水平和模型规模下保持稳定，证明了方法的鲁棒性和可扩展性。

【应用价值 / Applications】

DIET为大规模语言模型的实际部署提供了高效实用的解决方案，特别适用于资源受限环境下需要任务自适应能力的场景。由于无需训练且计算开销极低（每任务仅需100样本），该方法可广泛应用于边缘设备部署、多任务模型压缩以及快速模型定制等场景，显著降低了结构化剪枝的实用门槛。
