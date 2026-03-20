---
title: "Seeking Universal Shot Language Understanding Solutions"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18448"
published: "2026-03-20"
summarized: "2026-03-20T12:12:03.356607"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对电影镜头语言理解（Shot Language Understanding, SLU）这一具有挑战性但尚未充分探索的领域，提出了首个大规模综合训练与评估套件SLU-SUITE，包含49万条人工标注的问答对，覆盖33个任务和6个电影维度。研究从模型侧和数据侧两个视角揭示了视觉语言模型（VLMs）在SLU任务中的关键瓶颈与跨维度影响规律。基于这些发现，作者提出了两种互补的通用解决方案：UniShot（通用一体化模型）和AgentShots（专家集群系统），在领域内任务上超越专用集成模型，在领域外任务上领先商业VLM达22%。

【方法概述 / Method】

本研究构建了SLU-SUITE数据集，涵盖镜头构图、运动、时长、语义、情感和风格六大电影维度，通过系统性分析诊断VLM的模块瓶颈并量化任务间的跨维度影响。在此基础上，设计了两种解决方案：UniShot采用动态平衡数据混合策略训练单一通用模型；AgentShots则基于提示路由将查询分配给专门的维度专家模型集群，以最大化各维度的峰值性能。

【实验结果 / Results】

实验表明，UniShot和AgentShots在领域内任务上均优于任务特定的集成模型，且在领域外泛化任务上比领先的商业VLMs（如GPT-4V、Gemini等）提升22%。研究还验证了动态平衡采样对缓解多任务训练中的维度不平衡问题的有效性，以及提示路由机制在保持通用性的同时提升专业维度表现的能力。

【应用价值 / Applications】

该研究为电影工业、流媒体平台和视频内容分析提供了可扩展的自动化镜头理解工具，可应用于智能剪辑推荐、影片风格分析、内容审核及个性化推荐等场景。SLU-SUITE作为首个大规模开源SLU基准，也为计算机视觉与自然语言处理交叉领域的多模态理解研究提供了重要资源。
