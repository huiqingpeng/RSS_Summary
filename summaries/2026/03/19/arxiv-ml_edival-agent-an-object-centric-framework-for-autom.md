---
title: "EdiVal-Agent: An Object-Centric Framework for Automated, Fine-Grained Evaluation of Multi-Turn Editing"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.13399"
published: "2026-03-19"
summarized: "2026-03-19T14:17:06.794060"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了EdiVal-Agent，一种以对象为中心的自动化细粒度评估框架，用于解决基于指令的图像编辑中可靠评估的瓶颈问题。该框架通过将图像分解为语义对象并合成上下文感知的编辑指令，支持单轮和多轮编辑评估。作者还构建了EdiVal-Bench基准测试，涵盖9种指令类型和16种最先进的编辑模型，并证明该框架能够有效识别现有模型的失效模式。

【方法概述 / Method】
EdiVal采用对象为中心的视角，首先将输入图像分解为语义上有意义的对象，然后合成多样化的上下文感知编辑指令，并在多轮过程中动态更新对象池。基于此流程，设计了三个评估指标：EdiVal-IF（结合开放词汇检测器进行符号检查与VLM语义验证）、EdiVal-CC（利用演进的对象池计算未改变对象和背景的语义相似度）以及EdiVal-VQ（使用人类偏好模型量化整体视觉质量变化）。

【实验结果 / Results】
作者构建了EdiVal-Bench多轮编辑基准，涵盖9种指令类型和16种涵盖上下文学习、流匹配和扩散范式的最先进编辑模型。实验表明，该框架能够有效识别现有编辑模型的失效模式，为下一代编辑模型的发展提供指导。

【应用价值 / Applications】
EdiVal-Agent可广泛应用于图像编辑模型的自动评估与优化，特别适用于需要多轮交互式编辑的场景，如智能图像设计工具和创意内容生成平台。该框架的细粒度评估能力有助于开发者精准定位模型缺陷，推动更可靠、更符合人类偏好的编辑模型研发。
