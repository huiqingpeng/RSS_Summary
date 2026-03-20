---
title: "Koopman Autoencoders with Continuous-Time Latent Dynamics for Fluid Dynamics Forecasting"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.02832"
published: "2026-03-20"
summarized: "2026-03-20T14:10:38.266205"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了一种连续时间Koopman自编码器（continuous-time Koopman autoencoder），用于学习时变偏微分方程（PDEs）的替代模型。该方法在潜空间中引入参数化的线性生成器，通过矩阵指数实现精确的潜变量演化，从而无需自回归采样即可在任意时间分辨率下进行预测。实验表明，该方法在计算效率和长程稳定性方面具有显著优势，同时在短期生成精度上保持竞争力，有效解决了高表达性生成模型中常见的误差累积和计算成本高昂的问题。

【方法概述 / Method】

论文核心方法为连续时间Koopman自编码器架构，包含编码器、参数条件化的线性潜动态生成器和解码器三部分。潜动态通过矩阵指数运算实现精确的时间演化，避免了传统自回归方法中的逐步递推。该设计将非线性动力学编码到线性潜空间中，结合了神经网络的表达能力和线性系统的解析可解性。

【实验结果 / Results】

研究在具有挑战性的流体动力学基准数据集上进行了评估，与自回归神经算子（autoregressive neural operators）和基于扩散的模型进行了对比。结果表明，该方法实现了极高的计算效率和极端的长程稳定性，在短期生成精度上与现有方法相当，但在长时预测中显著减少了误差累积。

【应用价值 / Applications】

该方法适用于需要高效、稳定长时预测的流体动力学仿真场景，如气象预报、航空航天设计、海洋流动模拟等。其任意时间分辨率预测能力使其特别适合需要自适应时间步长或超分辨率时间插值的应用，同时大幅降低的计算成本有助于实时或大规模仿真部署。
