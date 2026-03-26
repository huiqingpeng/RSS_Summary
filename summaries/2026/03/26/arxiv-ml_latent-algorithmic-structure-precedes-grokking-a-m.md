---
title: "Latent Algorithmic Structure Precedes Grokking: A Mechanistic Study of ReLU MLPs on Modular Arithmetic"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23784"
published: "2026-03-26"
summarized: "2026-03-27T07:17:07.997429"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了神经网络在模运算任务上的"grokking"现象（验证准确率远晚于训练数据记忆后突然上升）。研究发现，与先前认为的神经网络学习正弦输入权重不同，ReLU MLP实际上学习的是近二进制的方波输入权重，且输出权重的傅里叶相位满足φ_out = φ_a + φ_b的相位和关系。关键发现是：即使模型在噪声数据上训练且未能实现grokking，这种算法结构已经存在，表明grokking并非发现正确算法，而是逐步锐化记忆阶段已编码的算法结构。

【方法概述 / Method】
作者通过离散傅里叶变换（DFT）从真实模型权重中提取每个神经元的频率和相位，构建了一个理想化的MLP模型：将输入权重替换为完美二进制方波，输出权重替换为余弦函数。该理想化模型使用从噪声数据训练的失败模型中提取的参数，仍能实现高准确率，从而验证算法结构在记忆阶段已 latent 存在。

【实验结果 / Results】
理想化MLP在从噪声数据训练的模型（本身仅0.23%准确率）中提取频率和相位后，达到了95.5%的准确率。这表明grokking过程中，输入权重逐步二值化为更清晰的方波，输出权重逐步对齐，最终使泛化成为可能，而非从头学习新算法。

【应用价值 / Applications】
该研究深化了对神经网络泛化机制的理解，揭示了"顿悟式学习"（grokking）的本质是算法结构的逐步锐化而非突然发现。这一发现对理解深度学习模型的内部工作机制、改进训练策略（如早停或正则化设计）以及开发更可解释的AI系统具有重要指导意义。
