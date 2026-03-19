---
title: "CogGen: Cognitive-Load-Informed Fully Unsupervised Deep Generative Modeling for Compressively Sampled MRI Reconstruction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.04438"
published: "2026-03-19"
summarized: "2026-03-19T14:19:04.699388"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CogGen，一种认知负载感知的完全无监督深度生成模型（FU-DGM），用于压缩采样MRI（CS-MRI）重建。该方法将CS-MRI视为分阶段反演问题，通过自步课程学习（SPCL）逐步调度内在难度和外在干扰，实现从易到难的k空间加权/选择策略。CogGen-DIP和CogGen-INR在重建保真度和收敛行为上均优于现有无监督基线方法，甚至可与有监督方法竞争。

【方法概述 / Method】
CogGen采用双模式自步课程学习框架，包含"学生模式"（反映模型当前学习能力）和"教师模式"（指示应遵循的目标），支持软加权和硬选择两种机制。该方法通过渐进式调度策略，在早期迭代中优先拟合低频、高信噪比、结构主导的样本，后期再引入高频或噪声主导的测量数据。

【实验结果 / Results】
实验表明，CogGen显著改善了重建保真度和收敛速度，相比传统FU-DGM方法（如DIP和INR）有效缓解了过拟合测量噪声的问题。CogGen在计算资源或训练数据受限的场景下展现出与有监督管道相竞争的性能。

【应用价值 / Applications】
该研究适用于临床MRI扫描中数据稀缺或计算资源受限的场景，能够在无配对训练数据的情况下实现高质量图像重建。CogGen的认知负载调度思想可推广至其他病态逆问题，为医学影像的快速、低成本、隐私保护型重建提供了新途径。
