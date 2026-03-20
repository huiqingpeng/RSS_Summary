---
title: "Self-Tuning Sparse Attention: Multi-Fidelity Hyperparameter Optimization for Transformer Acceleration"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18417"
published: "2026-03-20"
summarized: "2026-03-20T12:11:22.836280"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对稀疏注意力机制在生产环境中应用受限的问题，提出了AFBS-BO（自适应保真度二分搜索结合贝叶斯优化）框架，实现层级别和注意力头级别超参数的自动优化。该方法通过贝叶斯优化进行全局探索、二分搜索进行局部精修，并利用多保真度评估降低调优成本。在Llama-2-7B上的实验表明，相比网格搜索，AFBS-BO将超参数发现速度提升3.4倍，评估次数减少8.8倍，同时找到的高稀疏度配置在保持接近稠密注意力质量的同时超越现有稀疏注意力基线。

【方法概述 / Method】
AFBS-BO采用混合优化策略：贝叶斯优化负责全局超参数空间探索，二分搜索实现局部高效精修，并通过在不同序列长度上进行多保真度评估来加速收敛。该方法针对Transformer每层每注意力头的稀疏注意力超参数进行自动化搜索，无需人工干预。

【实验结果 / Results】
在Llama-2-7B模型上，AFBS-BO相比传统网格搜索实现3.4倍加速和8.8倍评估次数减少；发现的高稀疏度配置在性能上超越现有稀疏注意力基线，同时与稠密注意力的输出质量保持高度一致。

【应用价值 / Applications】
AFBS-BO将稀疏注意力从需要手动调优的启发式方法转变为自优化原语，可即插即用地应用于多种Transformer架构和领域，显著降低长上下文Transformer的部署门槛，推动稀疏注意力机制的实际生产落地。
