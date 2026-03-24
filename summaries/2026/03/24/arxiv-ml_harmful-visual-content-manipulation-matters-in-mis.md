---
title: "Harmful Visual Content Manipulation Matters in Misinformation Detection Under Multimedia Scenarios"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.21054"
published: "2026-03-24"
summarized: "2026-03-25T07:18:34.125476"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种名为HAVC-M4D的新型多模态虚假信息检测方法，首次将视觉内容操纵特征与操纵意图特征（有害/无害）相结合用于虚假信息识别。由于真实的操纵标签和意图标签未知，作者引入了两个弱监督指标作为替代，通过辅助数据集和正例-未标记学习框架实现特征学习。在四个主流MMD数据集上的实验表明，该方法能显著提升现有多模态虚假信息检测方法的性能。

【方法概述 / Method】

该方法通过双分支框架分别提取**操纵特征**（判断视觉内容是否被篡改）和**意图特征**（区分篡改的有害性与无害性）。针对标签缺失问题，作者利用图像篡改检测的辅助数据集构建弱监督信号，并将两个分类任务建模为正例-未标记学习（Positive and Unlabeled Learning）问题，使模型在缺乏完整标注的情况下仍能学习判别性特征。

【实验结果 / Results】

HAVC-M4D在四个广泛使用的多模态虚假信息检测数据集上进行了全面评估，实验结果显示该方法能够**显著且一致地提升**现有MMD方法的检测性能。虽然具体数值指标未在摘要中详述，但"significant and consistent improvements"的表述表明该方法具有较强的泛化能力和鲁棒性。

【应用价值 / Applications】

该研究对社交媒体平台的自动化内容审核具有重要价值，可帮助识别经过恶意篡改的视觉内容（如深度伪造、误导性图片编辑等）以遏制虚假信息传播。同时，区分有害与无害操纵的能力有助于减少误报，避免对正当的创意编辑或艺术加工内容造成过度审查，在实际部署中更具实用性和可解释性。
