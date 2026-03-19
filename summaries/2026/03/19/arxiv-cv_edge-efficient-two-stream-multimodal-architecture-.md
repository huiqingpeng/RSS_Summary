---
title: "Edge-Efficient Two-Stream Multimodal Architecture for Non-Intrusive Bathroom Fall Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17069"
published: "2026-03-19"
summarized: "2026-03-19T15:04:46.548281"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对独居老人浴室跌倒检测问题，提出了一种边缘高效的双流多模态架构。该架构通过Motion-Mamba分支编码毫米波雷达信号以捕捉长程运动模式，同时利用Impact-Griffin分支处理地板振动信号以强调冲击瞬态和跨轴耦合，并通过低秩双线性交互和Switch-MoE头实现跨条件融合。实验表明，该方法在Raspberry Pi 4B上实现了96.1%的准确率和0.968的AUC，相比最强基线将延迟从35.9ms降至15.8ms，能耗降低24%。

【方法概述 / Method】
论文采用双流架构分别处理毫米波雷达（运动模态）和地板振动（冲击模态）信号：Motion-Mamba分支利用Mamba状态空间模型建模长程运动依赖，Impact-Griffin分支采用Griffin结构突出冲击瞬态特征。两流特征通过低秩双线性交互进行跨条件融合，最终由Switch-MoE门控专家混合头输出分类结果，实现运动与冲击的因果关联编码。

【实验结果 / Results】
在包含8种场景、超过3小时同步数据的浴室跌倒检测基准数据集上，模型达到96.1%准确率、94.8%精确率、88.0%召回率和91.1%宏F1分数。与最强基线相比，准确率提升2.0个百分点，跌倒召回率提升1.3个百分点；在Raspberry Pi 4B边缘设备上，推理延迟降低56%（35.9ms→15.8ms），每2.56秒窗口能耗减少24%（14200mJ→10750mJ）。

【应用价值 / Applications】
该研究适用于智能家居养老监护系统，可在保护隐私的非侵入式部署环境下实现实时浴室跌倒检测。其边缘计算优化特性使其特别适合资源受限的物联网网关设备，为独居老人提供低延迟、高能效的安全监测解决方案，同时有效区分真实跌倒与物体掉落等干扰事件。
