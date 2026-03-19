---
title: "The Truth, the Whole Truth, and Nothing but the Truth: Automatic Visualization Evaluation from Reconstruction Quality"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16873"
published: "2026-03-19"
summarized: "2026-03-19T16:21:06.660220"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种基于数据重建质量的自动化可视化评估指标，无需依赖大规模人工标注数据集。该方法利用原始数据作为隐式真实标签，通过测量从可视化图像中重建原始数据的准确性来评估可视化质量。这一重建指标为全面的人工评估提供了可自主扩展的替代方案，能够支持更高效可靠的AI驱动可视化工作流。

【方法概述 / Method】
论文核心方法是将可视化质量评估转化为数据重建任务：给定生成的可视化图像，使用计算机视觉技术（如OCR、图表解析等）提取视觉元素并重建原始数据，然后计算重建数据与真实数据之间的差异作为质量分数。该方法无需人工标注，直接以原始数据为隐式基准进行端到端评估。

【实验结果 / Results】
（注：摘要及提供内容未包含具体实验结果，仅提及该方法"facilitating more efficient and reliable AI-driven visualization workflows"）

【应用价值 / Applications】
该研究主要应用于AI自动生成可视化的质量监控场景，可替代昂贵的人工评估流程，实现大规模自动化筛选与迭代优化。其核心价值在于为agentic可视化生成系统提供可扩展的反馈机制，降低人机协作成本，推动数据可视化领域的智能化生产 pipeline 建设。
