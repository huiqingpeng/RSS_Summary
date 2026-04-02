---
title: "Is One Token All It Takes? Graph Pooling Tokens for LLM-based GraphQA"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00342"
published: "2026-04-02"
summarized: "2026-04-03T07:20:44.211154"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究针对图问答（GraphQA）中图神经网络（GNN）与大语言模型（LLM）融合时的信息瓶颈问题，提出通过多token池化和全局注意力机制两种正交策略来增强图到LLM接口的带宽和语义质量。研究发现，虽然池化操作在软提示调优中引入显著不稳定性，但低秩适配（LoRA）能有效稳定特定的层次化投影方法（如虚拟节点池化和剪枝方法），使压缩表示达到与全图基线相当的性能（WebQSP上~73% Hit@1）。此外，作者将FandE评分适配到生成式GraphQA领域，揭示现有基准存在表征饱和问题，即目标答案往往与孤立节点特征高度相关。

【方法概述 / Method】

论文系统评估了多种层次化剪枝和基于聚类的池化算子（包括Top-k、SAGPool、DiffPool、MinCutPool和虚拟节点池化VNPool），将图数据投影为多个可学习token；同时采用全局注意力机制的图Transformer作为编码器，并引入LoRA进行参数高效微调以稳定训练过程。作者还从概念上证明，配备VNPool的图Transformer在结构上等价于单层Perceiver IO编码器。

【实验结果 / Results】

实验表明，多token池化结合LoRA稳定后，压缩表示可达到全图基线相当的性能，在WebQSP数据集上取得约73%的Hit@1准确率；然而，密集聚类算子（如DiffPool、MinCutPool）仍面临优化挑战。通过FandE评分分析发现，GraphQA基准测试存在表征饱和现象，节点特征与答案相关性过高而边结构信息利用不足。

【应用价值 / Applications】

该研究为高效图-语言模型融合提供了实用方案，使大规模图能以紧凑的多token形式输入LLM，降低计算成本的同时保持问答性能，适用于知识图谱问答、智能客服等需要处理复杂图结构的场景；同时提出的FandE评分适配方法为评估生成式图问答模型的特征-边利用平衡提供了新工具。
