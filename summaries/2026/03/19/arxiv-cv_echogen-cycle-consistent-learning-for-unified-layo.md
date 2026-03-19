---
title: "EchoGen: Cycle-Consistent Learning for Unified Layout-Image Generation and Understanding"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18001"
published: "2026-03-19"
summarized: "2026-03-19T16:20:39.132753"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出 EchoGen，一个统一的布局到图像生成与图像定位（image grounding）框架，能够生成布局准确且高度符合文本描述（如空间关系）的图像，同时实现稳健的图像定位。作者认为图像定位任务具备强大的文本和布局理解能力，可以弥补布局到图像生成中的相应不足；而生成的图像内容多样性又能增强图像定位的鲁棒性。通过渐进式训练策略（并行多任务预训练、双任务联合优化、循环强化学习），EchoGen 在两项任务上均取得最先进性能，并展现出明显的协同增益。

【方法概述 / Method】

EchoGen 采用三阶段渐进训练策略：首先，并行多任务预训练（PMTP）阶段通过共享 token 为模型赋予两项任务的基本能力并加速训练；其次，双任务联合优化（DJO）阶段利用任务对偶性依次整合两项任务，实现统一优化；最后，循环强化学习（Cycle RL）阶段以一致性约束作为奖励、借助 GRPO 策略消除对视觉监督的依赖，显著提升模型的统一能力。

【实验结果 / Results】

大量实验表明，EchoGen 在布局到图像生成和图像定位基准测试上均达到最先进的性能，且联合优化两项任务带来了清晰的协同增益（synergistic gains）。

【应用价值 / Applications】

EchoGen 可应用于需要精确控制图像布局与内容一致性的场景，如广告设计、游戏资产生成、数据增强等；同时其统一的生成-理解能力也为图像编辑、视觉问答等需要双向视觉-语言推理的任务提供了新的技术基础。
