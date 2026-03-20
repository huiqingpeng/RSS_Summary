---
title: "Hardware-Aware Neural Architecture Search for Encrypted Traffic Classification on Resource-Constrained Devices"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2506.11319"
published: "2026-03-20"
summarized: "2026-03-20T14:15:51.401117"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种通过硬件感知神经架构搜索（HW-NAS）优化的深度神经网络，用于在资源受限的物联网（IoT）和边缘设备上进行会话级加密流量分类。该优化后的1D卷积神经网络在ISCX VPN-nonVPN数据集上实现了96.60%的准确率，仅需88.26K参数、10.08M FLOPs和20.12K最大张量大小，相比最先进模型分别减少了444倍、312倍和15倍的资源开销。该模型在多个VPN和流量分类任务中达到99.86%的准确率，并能泛化到外部基准测试，同时在STM32微控制器上成功部署验证。

【方法概述 / Method】
论文采用硬件感知神经架构搜索（HW-NAS）方法，针对严格内存和计算约束自动优化1D卷积神经网络架构。研究还系统分析了头部级预处理和会话长度缩减（最高75%）对模型性能与效率的权衡影响，并对优化后的架构进行量化以适应嵌入式部署。

【实验结果 / Results】
优化模型在ISCX VPN-nonVPN数据集上达到96.60%准确率，参数仅88.26K；在多个VPN和流量分类任务中最高达99.86%准确率，在USTC-TFC和QUIC NetFlow外部基准上分别达99.98%准确率。会话长度减少75%可使效率显著提升，而准确率仅下降1-2%；但不恰当的预处理设置会导致准确率下降7%。量化后的架构在STM32微控制器上实现了低延迟推理。

【应用价值 / Applications】
该研究为资源受限的IoT网络和边缘设备提供了实用的加密流量分析解决方案，适用于网络安全监控、VPN流量检测和隐私保护场景。头部级预处理能力使其能在更严格的隐私要求下工作，而高效的嵌入式部署能力支持实时、低功耗的网络流量分类应用。
