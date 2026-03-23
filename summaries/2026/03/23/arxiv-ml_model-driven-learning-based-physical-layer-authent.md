---
title: "Model-Driven Learning-Based Physical Layer Authentication for Mobile Wi-Fi Devices"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19972"
published: "2026-03-23"
summarized: "2026-03-24T07:23:44.103913"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对物联网（IoT）中无线通信的认证安全问题，提出了一种模型驱动的学习式物理层认证（PLA）方案。该方案将条件统计模型融入假设检验框架，推导出理论最优的Neyman-Pearson（NP）检测器，并基于此设计了轻量级神经网络LiteNP-Net。仿真和真实Wi-Fi实验表明，LiteNP-Net无需信道统计先验知识即可逼近NP检测器性能，且在实际场景中优于传统相关方法和最先进的Siamese方法。

【方法概述 / Method】
论文采用假设检验驱动的深度学习架构，首先通过条件统计模型推导理论最优的NP检测器，然后将其嵌入神经网络设计作为归纳偏置，构建轻量级的LiteNP-Net网络。该方法结合了模型驱动方法的统计最优性和数据驱动方法的实用性，摆脱了对信道统计信息的依赖。

【实验结果 / Results】
仿真结果表明LiteNP-Net能够在未知信道统计的情况下逼近理论最优NP检测器的性能；在基于Wi-Fi IoT开发套件的真实场景实验中，LiteNP-Net的性能显著优于传统基于相关性的方法以及当前最先进的基于Siamese网络的方法，验证了其在实际移动Wi-Fi环境中的有效性。

【应用价值 / Applications】
该研究为物联网设备的物理层安全认证提供了实用且高性能的解决方案，特别适用于资源受限的移动Wi-Fi设备。其轻量级特性使其适合部署在边缘IoT设备上，可有效防范无线广播环境下的身份伪造攻击，提升智能家居、工业物联网等场景的安全性和可靠性。
