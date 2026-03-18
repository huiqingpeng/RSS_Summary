---
title: "MiroThinker-1.7 & H1: Towards Heavy-Duty Research Agents via Verification"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.15726"
published: "2026-03-18"
summarized: "2026-03-18T16:07:19.666280"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了 MiroThinker-1.7，一种面向复杂长程推理任务的新型研究智能体，并进一步推出了 MiroThinker-H1，通过引入局部和全局验证机制显著增强了多步问题求解的可靠性。MiroThinker-1.7 通过强调结构化规划、情境推理和工具交互的智能体中期训练，提升了单步交互的可靠性；而 H1 版本则在推理过程中直接嵌入验证，支持中间决策的实时评估与优化，并对整体推理轨迹进行审计以确保答案的证据链完整性。在开放网络研究、科学推理和金融分析等基准测试中，MiroThinker-H1 在深度研究任务上达到了最先进的性能，同时作者还开源了 MiroThinker-1.7 及其轻量版本。

【方法概述 / Method】
MiroThinker-1.7 采用智能体中期训练（agentic mid-training）策略，重点强化结构化规划、上下文推理和工具调用能力，以实现复杂任务中的持续多步交互。MiroThinker-H1 在此基础上引入双层验证机制：局部验证用于推理过程中对中间决策进行实时评估与修正，全局验证则对整个推理轨迹进行审计，确保最终答案基于连贯的证据链。

【实验结果 / Results】
MiroThinker-H1 在覆盖开放网络研究、科学推理和金融分析的多项基准测试中，于深度研究任务上取得了当前最优性能，同时在专业领域保持了强劲表现。开源版本 MiroThinker-1.7 和 MiroThinker-1.7-mini 在显著提升效率的同时，提供了具有竞争力的研究智能体能力。

【应用价值 / Applications】
该研究可广泛应用于需要深度信息整合与可靠推理的专业场景，如学术研究辅助、金融投资分析、科学假设验证等复杂决策任务。其开源特性降低了高性能研究智能体的部署门槛，使企业和研究机构能够构建可审计、可信赖的自动化研究系统。
