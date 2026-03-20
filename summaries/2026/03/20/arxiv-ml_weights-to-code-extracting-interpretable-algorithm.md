---
title: "Weights to Code: Extracting Interpretable Algorithms from the Discrete Transformer"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.05770"
published: "2026-03-20"
summarized: "2026-03-20T14:09:30.451156"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出**Discrete Transformer**，一种专为弥合连续表示与离散符号逻辑之间鸿沟而设计的新型架构，旨在解决从Transformer中提取可解释算法的核心障碍——表示纠缠（representation entanglement）。通过**温度退火采样（temperature-annealed sampling）**注入离散性，该框架结合假设检验与符号回归，成功提取出人类可读的程序。实验表明，Discrete Transformer在性能上可与RNN方法媲美，同时将可解释性扩展到连续变量域，且退火动态呈现出清晰的"探索-利用"过渡特征，为无需演示样本的算法发现提供了稳健框架。

---

【方法概述 / Method】

论文核心创新在于通过**温度退火机制**逐步降低采样温度，使模型表示从连续平滑过渡到离散状态，从而规避传统Transformer中特征叠加导致的纠缠问题。在此离散化基础上，结合**假设检验**筛选显著特征与**符号回归**合成数学表达式，实现从模型权重到可执行代码的自动转换。此外，架构设计引入了可控的归纳偏置（inductive biases），允许对合成程序的结构进行细粒度调控。

---

【实验结果 / Results】

Discrete Transformer在算法任务上取得了与RNN基线相当的学习性能，同时突破了RNN仅适用于离散变量的限制，成功处理**连续变量域**的算法学习。温度退火过程展现出明确的阶段性行为：初期高温阶段侧重全局探索，后期低温阶段收敛至稳定离散解，形成可解释的"探索-利用"相变。消融实验进一步证实，架构层面的归纳偏置能够有效引导生成程序的结构特性（如复杂度、递归深度等）。

---

【应用价值 / Applications】

该研究为**自动化算法发现**开辟了无需人工编写代码或提供演示样本的新路径，可直接从神经网络权重中恢复可解释的程序实现。在**Transformer可解释性**领域，提供了一种将黑箱模型转化为透明符号规则的系统方法，有助于审计和验证AI系统的决策逻辑。潜在应用包括教育辅助（自动生成算法教学示例）、科学计算（发现新型数值算法）以及安全关键系统的模型验证等场景。
