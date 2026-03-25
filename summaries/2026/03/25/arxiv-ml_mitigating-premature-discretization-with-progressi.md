---
title: "Mitigating Premature Discretization with Progressive Quantization for Robust Vector Tokenization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22304"
published: "2026-03-25"
summarized: "2026-03-26T07:09:17.988160"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文识别了传统向量量化（VQ）中的一个核心问题——"过早离散化"（Premature Discretization），即编码器尚未充分捕捉数据流形时就强制进行离散化。为此，作者提出渐进式量化（ProVQ），将量化难度动态变化作为VQ训练的新维度，通过课程学习的方式平滑地从连续潜在空间退火到离散空间。实验表明，ProVQ在图像重建生成（ImageNet-1K/100）和复杂生物序列建模（蛋白质结构token化）上均取得显著性能提升。

【方法概述 / Method】
ProVQ将量化过程视为一个课程学习问题，通过引入量化硬度（quantization hardness）的动态调度机制，使训练早期允许较"软"的量化（接近连续表示），随后逐渐退火至硬离散化。这种渐进策略引导码本向充分扩展的数据流形区域收敛，避免了传统VQ中编码器与量化器之间的优化冲突。

【实验结果 / Results】
在ImageNet-1K和ImageNet-100基准上，ProVQ实现了更优的重建质量和生成性能；在蛋白质结构token化任务中，ProVQ在StructTokenBench排行榜上建立了新的性能上限。这些跨模态结果验证了ProVQ对生成式建模的广泛增益。

【应用价值 / Applications】
ProVQ可直接应用于多模态大语言模型和扩散合成系统的token化模块，提升视觉生成质量；在科学计算领域，该方法为蛋白质结构预测与生成提供了更鲁棒的表示学习工具，具有推动AI for Science发展的潜力。
