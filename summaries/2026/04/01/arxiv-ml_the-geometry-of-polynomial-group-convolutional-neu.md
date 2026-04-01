---
title: "The Geometry of Polynomial Group Convolutional Neural Networks"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29566"
published: "2026-04-01"
summarized: "2026-04-02T07:19:15.974912"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了任意有限群G上的多项式群卷积神经网络（PGCNNs），提出了基于分级群代数的全新数学框架。该框架导出了基于Hadamard积和Kronecker积的两种自然参数化方法，二者通过线性映射相关联。研究计算了相关神经流形的维度，证明其仅依赖于网络层数和群的大小，并描述了Kronecker参数化的一般纤维结构，同时对Hadamard参数化提出了相应猜想。

【方法概述 / Method】

作者运用分级群代数（graded group algebras）的语言构建PGCNNs的数学框架，将网络架构表示为代数结构。通过该框架自然地导出两种参数化方式：Hadamard积形式和Kronecker积形式，并建立二者之间的线性映射关系。

【实验结果 / Results】

研究严格证明了神经流形的维度仅由网络层数和群的大小决定，与群的具体结构无关。对于Kronecker参数化，完整描述了其在正则群作用和重缩放下的一般纤维；对于Hadamard参数化，通过小群和浅层网络的显式计算验证了所提出的猜想。

【应用价值 / Applications】

该研究为群等变神经网络提供了严格的数学理论基础，有助于理解这类网络的表达能力边界和优化景观特性。研究成果可指导具有对称性约束的深度学习架构设计，在分子性质预测、物理系统模拟等具有内在群对称性的科学计算领域具有潜在应用价值。
