---
title: "Joint Optimization of Storage and Loading for High-Performance 3D Point Cloud Data Processing"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16945"
published: "2026-03-19"
summarized: "2026-03-19T14:22:01.979399"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对3D点云数据规模庞大、格式多样导致的数据加载与处理效率瓶颈问题，提出了一种统一的存储格式.PcRecord以及高性能数据处理流水线。通过多阶段并行流水线架构优化计算资源利用，该系统在多个主流点云数据集上实现了显著的性能加速，在GPU和Ascend平台上分别获得最高8.07倍和25.4倍的速度提升，有效解决了大规模点云数据处理的效率挑战。

【方法概述 / Method】
作者设计了.PcRecord统一存储格式以替代PLY、XYZ、BIN等多样化格式，减少存储占用并加速数据访问；同时构建了多模块集成的高性能数据处理流水线，采用多阶段并行流水线架构实现计算资源的高效调度与利用。

【实验结果 / Results】
系统在六个主流点云数据集上进行验证：ModelNet40、S3DIS、ShapeNet、KITTI、SUN RGB-D和ScanNet。GPU平台上平均加速比分别为6.61×、2.69×、2.23×、3.09×、8.07×和5.67×；Ascend平台上分别达到6.9×、1.88×、1.29×、2.28×、25.4×和19.3×，其中SUN RGB-D数据集在Ascend上获得最高25.4倍加速。

【应用价值 / Applications】
该研究成果可直接应用于自动驾驶、机器人感知和增强现实等依赖大规模3D点云处理的领域，通过降低数据I/O开销和加速预处理流程，显著提升深度学习模型训练与推理的效率，为实时3D视觉应用提供基础设施支撑。
