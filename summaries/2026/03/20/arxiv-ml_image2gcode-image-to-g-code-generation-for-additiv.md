---
title: "Image2Gcode: Image-to-G-code Generation for Additive Manufacturing Using Diffusion-Transformer Model"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2511.20636"
published: "2026-03-20"
summarized: "2026-03-20T14:08:51.186882"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Image2Gcode，一种端到端的数据驱动框架，可直接从2D图像或手绘草图生成3D打印机的G-code指令，无需传统的CAD建模和切片步骤。该方法采用去噪扩散概率模型（DDPM）结合Transformer架构，通过迭代去噪将高斯噪声转化为可执行的打印轨迹和挤出参数。实验表明，该框架显著降低了增材制造的入门门槛，加速了从概念设计到物理制造的设计迭代周期，支持快速原型制作和分布式制造场景。

【方法概述 / Method】
Image2Gcode采用两阶段架构：首先通过图像编码器从输入图像中提取切片级结构线索，然后使用基于Transformer的扩散模型对G-code序列进行去噪生成。该方法将G-code视为结构化序列数据，利用扩散模型的迭代细化能力逐步生成包含移动坐标和挤出参数的完整打印路径。

【实验结果 / Results】
论文展示了Image2Gcode能够直接从单张2D图像生成语法正确、可执行的G-code程序，生成的打印轨迹在几何保真度和制造可行性方面达到实用水平。与需要CAD中间件的常规流程相比，该方法将设计到制造的迭代时间从数小时缩短至分钟级，同时保持了对上游2D-to-3D重建模块的兼容性。

【应用价值 / Applications】
该技术适用于快速原型开发、现场维修零件制造和分布式生产场景，使非专业用户能够通过简单草图或照片直接驱动3D打印。Image2Gcode还可与现有的2D-to-3D重建方法集成，构建从概念图像到物理成品的全自动流水线，为教育、创客文化和即时制造（instant manufacturing）提供低门槛解决方案。
