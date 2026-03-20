---
title: "$K-$means with learned metrics"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14601"
published: "2026-03-20"
summarized: "2026-03-20T15:05:11.292820"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文研究了当度量测度空间的测度和距离均未知且需要估计时的Fréchet k-means问题。作者证明了k-means关于测度Gromov-Hausdorff拓扑的连续性，以及其Voronoi聚类的稳定性结果。该框架为广泛的度量学习程序的一致性证明提供了统一方法，并首次为多种重要估计器（包括流形上的Isomap和Fermat测地距离、扩散距离、基于学习地面度量的Wasserstein距离等）建立了新的收敛性结果。

【方法概述 / Method】

本文采用测度Gromov-Hausdorff拓扑作为分析工具，建立了度量测度空间中k-means的连续性理论框架。该方法不假设k-means解的唯一性，但在唯一性条件下可获得更强的理论保证，为耦合的度量学习与聚类问题提供了统一的数学基础。

【实验结果 / Results】

论文的主要理论成果包括：（1）k-means关于测度Gromov-Hausdorff拓扑的连续性定理；（2）Voronoi聚类的稳定性结果；（3）将框架应用于多种具体场景，首次证明了基于Isomap/Fermat距离、扩散距离、学习Wasserstein距离的k-means估计器的一致性，这些结果即使在k=1的退化情形下也是新的。

【应用价值 / Applications】

该研究的实际应用价值体现在：（1）为流形学习、度量学习和最优传输中的聚类算法提供理论保证，增强算法可靠性；（2）拓展至统计推断范式之外的领域，如首次通过渗流（first passage percolation）和长度空间的离散逼近，为复杂网络分析和几何数据处理等跨学科问题提供理论工具。
