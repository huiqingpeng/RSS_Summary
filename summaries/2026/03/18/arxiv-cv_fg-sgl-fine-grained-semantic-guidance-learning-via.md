---
title: "FG-SGL: Fine-Grained Semantic Guidance Learning via Motion Process Decomposition for Micro-Gesture Recognition"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16269"
published: "2026-03-18"
summarized: "2026-03-18T18:10:10.568181"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文针对微手势识别（Micro-Gesture Recognition, MGR）中类别间差异细微的挑战，提出了细粒度语义引导学习框架（FG-SGL）。该框架通过融合细粒度和类别级语义信息来引导视觉-语言模型感知局部微手势运动，并构建了包含四个语义维度的人工标注细粒度文本数据集。实验表明，FG-SGL在微手势识别任务上取得了具有竞争力的性能，验证了细粒度语义引导的有效性。

【方法概述 / Method】

FG-SGL框架包含两个核心模块：细粒度语义适配器（FG-SA）利用细粒度语义线索引导局部运动特征学习，类别级语义适配器（CP-A）通过类别级语义引导增强微手势特征的可分性。此外，研究设计了一种多级对比优化策略，以从粗到细的模式联合优化两个模块。

【实验结果 / Results】

论文通过实验验证了FG-SGL在微手势识别任务上的有效性，表明该框架能够有效捕捉细微的局部运动差异。具体性能指标在原文PDF中详细呈现，整体达到了与现有方法相比具有竞争力的识别准确率。

【应用价值 / Applications】

该研究可应用于人机交互、智能监控、虚拟现实等需要精确识别细微手势场景的领域。通过细粒度语义引导机制，该方法有望提升对微妙情感表达和意图理解的识别能力，为更自然的人机交互提供技术支撑。
