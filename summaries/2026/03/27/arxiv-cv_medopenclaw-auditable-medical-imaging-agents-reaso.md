---
title: "MedOpenClaw: Auditable Medical Imaging Agents Reasoning over Uncurated Full Studies"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.24649"
published: "2026-03-27"
summarized: "2026-03-28T07:14:16.333481"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了 MEDOPENCLAW，一个可审计的运行时环境，使视觉-语言模型（VLMs）能够在标准医学工具（如 3D Slicer）中动态操作，以解决现有医学影像评估过度依赖人工筛选的 2D 图像、忽视真实临床诊断中 3D 多序列导航挑战的问题。作者同时发布了 MEDFLOWBENCH 基准测试，涵盖多序列脑部 MRI 和肺部 CT/PET 的完整研究评估。核心发现表明：尽管最先进的 LLMs/VLMs（如 Gemini 3.1 Pro 和 GPT-5.4）能够成功导航查看器完成基础任务，但当提供专业工具支持时，由于缺乏精确的空间定位能力，其性能反而下降。

【方法概述 / Method】

MEDOPENCLAW 构建了一个可审计的运行时框架，允许 VLMs 与标准医学影像查看器和工具进行交互式操作，支持三种评估轨道：仅查看器（viewer-only）、工具使用（tool-use）和开放方法（open-method）。该框架通过模拟真实临床工作流程，使智能体能够在完整的 3D 医学影像研究中主动导航、收集证据并做出决策。

【实验结果 / Results】

在 MEDFLOWBENCH 上的初步评估显示，当前最先进的模型在仅使用查看器的基础任务上表现良好，但在获得专业工具访问权限后，由于空间定位能力不足，性能出现 paradoxical degradation（反常下降）。这一发现揭示了现有 VLMs 在从静态图像感知向交互式临床工作流过渡时的关键瓶颈。

【应用价值 / Applications】

该研究为开发可审计的完整研究医学影像智能体建立了可复现的基础，有助于推动医学 AI 从简化的人工场景向真实的临床诊断环境迈进。MEDOPENCLAW 和 MEDFLOWBENCH 可支持医学影像 AI 系统的标准化评估与改进，最终提升临床决策支持系统的可靠性和实用性。
