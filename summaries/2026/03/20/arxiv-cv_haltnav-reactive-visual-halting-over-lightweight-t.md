---
title: "HaltNav: Reactive Visual Halting over Lightweight Topological Priors for Robust Vision-Language Navigation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.12696"
published: "2026-03-20"
summarized: "2026-03-20T17:04:48.550544"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了HaltNav，一种面向开放词汇、目标导向视觉语言导航（VLN）的分层导航框架。该框架利用轻量级的文本型拓扑地图osmAG（OpenStreetMap区域图）作为全局先验，结合多模态大语言模型（MLLM）进行高层任务理解和障碍感知，将全局路径转换为局部执行片段。核心创新"反应式视觉停止"（RVH）机制能够在检测到局部异常（如关闭的门或拥挤通道）时中断控制循环、更新拓扑地图并触发重规划，显著提升了长程VLN在动态环境中的鲁棒性。

【方法概述 / Method】

HaltNav采用分层架构：MLLM-based"大脑模块"负责基于osmAG的全局路径规划和指令分解，将目标转化为先验约束的子指令；底层VLN执行器完成局部视觉导航。RVH机制通过视觉感知实时检测路径阻塞，触发拓扑更新与动态重规划。为高效训练停止能力，作者设计了基于生成模型的数据合成流程，向可导航场景中注入真实障碍以扩充困难负样本。

【实验结果 / Results】

实验表明，该框架在无需繁琐语言指令的条件下优于多个基线方法，显著提升了环境变化下长程视觉语言导航的鲁棒性。通过生成模型合成的障碍数据有效增强了模型对真实阻塞场景的识别与应对能力。

【应用价值 / Applications】

该研究适用于室内服务机器人、智能导览系统等需要在动态环境中执行开放式导航指令的场景。轻量级拓扑先验降低了对精确度量地图的依赖，RVH机制使机器人能够自适应处理门状态变化、人群拥堵等实际部署中的常见异常，为可扩展、可维护的自主导航系统提供了实用解决方案。
