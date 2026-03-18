---
title: "VisTIRA: Closing the Image-Text Modality Gap in Visual Math Reasoning via Structured Tool Integration"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.14440"
published: "2026-03-18"
summarized: "2026-03-18T17:14:00.579696"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文揭示了视觉-语言模型（VLMs）在数学推理中存在显著的"模态差距"现象：同一道数学题以图像形式呈现时的准确率明显低于纯文本形式，这源于模型在读取密集公式、版面布局和混合符号-图表上下文时的复合性失败。作者提出了VisTIRA框架，通过结构化工具集成和迭代式问题分解来缩小这一差距，并构建了LaTeX转换流程和合成工具使用轨迹数据集用于模型微调。研究发现模态差距的严重程度与模型规模呈负相关，且结构化推理与OCR定位是互补的改进策略。

【方法概述 / Method】

VisTIRA采用工具集成的推理代理架构，将视觉数学问题迭代分解为自然语言推理链和可执行的Python代码步骤。研究还开发了基于LaTeX的自动化流程，将文本形式的思维链数学语料库（如NuminaMath）转换为图像版本，并从真实作业图像数据集SnapAsk中生成大规模合成工具使用轨迹用于监督微调。

【实验结果 / Results】

实验表明工具集成监督能显著提升基于图像的推理能力，而OCR定位对较小模型的模态差距缩小效果更明显，但该优势随模型规模增大而减弱。核心发现是模态差距的严重程度与模型规模呈反比关系，即 larger models 受模态差距影响更小。

【应用价值 / Applications】

该研究为教育科技领域提供了改进视觉数学问题求解的技术路径，特别适用于拍照搜题、在线作业辅导等场景。VisTIRA框架可集成至智能教育系统中，帮助学生通过多模态交互获得逐步推理指导，同时为开发更具鲁棒性的视觉数学推理模型提供了数据构建和训练方法论。
