---
title: "RAMP: Reinforcement Adaptive Mixed Precision Quantization for Efficient On Device LLM Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17891"
published: "2026-03-19"
summarized: "2026-03-19T12:18:06.601174"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出RAMP（Reinforcement Adaptive Mixed Precision），一种基于离策略Soft Actor-Critic强化学习的训练后量化方法，用于学习逐层比特宽度分配以在全局比特预算约束下最小化困惑度。该方法通过11维嵌入（包含激活统计、权重属性和结构描述符）实现跨模型族和尺度的零样本迁移。配合提出的Scale Folding预处理技术（通过逐通道缩放和归一化层补偿将激活异常值迁移至权重），RAMP在Llama 2 7B上实现3.65有效比特下的5.54困惑度，较均匀4比特AWQ减小6%体积并提升1%-3%质量，且策略可零样本泛化至Llama 2 13B和Mistral 7B。

【方法概述 / Method】

RAMP采用离策略Soft Actor-Critic强化学习框架，策略网络以11维状态向量（激活统计、权重属性、结构描述符）为条件输出逐层比特宽度分配，价值网络评估量化质量。为稳定支持亚4比特量化，引入Scale Folding预处理技术：通过逐通道缩放因子将激活异常值迁移至权重，并对归一化层进行相应补偿。奖励函数采用质量优先设计，包含非对称惩罚项和预算悬崖机制以加速收敛。

【实验结果 / Results】

在Llama 2 7B上，RAMP达到3.68GB（3.65有效比特）和5.54困惑度，优于均匀4比特AWQ（3.90GB，5.60困惑度）和GPTQ，体积减少6%同时质量提升1%-3%。关键发现：仅在Llama 2 7B上训练的策略可零样本迁移至Llama 2 13B和Mistral 7B，且常优于目标特定训练，支持"量化敏感性主要由架构决定"的假设。HALO管道将分配导出至GGUF格式，在CPU/GPU/边缘设备上实现无内核修改推理，保留99.5%的FP16常识推理性能。

【应用价值 / Applications】

RAMP可直接部署于资源受限的边缘设备（手机、IoT设备）实现高效LLM推理，无需针对特定模型重新训练量化策略。GGUF格式导出支持llama.cpp等主流推理框架的即插即用，降低端侧AI部署门槛。该方法为不同架构LLM提供通用量化解决方案，有望加速大模型在消费级硬件上的普及应用。
