---
title: "FluxEDA: A Unified Execution Infrastructure for Stateful Agentic EDA"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.25243"
published: "2026-03-27"
summarized: "2026-03-28T07:07:51.352210"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了FluxEDA，一个面向智能体EDA（Agentic EDA）的统一有状态执行基础设施，解决了现有大语言模型与EDA工具集成中仅依赖脚本级或请求级交互、难以保留工具状态的问题。FluxEDA通过引入基于网关的托管执行接口和持久化后端实例，使上层智能体和可编程客户端能够在保留运行时状态的情况下与异构EDA工具交互。该框架在商业后端案例中的评估表明，其支持多步分析优化、状态复用、回滚和协调迭代执行，为智能体辅助EDA自动化奠定了实用基础。

【方法概述 / Method】
FluxEDA采用网关式架构设计，提供结构化的请求-响应处理机制，并维护持久的EDA工具后端实例而非隔离的shell调用。该基础设施通过状态化管理实现上层智能体与底层异构EDA工具之间的有状态交互，支持跨会话的状态保持与恢复。

【实验结果 / Results】
研究通过两个代表性商业后端案例进行评估：自动化布线后时序ECO和标准单元子库优化。实验结果表明FluxEDA能够在真实工具上下文中支持多步分析与优化，实现了状态复用、回滚机制以及协调式迭代执行，验证了有状态基础设施层在复杂EDA工作流中的可行性。

【应用价值 / Applications】
FluxEDA为芯片设计中的智能体自动化提供了生产级就绪的基础设施支撑，特别适用于需要多轮迭代优化的复杂EDA任务（如时序收敛、功耗优化等）。该框架可加速大语言模型与自主智能体在工业级EDA流程中的落地应用，降低智能体开发门槛并提升优化效率。
