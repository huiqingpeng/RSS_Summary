---
title: "TTQ: Activation-Aware Test-Time Quantization to Accelerate LLM Inference On The Fly"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19296"
published: "2026-03-23"
summarized: "2026-03-24T07:15:39.889249"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了测试时量化（Test-Time Quantization, TTQ）框架，用于在推理过程中动态压缩大型语言模型，以解决传统激活感知压缩方法依赖校准数据而导致的领域迁移问题。TTQ通过高效的在线校准机制，能够针对每个输入提示即时进行激活感知量化，无需重新训练即可适应不同的下游任务，同时实现推理加速。实验表明，TTQ在量化性能上优于现有最先进的方法。

【方法概述 / Method】
TTQ采用在线校准策略，在推理时根据当前输入动态计算量化参数，而非依赖预收集的校准数据集。该方法通过激活感知的即时量化，使模型能够针对每个新提示自适应地调整压缩策略，从而实现真正的"即时"（on-the-fly）模型压缩。

【实验结果 / Results】
论文通过多项实验验证了TTQ的有效性，结果显示其在量化性能上超越了当前最先进的基线方法。具体而言，TTQ能够在保持模型质量的同时实现推理速度提升，且无需针对特定下游任务进行离线校准。

【应用价值 / Applications】
TTQ适用于需要快速部署大语言模型且面临多样化下游任务的场景，如云端推理服务、边缘设备部署和实时交互应用。该框架消除了对预收集校准数据的依赖，显著提升了模型在新领域或动态环境中的适应性和实用性。
