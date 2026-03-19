---
title: "Deploying Semantic ID-based Generative Retrieval for Large-Scale Podcast Discovery at Spotify"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17540"
published: "2026-03-19"
summarized: "2026-03-19T13:13:11.314022"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了GLIDE，一个部署在Spotify的大规模生成式播客推荐系统。该系统将推荐任务转化为基于Semantic ID的指令跟随生成任务，结合近期收听历史和轻量级用户上下文，并通过软提示注入长期用户嵌入以捕获稳定偏好。大规模在线A/B测试表明，GLIDE在非习惯性播客流媒体收听上提升5.4%，新节目发现率提升14.3%，同时满足生产环境的成本和延迟约束。

【方法概述 / Method】
GLIDE采用基于Semantic ID的生成式检索框架，将播客目录离散化为语义标识符，使模型能够在大型库存上进行有根据的生成。模型以近期收听历史为条件，将长期用户嵌入作为软提示（soft prompts）注入，在严格的推理延迟限制下实现个性化推荐。

【实验结果 / Results】
评估涵盖离线检索指标、人工判断和LLM-based评估，并通过大规模在线A/B测试验证。结果显示，GLIDE在Spotify首页非习惯性播客流媒体提升高达5.4%，新节目发现率提升高达14.3%，同时满足生产成本和延迟要求。

【应用价值 / Applications】
该研究直接应用于Spotify的播客发现场景，解决了传统推荐系统难以兼顾用户稳定偏好与动态探索意图的问题。GLIDE的生成式框架可扩展至其他大规模内容发现平台，为在延迟敏感的生产环境中部署LLM驱动的推荐系统提供了可行方案。
