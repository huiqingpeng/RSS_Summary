---
title: "TerraScope: Pixel-Grounded Visual Reasoning for Earth Observation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19039"
published: "2026-03-20"
summarized: "2026-03-20T15:18:36.033286"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了 TerraScope，一种面向地球观测的统一视觉语言模型，旨在解决现有 VLMs 在像素级空间推理任务中的不足。该模型具备模态灵活推理（支持光学/SAR 单模态及自适应多模态融合）和多时序推理（整合时间序列进行变化分析）两大核心能力。研究还构建了包含 100 万样本的 Terra-CoT 数据集（嵌入像素级掩码的推理链）和 TerraScope-Bench 基准测试（涵盖 6 个子任务，同时评估答案准确性和掩码质量）。实验表明，TerraScope 在像素级地理空间推理任务上显著优于现有 VLMs，并提供可解释的视觉证据。

【方法概述 / Method】
TerraScope 采用统一的视觉语言架构，通过自适应融合机制处理光学与 SAR 两种模态的输入，并引入时序建模模块实现多时间点的变化分析。模型在训练过程中利用 Terra-CoT 数据集中的像素级掩码嵌入推理链，学习将高层语义推理与精确像素定位相结合。

【实验结果 / Results】
TerraScope 在 TerraScope-Bench 的六个子任务上均显著超越现有视觉语言模型，在答案准确率和掩码质量两项指标上取得领先。实验验证了模型在单模态、多模态融合及时序推理场景下的有效性，证明其能够生成高质量的像素级分割掩码作为可解释的视觉证据。

【应用价值 / Applications】
该研究可直接应用于土地利用变化监测、灾害评估、城市规划等需要精确定位和时序分析的地球观测任务。TerraScope 提供的像素级可解释输出有助于提升遥感图像分析的透明度和可信度，为环境监测、农业管理和应急响应等领域提供更可靠的决策支持。
