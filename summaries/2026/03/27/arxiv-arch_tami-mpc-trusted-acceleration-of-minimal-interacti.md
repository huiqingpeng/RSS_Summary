---
title: "TAMI-MPC:Trusted Acceleration of Minimal-Interaction MPC for Efficient Nonlinear Inference"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.24861"
published: "2026-03-27"
summarized: "2026-03-28T07:07:08.155883"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了TAMI-MPC框架，一种面向边缘设备隐私保护机器学习的可信最小交互多方安全计算方案。该研究通过重新设计核心原语（叶节点比较和树合并），将交互轮次从log(n)降至每操作仅1轮，显著降低通信开销。同时利用TEE内同步种子消除绝大多数不经意传输(OT)操作，并结合相关随机性复用技术实现轻量计算，最终在ResNet-50和BERT-base推理上分别取得4.86倍和7.44倍的加速效果。

【方法概述 / Method】
TAMI-MPC采用可信执行环境(TEE)与专用加速器协同设计的架构，通过TEE内同步种子生成伪随机数替代传统OT协议，消除计算瓶颈；并设计专用加速器重构数据流，实现连续细粒度流式处理与高并行度，降低内存开销。

【实验结果 / Results】
在ResNet-50推理任务中，TAMI-MPC相比最先进的CNN框架实现最高4.86倍加速；在BERT-base推理任务中，相比最先进的LLM框架实现最高7.44倍加速。核心优化使非线性操作的交互轮次从对数级降至常数级1轮。

【应用价值 / Applications】
该研究适用于资源受限边缘设备上的实时隐私保护机器学习推理，如智能手机、IoT设备等场景中的安全图像识别与自然语言处理。其低通信、低计算开销特性使MPC在边缘计算环境中具备实际部署可行性，推动隐私保护AI的广泛应用。
