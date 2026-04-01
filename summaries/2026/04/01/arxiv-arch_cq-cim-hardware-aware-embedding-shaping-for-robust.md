---
title: "CQ-CiM: Hardware-Aware Embedding Shaping for Robust CiM-Based Retrieval"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2602.20083"
published: "2026-04-01"
summarized: "2026-04-02T07:12:43.341869"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对边缘设备上部署检索增强生成（RAG）系统的需求，提出CQ-CiM框架，以解决高维高精度嵌入向量与存内计算（CiM）架构低精度、低维度约束之间的"表征鸿沟"。该框架首次将压缩与量化联合学习，生成适用于多样化CiM硬件设计的低比特嵌入，为RAG在CiM上的全面应用提供了统一的数据整形方案。

【方法概述 / Method】
CQ-CiM采用硬件感知的数据整形方法，通过端到端联合优化压缩（降维）和量化（降低精度）两个操作，而非传统分阶段处理方式。该框架能够针对不同CiM实现（如SRAM、ReRAM、FeFET）的具体硬件约束（如2-bit单元、512×512阵列）自适应生成兼容的嵌入表示。

【实验结果 / Results】
论文表明，相比将维度和精度处理分离的朴素方法，CQ-CiM在保持数据保真度方面显著更优，有效避免了因数据退化导致的检索性能下降。该框架成功弥合了表征鸿沟，使CiM能够真正发挥其在边缘RAG场景中的低延迟优势。

【应用价值 / Applications】
CQ-CiM为边缘AI和RAG系统的硬件-软件协同设计提供了关键支撑，使CiM架构能够高效部署于资源受限的边缘设备。该研究降低了CiM采用的门槛，帮助硬件设计者明确区分电路设计问题与输入数据质量问题，加速存内计算技术在智能终端、物联网等场景的落地应用。
