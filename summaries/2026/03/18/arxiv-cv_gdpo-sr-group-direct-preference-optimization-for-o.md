---
title: "GDPO-SR: Group Direct Preference Optimization for One-Step Generative Image Super-Resolution"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16769"
published: "2026-03-18"
summarized: "2026-03-18T18:20:29.763619"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种名为GDPO（Group Direct Preference Optimization）的新方法，将强化学习引入单步生成式图像超分辨率（ISR）模型训练。针对现有DPO方法需要离线生成正负样本对导致样本数量有限、以及GRPO方法仅计算整幅图像似然而忽略局部细节的问题，作者设计了融合GRPO组相对优势思想的GDPO策略，并结合噪声感知单步扩散模型和属性感知奖励函数，有效提升了单步生成ISR的性能。

【方法概述 / Method】
论文首先引入噪声感知单步扩散模型以生成多样化的ISR输出，并采用非等时间步策略解耦噪声添加与扩散过程的时间步以防止性能退化；随后提出GDPO策略，将GRPO的组相对优势计算原理融入DPO框架，对每个在线生成样本计算组相对优势进行模型优化；同时设计属性感知奖励函数，根据样本中平滑区域和纹理区域的统计特性动态评估得分。

【实验结果 / Results】
实验结果表明，GDPO能够有效提升单步生成ISR模型的性能，验证了所提噪声感知单步扩散模型、非等时间步策略、GDPO优化策略以及属性感知奖励函数各组件的有效性。

【应用价值 / Applications】
该研究为实时图像超分辨率应用提供了高效的单步生成解决方案，适用于需要快速高质图像增强的场景，如移动设备摄影、视频流处理和实时视觉系统等，同时所提出的GDPO方法可推广至其他需要结合局部细节评估的生成任务中。
