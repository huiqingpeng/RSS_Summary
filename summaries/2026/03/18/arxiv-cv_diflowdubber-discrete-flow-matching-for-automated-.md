---
title: "DiFlowDubber: Discrete Flow Matching for Automated Video Dubbing via Cross-Modal Alignment and Synchronization"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.14267"
published: "2026-03-18"
summarized: "2026-03-18T19:04:11.988397"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了DiFlowDubber，一种用于自动化视频配音的新型两阶段训练框架。该框架通过离散流匹配生成骨干网络，将预训练文本到语音（TTS）模型的知识有效迁移到视频驱动配音任务中。论文设计了FaPro模块从面部表情捕获全局韵律和风格线索，并引入Synchronizer模块桥接文本、视频与语音之间的模态差距，实现精确的语音-唇形同步。在两个主要基准数据集上的实验表明，DiFlowDubber在多项指标上均优于先前方法。

【方法概述 / Method】

DiFlowDubber采用基于离散流匹配的生成式骨干网络，结合两阶段训练策略：首先利用预训练TTS模型进行知识迁移，然后通过FaPro模块提取面部表情的韵律和风格信息来指导后续语音属性建模，最后通过Synchronizer模块实现跨模态对齐与时间同步。

【实验结果 / Results】

在两个主要基准数据集上的实验表明，DiFlowDubber在多项评估指标上均优于现有方法，能够生成更具表现力的韵律、更丰富的声学特征以及更精确的语音-唇形同步效果。

【应用价值 / Applications】

该技术可广泛应用于电影制作、多媒体内容创作以及辅助语音技术等领域，为视频本地化、无障碍内容生产和跨语言视频传播提供高质量的自动化配音解决方案。
