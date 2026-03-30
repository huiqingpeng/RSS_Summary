---
title: "Adversarial-Robust Multivariate Time-Series Anomaly Detection via Joint Information Retention"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25956"
published: "2026-03-30"
summarized: "2026-03-31T07:20:15.488251"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了ARTA（Adversarially Robust multivariate Time-series Anomaly detection via joint information retention），一种通过对抗训练提升多变量时间序列异常检测（TSAD）鲁棒性的联合训练框架。该框架采用min-max优化目标，同时训练异常检测器和稀疏约束掩码生成器，使检测器对结构化扰动保持稳定。在TSB-AD基准上的实验表明，ARTA在多样化数据集上持续提升检测性能，并在噪声水平增加时展现出比现有方法更优雅的退化特性。

【方法概述 / Method】
ARTA采用对抗式联合训练策略，包含两个核心组件：一个异常检测器和一个稀疏约束的掩码生成器。生成器通过识别最小化的任务相关时间扰动来最大化检测器的异常分数，而检测器则针对这些结构化扰动进行优化以保持稳定性。该min-max优化过程迫使检测器依赖分布式且稳定的时间模式，而非脆弱的局部伪影。

【实验结果 / Results】
在TSB-AD基准数据集上的广泛实验表明，ARTA在多样化的真实数据集上 consistently 提升了异常检测性能。与最先进基线相比，ARTA在噪声水平逐渐升高时表现出显著更优的鲁棒性，实现了更优雅的性能退化曲线，同时生成的掩码可作为检测器决策的可解释性信号。

【应用价值 / Applications】
ARTA可广泛应用于关键基础设施监控（如工业设备、数据中心）、金融交易异常检测和网络安全入侵检测等对鲁棒性要求高的场景。该方法不仅能提升复杂系统在噪声环境下的可靠性，还能通过掩码解释性增强模型可信度，帮助运维人员理解检测决策的敏感区域。
