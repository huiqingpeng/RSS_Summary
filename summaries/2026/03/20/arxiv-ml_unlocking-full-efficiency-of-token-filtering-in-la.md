---
title: "Unlocking Full Efficiency of Token Filtering in Large Language Model Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2502.00340"
published: "2026-03-20"
summarized: "2026-03-20T14:05:25.112979"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了 Centrifuge，一个通过算法与系统协同设计来充分释放大语言模型训练中 token 过滤效率潜力的系统。现有 token 过滤方法未能实现实际加速，主要原因在于稀疏性不足以及非标准稀疏范围无法被现有机器学习库高效支持。Centrifuge 在算法层面通过注意力反向传播核过滤无关 token 的激活值以增强反向计算的稀疏性，在系统层面提出自动工作流将稀疏 GEMM 转换为降维稠密 GEMM，从而在标准 ML 库上实现优化效率。

【方法概述 / Method】
Centrifuge 采用算法-系统协同设计：算法上在注意力机制的反向传播核中过滤不重要 token 的激活值，放大反向计算的稀疏性；系统上开发自动工作流，将稀疏 GEMM 运算转换为维度降低的稠密 GEMM 运算，使其能够利用标准 ML 库（如 cuBLAS）高效执行，避免自定义稀疏核的开销。

【实验结果 / Results】
在 1.1B 到 40B 参数的模型上评估表明，当过滤 50% token 时，Centrifuge 可减少高达 49.9% 的反向传播时间和 34.7% 的端到端训练时间；同时保持 token 过滤的效用优势，相比标准训练显著提升模型性能达 26.6%。

【应用价值 / Applications】
Centrifuge 可无缝集成到现有 LLM 训练框架中，已使用 token 过滤的系统仅需一行代码即可加速训练，为大语言模型的预训练和微调提供实际可行的计算效率提升方案，降低训练成本的同时改善模型质量。
