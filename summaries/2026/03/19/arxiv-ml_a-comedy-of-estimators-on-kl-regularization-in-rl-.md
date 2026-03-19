---
title: "A Comedy of Estimators: On KL Regularization in RL Training of LLMs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2512.21852"
published: "2026-03-19"
summarized: "2026-03-19T14:10:40.743013"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文系统研究了大型语言模型（LLM）强化学习（RL）训练中KL散度正则化的多种估计器配置。作者分析了不同KL估计器设计选择对梯度偏差的影响，发现当前广泛采用的实践存在梯度偏差问题，导致目标函数与其实现不一致。通过在Qwen2.5-7B、Llama-3.1-8B-Instruct和Qwen3-4B-Instruct-2507模型上的实验，研究表明无偏梯度估计器配置在分布内和分布外任务上均表现更优，而偏差梯度估计器会导致训练不稳定；此外，KL正则化有助于稳定异步设置下的离线RL训练。

【方法概述 / Method】

本研究从理论上分析了多种KL散度估计器配置（包括前向/反向KL、不同采样策略和梯度估计方式）的梯度特性，揭示了设计选择如何塑造梯度偏差。作者通过RL微调实验，系统比较了不同估计器配置在实际训练中的表现，涵盖同步（on-policy）和异步（off-policy）两种训练设置。

【实验结果 / Results】

实验结果表明：在同步（on-policy）设置中，具有偏差梯度的估计器配置会导致训练不稳定，而无偏梯度估计器在分布内和分布外任务上均取得更好性能；在异步（off-policy）设置中，KL正则化能够有效稳定训练过程，缓解异步设置带来的不稳定性问题。

【应用价值 / Applications】

本研究为LLM RL训练中的KL正则化实现提供了系统性指导，帮助研究者和实践者选择正确的估计器配置以避免训练不稳定和性能下降。其发现可直接应用于开源RLHF/RL训练框架的改进，提升模型推理能力和泛化性能，特别是在需要大规模分布式异步训练的生产环境中。
