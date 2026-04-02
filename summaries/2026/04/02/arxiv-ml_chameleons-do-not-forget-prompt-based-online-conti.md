---
title: "Chameleons do not Forget: Prompt-Based Online Continual Learning for Next Activity Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00653"
published: "2026-04-02"
summarized: "2026-04-03T07:23:23.477701"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对预测性流程监控（PPM）中的下一活动预测任务，提出了一种名为CNAPwP（Continual Next Activity Prediction with Prompts）的新方法，该方法将DualPrompt算法适配到在线持续学习场景，以缓解概念漂移环境下的灾难性遗忘问题。研究引入了新的周期性概念漂移数据集和任务特定遗忘度量指标，用于衡量任务首次出现与后续出现之间的预测准确率差距。在三个合成数据集和两个真实世界数据集上的实验表明，CNAPwP相比五种基线方法达到了SOTA或具有竞争力的性能。

【方法概述 / Method】
CNAPwP基于DualPrompt框架，采用提示学习（prompt-based learning）机制，通过引入可学习的提示参数来引导模型适应新任务，同时保持对旧任务的记忆。该方法将提示分为通用提示（general prompts）和任务特定提示（task-specific prompts），使模型能够在线识别任务身份并动态选择合适的提示进行推理，从而实现无需显式任务边界信息的持续学习。

【实验结果 / Results】
实验在包含周期性概念漂移的多种设置下进行，涵盖三个合成数据集和两个真实世界数据集。结果表明CNAPwP在准确率和适应性方面显著优于五种对比基线，达到SOTA或具有竞争力的性能水平。特别是，新提出的任务特定遗忘度量显示该方法有效缩小了任务首次出现与后续重现之间的预测准确率差距，验证了其在缓解灾难性遗忘方面的有效性。

【应用价值 / Applications】
该方法适用于动态变化的业务流程监控场景，如医疗流程管理、供应链物流、客户服务工单处理等存在概念漂移和周期性模式变化的实际环境。CNAPwP能够在不重新训练整个模型的情况下快速适应新流程变化，同时保持历史知识的有效利用，为需要实时决策支持的预测性流程监控系统提供了实用的技术方案。
