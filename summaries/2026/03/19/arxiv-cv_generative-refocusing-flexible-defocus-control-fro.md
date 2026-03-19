---
title: "Generative Refocusing: Flexible Defocus Control from a Single Image"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2512.16923"
published: "2026-03-19"
summarized: "2026-03-19T16:29:57.510233"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了"生成式重聚焦"(Generative Refocusing)，一种从单张图像实现灵活景深控制的新方法。该方法通过两步流程解决单图像重聚焦难题：首先使用DeblurNet从多样化输入中恢复全聚焦图像，然后使用BokehNet生成可控的散景效果。研究结合了合成数据与真实散景图像，在实现精确控制的同时保留了真实的光学特性，并在散焦去模糊、散景合成和重聚焦基准测试中取得了最优性能。

【方法概述 / Method】

该方法采用双网络架构：DeblurNet负责从各种模糊输入中恢复清晰的全聚焦图像，BokehNet则基于恢复的全聚焦图像生成具有精确光圈控制的真实感散景。系统通过混合合成数据与真实散景图像进行训练，突破了传统方法依赖全聚焦输入或纯模拟器合成数据的限制。

【实验结果 / Results】

实验表明，该方法在多个基准测试中达到领先水平，包括散焦去模糊(defocus deblurring)、散景合成(bokeh synthesis)和重聚焦(refocusing)任务。方法还支持自定义光圈形状，提供了传统技术难以实现的灵活控制能力。

【应用价值 / Applications】

该技术可广泛应用于计算摄影领域，使摄影师能够在拍摄后自由调整景深效果，无需多次尝试或专业设备。其自定义光圈形状功能为创意摄影和影视后期制作提供了新的可能性，同时降低了高质量景深控制的技术门槛。
