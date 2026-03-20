---
title: "MicroVision: An Open Dataset and Benchmark Models for Detecting Vulnerable Road Users and Micromobility Vehicles"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18192"
published: "2026-03-20"
summarized: "2026-03-20T15:06:38.604058"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了MicroVision数据集，这是一个开源图像数据集，用于训练和评估检测弱势道路使用者（VRUs，包括行人、骑行者、电动滑板车骑行者）和静止微型交通工具（MMVs，包括自行车、电动滑板车）的目标检测模型。该数据集从VRU视角采集，包含8,000余张高清图像和30,000余个精细标注，覆盖全年近2,000个独特交互场景。研究还提供了基于最先进架构的基准检测模型，在未见测试集上达到0.723的平均精度均值（mAP），以支持交通安全和微型交通工具使用监测。

【方法概述 / Method】
研究采用目标检测领域的主流架构构建基准模型，具体包括YOLO系列和Faster R-CNN等state-of-the-art检测器，并在MicroVision数据集上进行训练和评估。数据集采集采用VRU视角（而非传统车载视角），涵盖人行道、自行车道等VRU专用区域，通过全年多场景采集确保数据多样性。

【实验结果 / Results】
基准模型在MicroVision测试集上取得了最高0.723的mAP性能，验证了数据集的有效性和检测任务的挑战性。实验结果表明，该数据集能够有效支持细粒度VRU和MMV检测，区分传统数据集中常被混淆的类别（如行人与电动滑板车骑行者）。

【应用价值 / Applications】
该研究可直接应用于智能交通监控系统，帮助区分不同类型的道路使用者和微型交通工具，提升交通安全分析精度。同时可支持城市规划部门监测微型交通工具的使用模式，优化基础设施设计，并为自动驾驶系统的VRU感知模块提供更丰富的训练数据。
