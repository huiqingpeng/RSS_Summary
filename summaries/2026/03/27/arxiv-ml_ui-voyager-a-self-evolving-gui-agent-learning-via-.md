---
title: "UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.24533"
published: "2026-03-27"
summarized: "2026-03-28T07:11:43.320119"
ai_provider: "openai"
---

【论文摘要 / Abstract】
UI-Voyager 提出了一种新型的自进化移动 GUI 智能体，通过两阶段训练框架解决现有方法从失败轨迹中学习效率低下以及长程任务稀疏奖励下信用分配模糊的问题。该框架首先采用拒绝微调（RFT）实现数据与模型的自主协同进化，随后引入群组相对自蒸馏（GRSD）从成功轨迹中构建密集步骤级监督信号来纠正失败轨迹。在 AndroidWorld 基准上的实验表明，仅 4B 参数的模型达到了 81.0% 的 Pass@1 成功率，超越人类水平性能。

【方法概述 / Method】
UI-Voyager 采用两阶段自进化训练策略：第一阶段通过 Rejection Fine-Tuning（RFT）构建数据与模型的自主闭环进化系统，持续筛选高质量成功轨迹进行迭代训练；第二阶段提出 Group Relative Self-Distillation（GRSD），通过群组 rollout 识别关键分叉点，利用成功轨迹与失败轨迹的对比构建细粒度的步骤级监督信号，实现密集奖励下的有效信用分配。

【实验结果 / Results】
在 AndroidWorld 基准测试上，UI-Voyager 的 4B 模型取得 81.0% 的 Pass@1 成功率，显著优于众多近期基线方法并超越人类水平；消融实验和案例研究进一步验证了 GRSD 机制在识别关键决策点和纠正失败轨迹方面的有效性，证明了该方法无需昂贵人工标注即可实现高效自进化。

【应用价值 / Applications】
UI-Voyager 为移动设备自动化操作提供了高性能、低成本的解决方案，可广泛应用于智能手机任务自动化、无障碍辅助技术、软件测试与质量保障等领域；其自进化特性大幅降低了对人工标注数据的依赖，为构建可持续改进的 GUI 智能体系统开辟了新的技术路径，具有重要的商业部署价值和学术研究意义。
