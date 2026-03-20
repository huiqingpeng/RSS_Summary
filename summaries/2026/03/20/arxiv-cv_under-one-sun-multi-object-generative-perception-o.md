---
title: "Under One Sun: Multi-Object Generative Perception of Materials and Illumination"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.19226"
published: "2026-03-20"
summarized: "2026-03-20T16:06:29.582042"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Multi-Object Generative Perception (MultiGP)，一种生成式逆渲染方法，用于从单张图像中随机采样所有辐射成分（反射率、纹理和光照）。该方法的核心洞见是：同一场景中的物体虽然纹理和反射率各异，但共享相同的光照条件。MultiGP利用这一共识约束，通过级联端到端架构、协调引导扩散收敛、轴向注意力机制和纹理提取ControlNet四项关键技术，实现了对多物体场景中个体材质属性与共同光照的联合估计。

【方法概述 / Method】
MultiGP采用级联端到端架构，结合图像空间和角度空间解耦策略；引入"协调引导"机制确保扩散模型收敛到一致的单一光照估计；应用轴向注意力促进不同反射率物体之间的信息交互；并设计纹理提取ControlNet在保留高频纹理细节的同时实现与估计光照的解耦。

【实验结果 / Results】
实验结果表明，MultiGP能够有效利用多物体外观在空间域和频率域上的互补特性，成功恢复各个物体的独立纹理和反射率属性，同时准确估计场景的共同光照条件，解决了辐射解耦问题中的固有歧义性。

【应用价值 / Applications】
该研究可应用于计算机图形学中的材质编辑、场景重光照、虚拟物体插入等任务，为增强现实、影视后期制作和数字内容创作提供技术支持，实现从单张真实图像中重建可编辑的物理正确场景表示。
