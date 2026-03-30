---
title: "AcTTA: Rethinking Test-Time Adaptation via Dynamic Activation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26096"
published: "2026-03-30"
summarized: "2026-03-31T07:21:32.998190"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了AcTTA，一种基于动态激活的测试时自适应框架，突破了现有方法仅关注归一化层仿射调制的局限。通过将传统激活函数（如ReLU、GELU）重新参数化为可学习形式，AcTTA能够在测试时动态调整激活阈值和梯度敏感性，无需修改网络权重或访问源数据。在CIFAR10-C、CIFAR100-C和ImageNet-C等分布偏移基准上，AcTTA consistently优于基于归一化的TTA方法，证明了激活自适应作为紧凑有效的域鲁棒学习新途径。

【方法概述 / Method】
AcTTA将传统激活函数转化为参数化形式，引入可学习的阈值偏移和梯度调制参数，使其响应特性能够根据输入分布动态调整。该方法在推理过程中仅更新激活函数的参数，保持网络主干权重冻结，同时无需存储源数据，实现了轻量级的在线自适应。

【实验结果 / Results】
AcTTA在多个标准损坏基准（CIFAR10-C、CIFAR100-C、ImageNet-C）上均取得优于现有归一化自适应方法的性能，展现出更强的鲁棒性和稳定性。实验表明，激活函数的自适应调整能够有效应对多样化的分布偏移，且方法简洁高效。

【应用价值 / Applications】
AcTTA适用于部署在边缘设备或云端、面临实时数据分布变化的深度学习模型，如自动驾驶感知系统、医学影像诊断和工业质检等场景。该方法为资源受限环境下的持续模型优化提供了新思路，有望降低模型维护成本并提升实际部署中的可靠性。
