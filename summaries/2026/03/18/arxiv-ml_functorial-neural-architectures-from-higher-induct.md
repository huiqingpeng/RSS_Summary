---
title: "Functorial Neural Architectures from Higher Inductive Types"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16123"
published: "2026-03-18"
summarized: "2026-03-18T15:40:43.968977"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文揭示了神经网络在组合泛化（compositional generalization）上的系统性失败本质上是架构性的：组合泛化等价于解码器的函子性（functoriality）。作者提出从更高归纳类型（Higher Inductive Types, HIT）规范编译神经架构的方法，通过从目标空间路径广群到参数映射范畴的单子函子，将路径构造器转化为生成网络、复合转化为结构拼接、2-细胞转化为可学习的自然变换。研究证明了结构拼接组装的解码器是严格单子函子（天生具有组合性），而softmax自注意力对任何非平凡组合任务都不具备函子性，这些结果均在Cubical Agda中形式化验证。

【方法概述 / Method】

核心方法是建立从拓扑空间的路径广群（path groupoid）到参数映射范畴的单子函子，将HIT的代数结构编译为神经网络架构：路径构造器对应生成网络，路径复合对应网络的结构拼接（structural concatenation），而见证群关系的2-细胞则对应可学习的自然变换。这种编译过程保证了生成的解码器在构造上即满足函子性。

【实验结果 / Results】

在三个拓扑空间上的实验验证了完整层次结构：在环面（$\mathbb{Z}^2$）上，函子化解码器性能优于非函子化版本2-2.7倍；在双圆楔（$S^1 \vee S^1$，自由群$F_2$）上，A/B类型差距扩大至5.5-10倍；在克莱因瓶（$\mathbb{Z} \rtimes \mathbb{Z}$）上，可学习的2-细胞在涉及群关系的测试词上将误差差距缩小了46%。

【应用价值 / Applications】

该研究为需要严格组合泛化的领域（如程序合成、形式语言理解、结构化推理）提供了理论指导的架构设计原则，特别是通过HIT规范可直接编译得到具有组合性保证的神经网络，避免了传统架构在分布外组合上的失效；同时，函子性视角也为分析现有架构（如Transformer）的固有局限性提供了形式化工具。
