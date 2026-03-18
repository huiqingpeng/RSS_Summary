---
title: "Point-to-Mask: From Arbitrary Point Annotations to Mask-Level Infrared Small Target Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16257"
published: "2026-03-18"
summarized: "2026-03-18T18:09:51.332431"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Point-to-Mask框架，通过低成本点标注实现红外小目标（IRSTD）的掩膜级检测。该框架包含两个核心组件：物理驱动的自适应掩膜生成模块（PAMG）将点标注转换为紧凑目标掩膜，以及轻量级半径感知点回归网络（RPR-Net）将IRSTD重新表述为目标中心定位与有效半径回归任务。实验表明，该方法在大幅降低标注成本的同时，能够达到接近全监督方法的检测性能。

【方法概述 / Method】
PAMG模块利用红外目标的物理特性（如热辐射扩散模型）从点标注生成伪掩膜标签和几何监督信号；RPR-Net则结合时空运动线索，通过预测目标中心点坐标和有效半径来实现目标检测。两个模块形成闭环：训练时PAMG为RPR-Net提供监督，推理时RPR-Net的几何预测反馈至PAMG以恢复像素级掩膜。

【实验结果 / Results】
作者构建了带有精细像素级标注的序列数据集SIRSTD-Pixel用于系统评估；实验表明所提框架生成的伪标签质量高，检测精度接近全监督方法，同时推理效率显著提升，在点监督设置下实现了与密集标注相当甚至更优的性能。

【应用价值 / Applications】
该方法适用于红外监控、预警探测等需要快速部署的场景，可大幅减少专业标注人员的时间和成本投入；其"点标注→掩膜检测"的范式也为其他小目标检测任务（如遥感、医学影像中的微小病灶检测）提供了可迁移的低标注成本解决方案。
