---
title: "DRiffusion: Draft-and-Refine Process Parallelizes Diffusion Models with Ease"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.25872"
published: "2026-03-30"
summarized: "2026-03-31T07:19:23.326538"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出DRiffusion，一种通过草稿-精炼（draft-and-refine）过程并行化扩散模型推理的采样框架，以解决扩散模型迭代采样速度慢、延迟高的问题。该方法利用跳跃转移生成未来多个时间步的草稿状态，并行计算其对应噪声，再用于标准去噪过程生成精炼结果。理论上可实现1/n或2/(n+1)的加速比（n为设备数），实验表明在1.4-3.7倍加速的同时，生成质量仅有轻微下降。

【方法概述 / Method】
DRiffusion采用"草稿-精炼"两阶段并行策略：首先通过skip transitions预测未来多个时间步的草稿状态，并行计算这些状态的噪声估计；然后将并行计算的噪声融入标准去噪流程进行精炼，支持保守模式（conservative）和激进模式（aggressive）两种配置。

【实验结果 / Results】
在多个扩散模型上实现1.4×-3.7×的推理加速；在MS-COCO数据集上，FID和CLIP分数与原始模型基本持平，PickScore和HPSv2.1平均仅下降0.17和0.43，验证了加速效果与质量保持的平衡。

【应用价值 / Applications】
该研究可显著降低扩散模型在实时交互式应用（如实时图像编辑、在线内容生成工具）中的延迟门槛，使高保真生成模型能够部署于对响应时间敏感的生产环境，推动扩散模型从离线批处理向在线服务转型。
