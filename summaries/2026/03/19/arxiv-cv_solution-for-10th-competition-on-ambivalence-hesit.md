---
title: "Solution for 10th Competition on Ambivalence/Hesitancy (AH) Video Recognition Challenge using Divergence-Based Multimodal Fusion"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16939"
published: "2026-03-19"
summarized: "2026-03-19T14:21:36.746442"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对第10届ABAW竞赛（CVPR 2026）中的矛盾/犹豫（A/H）视频识别挑战，提出了一种基于散度的多模态融合方法。该方法通过显式测量视觉、音频和文本通道之间的跨模态冲突来识别A/H状态，在BAH数据集验证集上取得了0.6808的宏F1分数，显著优于0.2827的基线水平。统计分析进一步证实，动作单元（AUs）的时间变异性是区分A/H的主导视觉特征。

【方法概述 / Method】
该研究采用三模态特征提取架构：视觉特征通过Py-Feat提取动作单元（AUs），音频使用Wav2Vec 2.0编码，文本采用BERT嵌入。各模态经BiLSTM与注意力池化处理后投影至共享嵌入空间，融合模块通过计算模态嵌入间的成对绝对差值直接捕捉表征A/H的模态不一致性。

【实验结果 / Results】
在包含1,132个视频的BAH数据集上，该方法达到0.6808的宏F1分数，较挑战赛基线（0.2827）提升约141%。验证表明AU的时间动态变化是A/H识别的关键视觉线索，而基于散度的融合策略有效量化了跨模态冲突这一A/H的核心特征。

【应用价值 / Applications】
该研究为情感计算中的人机交互提供了精准的犹豫状态检测方案，可应用于心理咨询辅助系统、客户服务质量评估及智能面试分析等场景。其多模态冲突建模框架对理解微妙情感状态具有普适性，可扩展至其他需要识别矛盾情感的领域。
