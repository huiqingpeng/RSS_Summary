---
title: "Dropout Robustness and Cognitive Profiling of Transformer Models via Stochastic Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17811"
published: "2026-03-19"
summarized: "2026-03-19T12:16:45.381060"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究首次系统评估了19种Transformer模型在推理阶段使用蒙特卡洛Dropout（MC Dropout）时的行为表现，发现53%的模型在基线MC Dropout下出现严重精度下降，且Dropout鲁棒性与模型规模无相关性。研究还提出了认知分解框架，将模型性能解耦为记忆和推理两个组件，揭示了84%的模型存在记忆偏向性，以及高Dropout率对记忆任务的破坏性远大于推理任务（-27% vs -1%）的不对称效应。

【方法概述 / Method】
研究采用MC Dropout方法，对每个样本进行100次随机前向传播，通过单次运行精度的标准差量化预测稳定性；同时构建了认知分解框架，将任务性能分离为记忆组件（依赖稳定表征）和推理组件（依赖抽象能力），并在五种Dropout配置下对1,000个样本进行了95组独立评估。

【实验结果 / Results】
实验发现：小型模型展现出完美的预测稳定性，中型模型整体性能最佳但波动性显著，大型模型在记忆任务上表现突出；任务专用模型在MC Dropout下精度损失高达24个百分点，表明其不适合不确定性量化应用；高Dropout率对记忆准确率的损害（降低27个百分点）远超推理准确率（仅降低1个百分点）。

【应用价值 / Applications】
该研究为不确定性感知应用（如医疗诊断、自动驾驶等高风险决策场景）中的模型选择提供了可操作的指导，帮助从业者识别哪些架构适合部署MC Dropout进行可靠的不确定性估计；认知分解框架还可用于针对性改进模型设计，例如在需要稳定记忆的场景中避免高Dropout配置。
