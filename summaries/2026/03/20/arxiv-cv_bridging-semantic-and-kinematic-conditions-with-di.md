---
title: "Bridging Semantic and Kinematic Conditions with Diffusion-based Discrete Motion Tokenizer"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19227"
published: "2026-03-20"
summarized: "2026-03-20T16:06:42.251947"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了一种三阶段运动生成框架，将连续扩散模型在运动学控制方面的优势与离散token生成器在语义条件方面的优势相结合。核心创新是MoTok——一种基于扩散的离散运动tokenizer，通过将运动恢复委托给扩散解码器来实现语义抽象与细粒度重建的解耦。在HumanML3D数据集上，该方法仅用MaskControl六分之一的token数量，显著提升了可控性和保真度，轨迹误差从0.72cm降至0.08cm，FID从0.083降至0.029；且在更强的运动学约束下，FID进一步从0.033降至0.014，突破了以往方法性能随约束增强而下降的限制。

【方法概述 / Method】
该框架包含三个阶段：条件特征提取（Perception）、离散token生成（Planning）和基于扩散的运动合成（Control）。MoTok作为核心组件，采用单层紧凑token进行语义规划，同时通过扩散解码器负责运动细节重建，实现了语义与运动学的分离处理。对于运动学条件，粗粒度约束在规划阶段引导token生成，细粒度约束则在控制阶段通过扩散优化强制执行。

【实验结果 / Results】
在HumanML3D基准测试上，该方法相比MaskControl实现了数量级的性能提升：token使用量减少83%（仅为1/6），轨迹误差降低89%（0.72cm→0.08cm），FID改善65%（0.083→0.029）。值得注意的是，与先前方法在强运动学约束下性能退化不同，本文方法展现出"约束越强、保真度越高"的特性，FID从0.033进一步优化至0.014。

【应用价值 / Applications】
该研究可广泛应用于角色动画、游戏开发、虚拟现实和机器人运动规划等领域，特别是在需要同时满足高层语义描述（如"悲伤地行走"）和精确运动学约束（如特定路径或关节角度）的场景。其高效的单层token表示和扩散优化机制，为实时交互式运动生成系统提供了计算可行的高质量解决方案。
