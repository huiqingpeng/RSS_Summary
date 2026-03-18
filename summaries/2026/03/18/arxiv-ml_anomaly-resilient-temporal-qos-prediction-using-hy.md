---
title: "Anomaly Resilient Temporal QoS Prediction using Hypergraph Convoluted Transformer Network"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2410.17762"
published: "2026-03-18"
summarized: "2026-03-18T16:16:45.208603"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种实时、可信感知的时间QoS预测框架，通过端到端深度架构Hypergraph Convoluted Transformer Network（HCTN）解决现有方法面临的数据稀疏性、冷启动问题以及对异常值和"灰羊"用户/服务敏感等挑战。HCTN在WSDREAM-2大规模数据集上实现了响应时间和吞吐量的最先进性能，证明了其在处理网络不确定性和用户偏好动态变化方面的有效性。

【方法概述 / Method】
HCTN结合了超图结构与超边图卷积，通过捕获复杂的高阶相关性来解决高稀疏性问题；同时采用Transformer网络，利用多头注意力机制配合并行1D卷积层和全连接密集块，捕获细粒度和粗粒度的动态模式。此外，该方法还包含针对"灰羊"用户和服务的稀疏弹性检测方案，并采用对异常值具有鲁棒性的损失函数进行训练。

【实验结果 / Results】
HCTN在WSDREAM-2大规模数据集上的响应时间和吞吐量预测任务中达到了最先进的性能水平，验证了其在处理高稀疏数据、异常值和"灰羊"用户/服务方面的有效性。具体量化指标虽未在摘要中详述，但结果表明该方法显著优于现有基线方法。

【应用价值 / Applications】
该研究可应用于云服务推荐系统、自适应服务选择和动态资源调度等场景，帮助服务提供商在复杂网络环境下实现精确的实时性能预测。其异常值鲁棒性和对"灰羊"用户的处理能力使其特别适用于大规模、异构的服务生态系统，能够提升用户体验并优化服务部署决策。
