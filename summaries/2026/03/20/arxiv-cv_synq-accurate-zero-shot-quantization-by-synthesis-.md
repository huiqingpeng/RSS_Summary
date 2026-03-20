---
title: "SynQ: Accurate Zero-shot Quantization by Synthesis-aware Fine-tuning"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18423"
published: "2026-03-20"
summarized: "2026-03-20T15:08:26.447625"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了SynQ（Synthesis-aware Fine-tuning for Zero-shot Quantization），一种针对零样本量化（ZSQ）的新型框架，旨在解决现有方法面临的三大挑战：合成数据噪声、基于偏离目标模式的预测以及错误硬标签的误导。SynQ通过低通滤波减少生成样本噪声，通过类激活图对齐提升量化模型精度，并利用软标签缓解困难样本的误导问题。大量实验表明，SynQ在零样本量化任务上达到了最先进的准确率。

【方法概述 / Method】
SynQ采用三阶段技术方案：首先利用低通滤波器对合成数据去噪，生成更干净的样本；其次通过最小化全精度模型与量化模型之间的类激活图（CAM）差异进行特征对齐训练；最后针对困难样本仅使用软标签进行蒸馏，避免错误硬标签的误导。

【实验结果 / Results】
SynQ在多个基准数据集和模型架构上取得了最先进的零样本量化性能，显著优于现有ZSQ方法；实验验证了低通滤波、CAM对齐和软标签策略各自的有效性，消融研究表明各组件对最终精度均有正向贡献。

【应用价值 / Applications】
该研究适用于隐私敏感或安全受限场景下的模型部署，如医疗影像、金融数据和专有工业模型等无法获取原始训练数据的领域；SynQ使边缘设备能够在无数据访问权限的情况下实现高精度模型量化，降低了神经网络在资源受限环境中的部署门槛。
