---
title: "Interpreting the Synchronization Gap: The Hidden Mechanism Inside Diffusion Transformers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20987"
published: "2026-03-24"
summarized: "2026-03-25T07:17:15.535137"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究揭示了扩散变换器（DiTs）内部"同步间隙"（synchronization gap）的隐藏机制——即不同模式在逆向扩散过程的不同阶段"承诺"（commit）生成的时间层次结构。作者通过构建双轨迹联合嵌入的显式架构实现，结合线性化注意力差异分析，证明同步间隙是DiTs的内在架构特性，且严格定位于Transformer的最终层。研究还发现全局低频结构始终先于局部高频细节承诺，为DiTs如何消解生成歧义提供了机制性解释。

【方法概述 / Method】

作者设计了一种"副本耦合"（replica coupling）架构：将两条生成轨迹嵌入联合token序列，通过可变相位耦合强度g的对称交叉注意力门控进行调制。在此基础上，对注意力差异进行线性化分析，将副本交互机制分解为可解释组件，并基于空间路由边界（spatial routing bounds）建立理论预测框架。

【实验结果 / Results】

在预训练DiT-XL/2模型上的实证研究表明：（1）即使关闭外部耦合，同步间隙仍作为内在架构特性持续存在；（2）强耦合条件下间隙完全坍缩，与理论预测一致；（3）间隙具有严格的深度局域性，仅在Transformer最后几层急剧涌现；（4）生成过程遵循从全局低频到局部高频的承诺顺序。

【应用价值 / Applications】

该研究为理解和优化扩散模型提供了深层机制洞察：明确同步间隙的深度局域性可指导高效模型蒸馏与层剪枝策略；对"全局-局部"生成顺序的揭示有助于设计更可控的图像编辑和条件生成方法；副本耦合框架还可扩展至多模态生成任务，提升生成一致性与可控性。
