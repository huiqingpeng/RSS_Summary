---
title: "Case Study: Horizontal Side-Channel Analysis Attack against Elliptic Curve Scalar Multiplication Accelerator under Laser Illumination"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.19811"
published: "2026-03-23"
summarized: "2026-03-24T07:14:27.700635"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种针对椭圆曲线标量乘法加速器的组合攻击方法，将侧信道分析（SCA）与激光照射相结合。实验表明，激光照射会增加芯片的功耗，特别是静态功耗，但对水平功耗分析攻击的成功率影响不显著。作者推测，使用高功率激光束并专注于测量和分析静态电流，可显著提高攻击成功率，并首次提出了"激光照射下静态功耗攻击"（SCuLI攻击）的概念，指出其对采用先进工艺制造的密码芯片具有潜在威胁。

【方法概述 / Method】

本研究采用Teledyne LeCroy差分探头，对椭圆曲线标量乘法加速器实施水平侧信道分析攻击，同时引入激光照射作为物理刺激手段。通过对比激光照射前后的功耗特征，分析动态功耗与静态功耗的变化规律，探索新型攻击向量的可行性。

【实验结果 / Results】

实验结果显示，激光照射显著增加了芯片的整体功耗，其中静态功耗的增长尤为明显。然而，传统的水平功耗分析攻击成功率并未因此得到实质性提升。作者据此假设，专门针对静态电流进行精细化测量与分析，可能成为突破现有防御机制的有效途径。

【应用价值 / Applications】

该研究揭示了针对先进工艺节点（scaled technologies）密码芯片的新型攻击威胁，为密码硬件安全评估提供了重要参考。研究成果有助于推动针对SCuLI攻击的防御对策研发，对智能卡、安全芯片、物联网加密设备等需要高等级物理安全防护的场景具有重要指导意义。
