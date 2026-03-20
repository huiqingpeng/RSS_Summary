---
title: "Auto-Annotation with Expert-Crafted Guidelines: A Study through 3D LiDAR Detection Benchmark"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2506.02914"
published: "2026-03-20"
summarized: "2026-03-20T16:12:03.963948"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文探索了一种基于专家制定指南的自动标注范式，以替代传统的人工标注流程。研究者构建了AutoExpert基准测试，该测试基于nuScenes数据集，包含18个目标类别的专家指南（以语言描述和少量视觉示例形式呈现），要求模型基于少量带标签的图像和文本在LiDAR数据上执行3D检测。通过利用基础模型构建简单的三阶段流水线（2D检测分割→2D到3D提升→3D立方体生成），研究将3D检测mAP提升至25.4，显著优于先前方法的12.1。

【方法概述 / Method】
论文采用基础模型驱动的三阶段流水线解决跨模态自动标注问题：首先利用基础模型在RGB图像中进行2D目标检测与分割，然后基于已知传感器位姿将2D检测结果提升为3D点云，最后生成3D标注框。该方法的核心挑战在于处理数据模态差异（图像→LiDAR）和标注任务差异（2D→3D），且专家指南仅提供少量图像示例而无LiDAR视觉参考。

【实验结果 / Results】
经过对关键组件的渐进式优化，该方法在AutoExpert基准上取得了25.4的3D检测mAP，较先前最优方法12.1的性能实现了翻倍以上的提升。这一结果表明，结合专家指南与基础模型的自动标注流水线能够有效弥合跨模态检测的性能差距。

【应用价值 / Applications】
该研究为自动驾驶领域的3D LiDAR数据标注提供了高效、低成本的自动化解决方案，可显著减少人工标注的劳动强度和成本。同时，AutoExpert基准及其方法论可推广至其他需要专家知识指导的跨模态自动标注场景，为构建大规模高质量训练数据集提供新范式。
