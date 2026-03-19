---
title: "EmergeNav: Structured Embodied Inference for Zero-Shot Vision-and-Language Navigation in Continuous Environments"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16947"
published: "2026-03-19"
summarized: "2026-03-19T14:22:10.329233"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了EmergeNav，一个用于连续环境中零样本视觉语言导航（VLN-CE）的结构化具身推理框架。作者指出，现有视觉语言模型（VLMs）的主要瓶颈并非缺乏知识，而是缺乏组织指令跟随、感知 grounding、时间进度和阶段验证的执行结构。EmergeNav通过显式的执行层次结构将VLM的先验知识转化为稳定的具身导航行为，在仅使用开源VLM骨干网络且无需任务特定训练的情况下，取得了显著的性能提升。

【方法概述 / Method】
EmergeNav采用"Plan-Solve-Transition"层次结构实现阶段化执行，结合GIPE（Goal-Conditioned Instructional Perceptual Extraction）进行目标条件感知提取，利用对比双记忆推理进行进度grounding，并采用角色分离的双视场（Dual-FOV）感知实现时间对齐的局部控制和边界验证。该框架将连续VLN形式化为结构化的具身推理问题，无需显式地图、图搜索或航点预测器。

【实验结果 / Results】
在VLN-CE基准测试上，EmergeNav展现出强大的零样本性能：使用Qwen3-VL-8B达到30.00%的成功率（SR），使用Qwen3-VL-32B达到37.00%的SR。这些结果表明，显式的执行结构是将VLM先验知识转化为稳定具身导航行为的关键要素，且该框架完全不依赖任务特定训练、显式地图或专用航点预测模块。

【应用价值 / Applications】
EmergeNav为家庭服务机器人、智能导览系统和自主移动平台提供了无需大量任务特定训练即可部署的导航解决方案。该框架的零样本特性使其能够快速适应新环境和新指令，降低了具身AI系统的部署成本；同时，其模块化的结构化设计为将基础模型的语义理解能力与稳定的机器人执行相结合提供了可扩展的技术路径。
