---
title: "From Language to Action in Arabic: Reliable Structured Tool Calling via Data-Centric Fine-Tuning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16901"
published: "2026-03-19"
summarized: "2026-03-19T12:05:18.158481"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对阿拉伯语函数调用模型存在严重结构不稳定性的问题，提出了AISA-AR-FunctionCall框架。该框架基于270M参数的FunctionGemma骨干网络，通过系统性的数据集审计、模式修复、工具感知提示重构和全参数监督微调，将解析失败率从87%降至1%以下，函数名准确率提升超过8倍。研究发现错误类型从结构崩溃转变为语义错位，表明序列化稳定性和决策级推理是可分离的挑战。

【方法概述 / Method】
论文采用数据为中心的微调方法，包括系统性的数据集审计与模式修复、工具感知提示重构，以及基于FunctionGemma的全参数监督微调。此外，作者还探索了一种推理增强的LoRA变体，在工具调用前引入显式中间推理步骤。

【实验结果 / Results】
在留出测试集上，微调后的模型解析失败率从87%降至1%以下，函数名准确率提升超过8倍，跨方言和领域的参数对齐显著改善。错误分析显示模型错误从结构性问题转变为语义层面的错位。

【应用价值 / Applications】
该研究为阿拉伯语地区的智能体AI系统提供了可靠的函数调用能力，可应用于阿拉伯语客服自动化、智能助手、企业流程自动化等场景。所有数据集和模型已作为AISA框架开源发布，具有重要的实际部署价值和区域语言技术普惠意义。
