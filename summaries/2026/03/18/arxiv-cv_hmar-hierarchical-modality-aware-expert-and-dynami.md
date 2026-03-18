---
title: "HMAR: Hierarchical Modality-Aware Expert and Dynamic Routing Medical Image Retrieval Architecture"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16679"
published: "2026-03-18"
summarized: "2026-03-18T18:17:56.916986"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了HMAR（分层模态感知专家与动态路由）框架，一种基于混合专家（MoE）架构的自适应医学图像检索系统，解决了现有系统在统一特征编码、粗粒度相似度度量以及缺乏细粒度区域检索能力方面的三大局限。该框架通过双专家机制（全局特征提取与位置不变局部表征学习）、两阶段对比学习策略（无需边界框标注）以及滑动窗口匹配算法，实现了整体相似性与病灶区域精确检索的统一。在RadioImageNet-CT数据集上的实验表明，HMAR在64位和128位哈希码下分别取得0.711和0.724的mAP，较当前最优方法ACIR提升0.7%和1.1%。

【方法概述 / Method】
HMAR采用Mixture-of-Experts架构，包含两个专业化专家：Expert0负责提取全局特征用于整体图像匹配，Expert1学习位置不变的局部表征以实现病灶区域级检索。框架引入两阶段对比学习策略，通过图像级和区域级对比损失消除对昂贵边界框标注的依赖；推理阶段采用滑动窗口匹配算法进行密集局部比较，并利用Kolmogorov-Arnold Network层生成紧凑哈希码以支持高效的汉明距离搜索。

【实验结果 / Results】
在包含16种临床模式、29,903张图像的RadioImageNet-CT数据集上，HMAR在64位和128位哈希码配置下分别达到0.711和0.724的平均精度均值（mAP）。与当前最先进的ACIR方法相比，性能分别提升0.7%和1.1%，验证了该框架在医学图像检索任务中的有效性。

【应用价值 / Applications】
HMAR可广泛应用于计算机辅助诊断系统，为放射科医生提供基于相似病例的智能检索支持，尤其适用于需要精确定位病灶区域的临床场景（如肿瘤筛查与随访）。其高效哈希编码机制支持大规模医学影像数据库的快速检索，且无需昂贵的专家标注即可训练，降低了部署成本，具有显著的临床实用价值和推广潜力。
