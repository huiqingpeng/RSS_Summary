---
title: "AVO: Agentic Variation Operators for Autonomous Evolutionary Search"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24517"
published: "2026-03-27"
summarized: "2026-03-28T07:11:08.388771"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了**Agentic Variation Operators (AVO)**，一类全新的进化变异算子，用自主编程智能体替代了传统进化搜索中固定的变异、交叉和手工设计启发式规则。AVO 将语言模型从受限的候选生成器提升为自导向的智能体循环，能够利用当前谱系信息、领域知识库和执行反馈来提出、修复、评判和验证代码修改。在 NVIDIA Blackwell (B200) GPU 上对多头注意力算子进行 7 天连续自主进化，AVO 发现的内核在多个配置下比 cuDNN 快 3.5%、比 FlashAttention-4 快 10.5%；且仅需 30 分钟额外自适应即可迁移到分组查询注意力，获得 7.0% 和 9.3% 的性能提升。

---

【方法概述 / Method】

AVO 的核心创新是将**大语言模型从"候选生成器"重新定位为"变异算子"本身**——构建一个自包含的智能体循环，该循环可主动查询当前进化谱系、检索领域特定知识库，并根据代码执行反馈进行多轮迭代（提出编辑→修复错误→批判评估→验证正确性）。这种设计突破了传统"LLM-in-the-loop"流水线中语言模型被限制在固定步骤内的局限，使变异过程具备完全的自主性和适应性。

---

【实验结果 / Results】

在 NVIDIA 最新 Blackwell B200 GPU 上，AVO 对**多头注意力（multi-head attention）**进行 7 天自主进化，发现的内核在评估配置中最高比 NVIDIA cuDNN 快 **3.5%**、比 FlashAttention-4 快 **10.5%**。迁移至**分组查询注意力（grouped-query attention）**时，仅 30 分钟自适应进化即实现最高 **7.0%**（vs cuDNN）和 **9.3%**（vs FlashAttention-4）的性能增益，展现出优秀的跨任务迁移能力。

---

【应用价值 / Applications】

AVO 为**高性能计算内核的自动化优化**开辟了新路径，特别适用于 AI 系统中计算密集型的核心算子（如注意力机制），能够在最新硬件架构上持续发现超越人类专家手工调优的微观架构优化。该方法可推广至其他需要极致性能优化的领域（如科学计算、图形渲染），显著降低对领域专家经验的依赖，加速硬件-软件协同设计周期。
