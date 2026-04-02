---
title: "Sit-to-Stand Transitions Detection and Duration Measurement Using Smart Lacelock Sensor"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00175"
published: "2026-04-02"
summarized: "2026-04-03T07:17:56.498267"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究开发了一种利用智能鞋带锁传感器（Smart Lacelock）检测坐立转换（Sit-to-Stand, SiSt）并测量其持续时间的方法。该鞋载设备集成称重传感器、加速度计和陀螺仪，通过多模态信号特征训练机器学习分类器，在16名老年人（平均年龄76.84岁）的SPPB测试中实现了0.98的分类准确率和0.8的F1分数，持续时间测量的平均绝对误差仅为0.047秒。研究表明该传感器具有实时跌倒风险评估和老年人活动能力监测的应用潜力。

【方法概述 / Method】
研究采用轻量化的鞋载智能鞋带锁传感器，融合称重、加速度与角速度多源信号进行运动分析。通过4折参与者独立交叉验证，比较了四种机器学习分类器的性能，最终选用集成袋装树（bagged tree）模型实现SiSt转换的精准识别与时序定位。

【实验结果 / Results】
袋装树分类器在SiSt转换检测中达到0.98的准确率和0.8的F1分数；对于正确识别的转换事件，持续时间测量的平均绝对误差为0.047秒（标准差0.07秒）。该性能指标表明系统具备高精度、低延迟的临床级测量能力。

【应用价值 / Applications】
该技术可嵌入日常 footwear 实现居家无感监测，为老年人提供连续的下肢功能评估与跌倒风险预警。其轻量化设计与高精度特性使其适用于社区健康管理和远程老年照护场景，有助于早期识别肌少症和功能衰退。
