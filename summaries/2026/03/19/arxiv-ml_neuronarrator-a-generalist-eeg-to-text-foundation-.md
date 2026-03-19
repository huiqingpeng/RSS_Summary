---
title: "NeuroNarrator: A Generalist EEG-to-Text Foundation Model for Clinical Interpretation via Spectro-Spatial Grounding and Temporal State-Space Reasoning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16880"
published: "2026-03-19"
summarized: "2026-03-19T12:19:06.686908"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了NeuroNarrator，首个通用的EEG-to-Text基础模型，旨在将脑电信号转化为精确的临床叙述文本。研究团队构建了NeuroCorpus-160K数据集，包含超过16万段EEG信号及其对应的结构化临床语言描述。该模型通过对比学习目标实现时频波形与空间地形图的联合对齐，并基于状态空间模型整合历史时序与频谱上下文，从而生成连贯的临床叙述，为神经电生理数据的开放式临床解读建立了新范式。

【方法概述 / Method】

NeuroNarrator采用双阶段架构：首先通过对比学习将时序EEG波形与空间拓扑图对齐，建立"频谱-空间"基础表征；随后以状态空间模型（state-space formulation）为框架，将历史时序和频谱上下文条件化输入大型语言模型，实现从连续信号动态到离散临床语言的转换。该方法首次将Mamba等状态空间模型引入EEG序列建模，以线性复杂度捕获长程时序依赖。

【实验结果 / Results】

在多个基准数据集和零样本迁移任务上的广泛评估表明，NeuroNarrator能够有效整合时间、频谱和空间三重动态信息，生成的临床叙述在准确性、连贯性和临床可用性方面显著优于现有任务特定分类方法。模型展现出强大的跨数据集泛化能力，无需微调即可适应新的临床场景，为开放式EEG解读提供了首个通用基础框架。

【应用价值 / Applications】

该研究可直接应用于临床神经科报告自动化生成，辅助神经科医师快速解读脑电监测数据，提升诊断效率与标准化水平。其开放式文本生成能力还可支持癫痫监测、睡眠障碍分析、麻醉深度评估等多种临床场景的智能化解读，并为脑机接口系统的自然语言反馈模块提供技术基础，推动神经工程与临床实践的深度融合。
