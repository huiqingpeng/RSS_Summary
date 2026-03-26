---
title: "From Imperative to Declarative: Towards LLM-friendly OS Interfaces for Boosted Computer-Use Agents"
source: "arXiv Embedded Systems"
url: "https://arxiv.org/abs/2510.04607"
published: "2026-03-26"
summarized: "2026-03-27T07:12:29.356533"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种面向大语言模型（LLM）的声明式操作系统接口——声明式模型接口（DMI），以解决现有计算机使用智能体（CUAs）在操作传统图形用户界面（GUI）时面临的低效问题。DMI将GUI抽象为三个声明式原语（access、state、observation），实现策略与机制的分离，使LLM专注于高层语义规划而非底层交互细节。实验表明，DMI在Microsoft Office套件上可将任务成功率提升67%，交互步骤减少43.5%，且超过61%的成功任务仅需单次LLM调用即可完成。

【方法概述 / Method】
DMI的核心设计思想是策略-机制分离：LLM负责高层决策（策略），DMI负责底层导航与交互执行（机制）。该方法无需修改应用程序源代码或依赖API，通过将现有GUI转换为声明式原语，为LLM智能体提供更友好的操作系统接口。这种抽象层使智能体能够以声明式方式指定"想要什么"而非"如何一步步操作"。

【实验结果 / Results】
在Windows平台的Microsoft Office套件（Word、PowerPoint、Excel）评估中，DMI集成到领先的基于GUI的智能体基线后，任务成功率相对提升67%，交互步骤减少43.5%。尤为突出的是，超过61%的成功任务可通过单次LLM调用完成，显著降低了对多轮推理的依赖和累积错误风险。

【应用价值 / Applications】
该研究为自动化办公、软件测试、无障碍辅助技术等场景提供了更高效的智能体交互范式，使LLM能够更可靠地操控传统桌面应用程序。DMI的通用设计原则可扩展至其他GUI密集型领域，为构建真正实用的计算机使用智能体铺平道路，同时降低了对应用程序专用API的依赖门槛。
