---
title: "MF-QAT: Multi-Format Quantization-Aware Training for Elastic Inference"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00529"
published: "2026-04-02"
summarized: "2026-04-03T07:22:29.400749"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了多格式量化感知训练（MF-QAT），使单个模型能够同时在多种数值精度格式下保持鲁棒性。研究发现MF-QAT可以在各目标精度上匹配单格式QAT的性能，且模型对训练时未见过的格式也具有良好的泛化能力。作者还提出了Slice-and-Scale转换流程，支持MXINT和MXFP格式在推理时动态降精度转换，无需重新训练，从而实现弹性精度缩放。

【方法概述 / Method】
MF-QAT通过在训练过程中对多种量化格式进行联合优化，使模型权重和激活值适应不同数值精度。针对MXINT和MXFP格式，作者设计了Slice-and-Scale转换方法，通过切片和缩放操作将高精度表示（如MXINT8/MXFP8）动态转换为低精度格式。整个流程采用单一锚定格式的检查点存储，支持运行时按需转换。

【实验结果 / Results】
实验表明，MF-QAT训练的单模型在各目标精度上的性能与专门训练的单格式QAT模型相当，且对未见格式具有良好的零样本泛化能力。Slice-and-Scale转换在运行时动态降精度几乎不造成额外精度损失，实现了从8位到更低位宽的高效弹性推理。

【应用价值 / Applications】
该研究为云端和边缘端弹性推理提供了实用方案，允许根据硬件支持能力或实时约束（如延迟、功耗预算）动态选择推理精度。单一模型适配多种部署场景，显著降低了模型存储和管理开销，特别适用于需要跨异构硬件平台部署的大规模AI服务。
