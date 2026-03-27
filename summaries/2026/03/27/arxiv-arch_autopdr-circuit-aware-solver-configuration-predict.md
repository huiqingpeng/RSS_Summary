---
title: "AutoPDR: Circuit-Aware Solver Configuration Prediction for Hardware Model Checking"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.25048"
published: "2026-03-27"
summarized: "2026-03-28T07:07:44.511186"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了AutoPDR，一种面向硬件模型检测的电路感知求解器配置预测框架。针对PDR（Property Directed Reachability）算法性能高度依赖参数配置、手动调参耗时且需要专业知识的问题，该研究结合图学习和静态电路特征，实现智能启发式选择，并通过基于约束的参数过滤减少78%的搜索空间。实验表明，该方法能自动识别电路特定的参数模式，相比默认配置和常用设置显著提升性能。

【方法概述 / Method】
AutoPDR采用图神经网络处理电路的图表示，并融合结构、功能和连接性等静态电路特征进行特征提取。通过引入专家先验知识构建约束条件，预先过滤无效和低效配置，从而在缩减的搜索空间内预测最优PDR求解配置。

【实验结果 / Results】
在综合基准测试集上的实验评估显示，AutoPDR相比默认配置和常用参数设置取得了显著的性能提升。系统成功识别出不同电路的特定参数模式，并能基于电路特征自动选择最适合的求解策略。

【应用价值 / Applications】
AutoPDR为自动化形式化验证工作流提供了实用工具，特别适用于需要快速响应的硬件验证任务，如集成电路设计验证和安全关键系统的形式化分析。该方法降低了对专家调参经验的依赖，有望加速硬件设计周期并提升验证效率。
