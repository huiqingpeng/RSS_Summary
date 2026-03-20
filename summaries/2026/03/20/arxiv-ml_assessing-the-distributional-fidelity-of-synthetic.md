---
title: "Assessing the Distributional Fidelity of Synthetic Chest X-rays using the Embedded Characteristic Score"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2501.00744"
published: "2026-03-20"
summarized: "2026-03-20T14:14:35.303243"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种名为嵌入特征分数（Embedded Characteristic Score, ECS）的新方法，用于评估合成胸部X光片（CXR）与真实患者CXR图像之间的分布保真度。该方法通过特征嵌入的特征函数变换来比较合成样本与真实样本，能够敏感地检测到分布的高阶矩和尾部差异，而这些方面常被常用的Fréchet Inception Distance（FID）等评估指标所忽略。研究通过模拟实验和标准基准成像数据集验证了ECS的性能，并发现使用ECS评估合成CXR图像时能够揭示与临床相关的分布差异，强调了在高风险决策中可靠评估合成数据的重要性。

【方法概述 / Method】

ECS方法的核心是对特征嵌入应用特征函数变换，通过分析特征函数在原点附近的行为来捕捉分布的细微差异。该方法具有灵活性，其嵌入选择可根据具体的临床或科学背景进行定制，并建立了基于简单重采样程序的校准策略以确保评估的可靠性。

【实验结果 / Results】

研究通过模拟实验和标准基准成像数据集将ECS与FID进行了对比，结果表明ECS能够有效识别FID无法检测到的分布差异。在合成CXR图像的评估中，ECS成功揭示了与临床相关的分布不一致性，证明了其在医学影像合成数据质量评估中的优越性。

【应用价值 / Applications】

ECS方法在医学影像领域具有重要的实际应用价值，特别是在需要严格隐私保护的场景下，可用于可靠评估合成CXR图像的质量，确保其适用于数据共享和机器学习模型训练等下游任务。该方法还可推广至其他高风险医学成像应用，为合成数据的临床安全性和有效性提供质量保证。
