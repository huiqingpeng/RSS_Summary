---
title: "Newton Adds Contact-Rich Manipulation and Locomotion Capabilities for Industrial Robotics"
source: "NVIDIA Developer Blog"
url: "https://developer.nvidia.com/blog/newton-adds-contact-rich-manipulation-and-locomotion-capabilities-for-industrial-robotics/"
published: "2026-03-16"
summarized: "2026-03-17T07:08:23.794602"
ai_provider: "openai"
---

【是什么 / What it is】

Newton 是由 NVIDIA、Google DeepMind 和 Disney Research 联合发起的开源 GPU 加速物理仿真引擎，于 2026 年 NVIDIA GTC 大会发布 1.0 正式版。它基于 NVIDIA Warp 和 OpenUSD 构建，专为机器人灵巧操作与移动任务设计，能够同时兼顾仿真速度与物理真实性，解决了传统引擎在速度与精度之间的权衡难题。

Newton is an open-source, GPU-accelerated physics simulator launched by NVIDIA, Google DeepMind, and Disney Research as a Linux Foundation project, with version 1.0 GA announced at NVIDIA GTC 2026. Built on NVIDIA Warp and OpenUSD, it is designed for dexterous manipulation and locomotion tasks in robotics, achieving both high simulation speed and physical realism that traditional engines typically trade off.

---

【为什么重要 / Why it matters】

工业机器人和物理 AI 的发展瓶颈在于仿真与现实之间的差距（sim-to-real gap），而 Newton 通过多求解器架构、可变形体仿真、高保真接触建模等能力显著缩小了这一差距。其模块化设计支持 MJCF/URDF/OpenUSD 等多种格式，并与 NVIDIA Isaac 生态深度集成，有望加速从机械设计、策略训练到真实部署的全流程，推动物理 AI 的规模化应用。

The sim-to-real gap has been a critical bottleneck for industrial robotics and physical AI, and Newton addresses this through multi-solver architecture, deformable body simulation, and high-fidelity contact modeling. Its modular design supporting multiple robotics formats and deep integration with the NVIDIA Isaac ecosystem promises to accelerate the entire pipeline from mechanical design through policy training to real-world deployment, enabling scaled adoption of physical AI.

---

【我能用什么 / How I can use it】

开发者可将 Newton 作为 Isaac Lab/Sim 的后端，利用其 GPU 并行能力大规模训练 RL/模仿学习策略，尤其适用于需要精细接触感知的装配、抓取等工业场景；机械设计师可借助 Kamino 求解器验证复杂闭链机构（如多足机器人）而无需担心可仿真性；还可结合 VBD/iMPM 求解器开展线缆、布料、颗粒材料等可变形体的操作与移动研究，并通过 OpenUSD 实现资产与流程的标准化复用。

Developers can use Newton as a backend for Isaac Lab/Sim to train RL/imitation learning policies at GPU scale, particularly for industrial tasks requiring fine contact perception like assembly and grasping; mechanical designers can leverage the Kamino solver to validate complex closed-chain mechanisms like legged robots without simulatability concerns; researchers can combine VBD/iMPM solvers for deformable manipulation and locomotion with cables, cloth, and granular materials, while standardizing asset reuse through OpenUSD.
