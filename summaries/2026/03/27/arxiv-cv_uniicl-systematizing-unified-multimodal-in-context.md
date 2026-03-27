---
title: "UniICL: Systematizing Unified Multimodal In-context Learning through a Capability-Oriented Taxonomy"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24690"
published: "2026-03-27"
summarized: "2026-03-28T07:14:51.396469"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对统一多模态模型中的上下文学习（In-context Learning, ICL）问题，提出了一种能力导向的六层分类法，用于诊断示例演示在不同认知层级（从基础感知到高阶辨别）中的功能角色。基于此框架，作者构建了大规模数据集UniICL-760K和评测基准UniICL-Bench，涵盖15个子任务的8-shot ICL场景。此外，论文提出了轻量级即插即用模块Context-Adaptive Prototype Modulator，以稳定少样本自适应能力，实验表明该方法在多数理解型ICL任务上超越了更大参数量的多模态大语言模型基线。

【方法概述 / Method】
论文首先建立了一个六层能力导向的分类体系，系统性地刻画多模态ICL中示例演示的认知功能层级；随后基于该分类法构建了包含760K个8-shot episode的大规模语料库UniICL-760K，并配套开发控制变量严格的评测基准UniICL-Bench。为缓解ICL性能的非单调性和任务依赖性，作者设计了Context-Adaptive Prototype Modulator模块，通过自适应调节原型表示来增强上下文学习的稳定性。

【实验结果 / Results】
在UniICL-Bench上的评估表明，所提方法在统一多模态ICL任务中取得了高度竞争力的综合表现，尤其在理解型ICL任务上超越了参数量更大的多模态大语言模型基线。该轻量级模块有效稳定了少样本自适应过程，显著改善了ICL效果的非单调性和跨模态干扰问题。

【应用价值 / Applications】
该研究为多模态大模型的免训练自适应提供了系统化的诊断框架和实用工具，可广泛应用于需要快速任务适配的视觉-语言理解、图像生成等场景。提出的分类法和评测基准有助于标准化ICL能力评估，而即插即用模块为资源受限环境下的高效模型定制提供了可行方案，对推动统一多模态模型的实用化部署具有重要价值。
