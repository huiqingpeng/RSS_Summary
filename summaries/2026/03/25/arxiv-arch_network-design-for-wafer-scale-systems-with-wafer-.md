---
title: "Network Design for Wafer-Scale Systems with Wafer-on-Wafer Hybrid Bonding"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2603.05266"
published: "2026-03-25"
summarized: "2026-03-26T07:07:48.216418"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文研究了基于Transformer的大规模语言模型受限于芯片边界外通信带宽急剧下降的问题。作者利用晶圆对晶圆混合键合（wafer-on-wafer hybrid bonding）技术实现晶圆级集成，以提供键合晶圆上光刻单元（reticle）之间的超高带宽。研究重点探讨了光刻单元在晶圆上的物理排布如何影响可实现的网络拓扑和通信性能，提出了四种优化的光刻单元排布方案，显著提升了系统通信效率。

【方法概述 / Method】
论文从二维网格状基线拓扑出发，提出了四种创新的光刻单元物理排布方案：对齐式（Aligned）、交错式（Interleaved）、旋转式（Rotated）和轮廓式（Contoured）。这些方案通过优化键合晶圆间光刻单元的空间位置关系，重新设计网络拓扑结构，以最大化利用晶圆对晶圆混合键合提供的高密度垂直互连带宽。

【实验结果 / Results】
实验结果表明，所提出的四种光刻单元排布方案相比基线设计，在通信性能上实现了显著提升：吞吐量提升高达250%，延迟降低最高达36%，每传输字节的能耗减少最高达38%。其中不同排布方案在吞吐量、延迟和能效方面各有优势，为不同应用场景提供了灵活的设计选择。

【应用价值 / Applications】
该研究对大规模AI训练和推理系统具有重要价值，特别是需要海量计算资源和高效通信的Transformer类大语言模型。晶圆级集成技术结合优化的网络拓扑设计，可突破传统多芯片系统的内存墙和通信瓶颈，为下一代AI加速器、高性能计算（HPC）系统以及数据中心级计算平台提供可扩展的高能效解决方案。
