---
title: "Memori: A Persistent Memory Layer for Efficient, Context-Aware LLM Agents"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19935"
published: "2026-03-23"
summarized: "2026-03-24T07:23:30.893430"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了 Memori，一个与 LLM 无关的持久化记忆层，用于解决现有 LLM 智能体在多会话交互中面临的上下文感知问题。Memori 通过将非结构化对话转换为紧凑的语义三元组和对话摘要，实现了精确检索和连贯推理。在 LoCoMo 基准测试中，Memori 达到 81.95% 的准确率，同时每查询仅使用 1,294 个 token（约为完整上下文的 5%），显著降低了成本。研究表明，有效的智能体记忆应依赖结构化表示而非更大的上下文窗口。

【方法概述 / Method】
Memori 将记忆视为数据结构化问题，采用"Advanced Augmentation"流水线处理非结构化对话：首先提取语义三元组（主语-谓语-宾语）以捕捉关键事实关系，同时生成对话摘要以维护高层语义连贯性。该记忆层位于 API 层，可与任意 LLM 后端集成，避免厂商锁定。

【实验结果 / Results】
在 LoCoMo 长上下文多会话基准测试中，Memori 取得 81.95% 的准确率，超越现有记忆系统；每查询平均仅消耗 1,294 个 token，比竞争方法减少 67% 的 token 使用量，相比完整上下文方法节省超过 20 倍成本，同时保持或提升任务性能。

【应用价值 / Applications】
Memori 适用于需要长期记忆的客户服务机器人、个性化教育助手、医疗随访系统等多会话 LLM 应用场景。其 LLM 无关架构使企业可灵活切换底层模型而无需重构记忆系统，显著降低运营成本和延迟，为大规模部署上下文感知智能体提供了可扩展、经济高效的解决方案。
