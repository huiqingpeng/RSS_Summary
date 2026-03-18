---
title: "ACPV-Net: All-Class Polygonal Vectorization for Seamless Vector Map Generation from Aerial Imagery"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16616"
published: "2026-03-18"
summarized: "2026-03-18T18:15:57.814112"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了全类别多边形矢量化（ACPV）这一新任务，旨在从航拍影像中一次性生成包含所有地物类别的完整矢量地图，确保多边形间共享边界、无间隙且无重叠。作者发布了首个公开基准数据集Deventer-512及标准化评估指标，并设计了ACPV-Net框架，通过语义监督条件机制（SSC）和拓扑重建模块实现语义感知与几何生成的耦合。实验表明，ACPV-Net在严格满足拓扑约束的同时，多边形质量超越所有单类别基线方法，且无需修改即可应用于单类别任务并在WHU-Building数据集上取得最优结果。

【方法概述 / Method】
ACPV-Net采用统一框架实现全类别矢量化，核心创新包括：（1）语义监督条件机制（SSC），将高层语义特征嵌入几何基元生成过程，实现语义与几何的联合建模；（2）拓扑重建模块，通过显式设计强制共享边一致性，从根本上消除重复边、间隙和重叠等拓扑不一致问题。

【实验结果 / Results】
在Deventer-512基准上，ACPV-Net在所有类别上均优于单类别专用基线，同时满足全局拓扑一致性约束；在WHU-Building单类别数据集上，该模型无需任何架构调整即达到当前最佳性能，证明了方法的通用性和优越性。

【应用价值 / Applications】
该研究可直接应用于地理信息系统（GIS）自动化更新、智慧城市三维建模、土地利用规划等领域，实现从遥感影像到可直接使用的矢量地图的高效转换；其严格的拓扑保证特性对于需要精确空间分析的专业测绘、导航地图制作等场景具有重要实用价值。
