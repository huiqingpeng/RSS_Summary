---
title: "MetaKube: An Experience-Aware LLM Framework for Kubernetes Failure Diagnosis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23580"
published: "2026-03-26"
summarized: "2026-03-27T07:15:44.744055"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MetaKube，首个能够从运维经验中持续学习的Kubernetes故障诊断LLM框架。该框架通过三项创新——情景模式记忆网络（EPMN）、元认知控制器和领域特化模型KubeLLM——解决了现有系统依赖静态知识、无法从历史解决方案中改进的局限。在1,873个真实场景评估中，MetaKube将Qwen3-8B的诊断准确率从50.9分提升至90.5分，接近GPT-4.1水平，同时确保完全的数据隐私保护。

【方法概述 / Method】
MetaKube采用三层架构设计：（1）EPMN模块从历史解决方案中抽象诊断模式，提供置信度校准的检索机制，支持快速模式匹配与引导式因果探索；（2）元认知控制器根据问题熟悉度动态切换直觉型与分析型推理路径，优化速度与深度的权衡；（3）基于7,000样本Kubernetes故障解决数据集进行领域后训练，得到本地可部署的8B参数模型KubeLLM。

【实验结果 / Results】
实验表明，EPMN的经验学习机制单独贡献15.3%的性能提升，且系统随运维知识积累呈现持续进步趋势。MetaKube使轻量级开源模型（Qwen3-8B）达到接近闭源大模型（GPT-4.1）的诊断水平，在完全本地部署条件下实现了隐私与性能的双重保障。

【应用价值 / Applications】
该研究为云原生运维场景提供了隐私可控、经验可累积的智能诊断方案，特别适用于金融、政务等对数据安全敏感的企业级Kubernetes集群管理。框架的经验学习机制可推广至其他复杂IT系统的故障诊断领域，推动LLM从通用问答向专业化、持续进化的运维助手转型。
