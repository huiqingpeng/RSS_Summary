---
title: "Rethinking Pose Refinement in 3D Gaussian Splatting under Pose Prior and Geometric Uncertainty"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16538"
published: "2026-03-18"
summarized: "2026-03-18T18:14:37.951677"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文重新审视了3D高斯泼溅（3DGS）中的姿态精修问题，指出其对初始相机姿态和重建几何的高度敏感性源于两种不确定性：姿态先验不确定性（来自回归或检索模型的单一确定性估计）和几何不确定性（3DGS重建缺陷传播至PnP求解器）。为此，作者提出了一种结合蒙特卡洛姿态采样与基于Fisher信息的PnP优化的重定位框架，无需重新训练或额外监督，在多种室内外基准测试中显著提升了定位精度与稳定性。

【方法概述 / Method】
该方法通过蒙特卡洛采样从姿态先验分布中生成多个候选姿态假设，以显式建模姿态不确定性；同时利用Fisher信息矩阵指导PnP优化过程，对几何不确定性进行加权处理，从而在优化中抑制不可靠几何约束的影响。

【实验结果 / Results】
实验表明，该方法在存在姿态噪声和深度噪声的情况下均能显著提升定位精度和优化稳定性，在多样化的室内和室外数据集上均取得一致的性能改进。

【应用价值 / Applications】
该研究可应用于机器人视觉定位、增强现实（AR）中的实时相机追踪、自动驾驶高精地图定位等场景，特别是在传感器噪声较大或初始位姿估计不可靠的恶劣环境中具有重要价值。
