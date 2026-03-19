---
title: "A practical artificial intelligence framework for legal age estimation using clavicle computed tomography scans"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17926"
published: "2026-03-19"
summarized: "2026-03-19T16:18:54.630977"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究提出了一种基于锁骨CT扫描的法律年龄估计实用AI框架，填补了该领域的技术空白。该框架结合自动锁骨检测、基于Integrated Gradients的切片选择策略以及多切片卷积神经网络，并引入共形预测区间实现不确定性量化。在1,158例尸体全身体CT数据集上，模型达到1.55±0.16年的平均绝对误差，超越人类专家（约1.90年）和现有方法，且已集成至Skeleton-ID软件作为法医决策支持工具。

【方法概述 / Method】

研究设计了三阶段可解释流程：首先采用基于特征的连通组件方法实现锁骨自动定位，仅需极少人工标注；随后利用Integrated Gradients引导切片选择，构建多切片CNN的输入数据；最后通过共形预测生成符合国际法医协议的可配置置信区间。归因分析验证模型聚焦于内侧锁骨骨骺等解剖相关区域。

【实验结果 / Results】

在New Mexico Decedent Image Database的保留测试集上，最终模型MAE为1.55±0.16年，显著优于人类专家（~1.90年）及同数据集先前方法（>1.75年）。共形预测支持按法医需求调整覆盖水平，Integrated Gradients热力图显示模型决策依赖于解剖学合理的内侧锁骨骨骺区域，增强了结果的可解释性。

【应用价值 / Applications】

该方法已整合入Skeleton-ID软件，作为多因素法医工作流程中的决策支持组件，适用于身份不明遗体的年龄推断、难民年龄评估等法律医学场景。框架的显式不确定性量化和国际协议兼容性，使其能够满足法庭证据的严谨性要求，推动AI工具在法医实践中的标准化应用。
