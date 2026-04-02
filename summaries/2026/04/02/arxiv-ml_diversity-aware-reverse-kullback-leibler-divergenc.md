---
title: "Diversity-Aware Reverse Kullback-Leibler Divergence for Large Language Model Distillation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00223"
published: "2026-04-02"
summarized: "2026-04-03T07:18:54.093866"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了反向KL散度（RKL）在大语言模型蒸馏中的应用，发现RKL虽优于正向KL（FKL），但存在结构性缺陷：非目标梯度会持续推高目标logit导致学生模型过度自信、输出多样性下降，且对非目标类别的监督不足造成尾部对齐差。为此，作者提出多样性感知RKL（DRKL），通过消除该梯度效应并增强非目标监督，在保持RKL优化优势的同时实现更好的保真度-多样性权衡。实验表明DRKL在多个数据集和模型家族上 consistently 优于FKL、RKL及其他先进蒸馏目标。

【方法概述 / Method】

作者首先通过将RKL梯度分解为目标组件和非目标组件进行理论分析，揭示非目标梯度在匹配后仍向上推动目标logit的机制；基于此提出DRKL，通过修正梯度结构消除过度自信问题，同时加强对非目标token的监督信号，保留RKL在主导模式上的聚焦优势。

【实验结果 / Results】

DRKL在跨数据集和模型家族的广泛实验中 consistently 超越FKL、RKL及现有最优蒸馏目标；该方法在提升模型性能的同时，显著改善了输出多样性与教师分布的保真度权衡，有效缓解了RKL导致的模式坍塌和尾部对齐不良问题。

【应用价值 / Applications】

DRKL可直接应用于大语言模型的高效知识蒸馏，助力在资源受限场景下部署高性能小模型；其改进的多样性-保真度权衡对需要丰富生成质量和可靠不确定度估计的任务（如对话系统、创意写作、安全关键应用）具有重要价值，也为理解KL散度变体在序列建模中的行为提供了理论基础。
