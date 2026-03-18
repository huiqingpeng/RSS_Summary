---
title: "AOI: Turning Failed Trajectories into Training Signals for Autonomous Cloud Diagnosis"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.03378"
published: "2026-03-18"
summarized: "2026-03-18T17:05:05.171310"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了AOI（Autonomous Operations Intelligence），一个可训练的多智能体框架，用于在安全约束下将自动化运维建模为结构化轨迹学习问题。该框架通过GRPO蒸馏专家知识到本地开源模型、采用读写分离的安全执行架构，以及创新的失败轨迹闭环演化器，解决了LLM智能体在企业SRE部署中的数据隐私、动作安全和持续学习三大挑战。在AIOpsLab基准测试上，AOI取得了66.3%的best@5成功率，较先前SOTA提升24.4个百分点；14B本地模型经训练后在63个未见故障类型任务上达到42.9% avg@1，超越Claude Sonnet 4.5。

【方法概述 / Method】

AOI框架包含三个核心组件：（1）基于GRPO的可训练诊断系统，通过组相对策略优化将专家级知识蒸馏到本地部署的开源模型，实现无需暴露敏感数据的偏好学习；（2）读写分离的执行架构，将运维轨迹解耦为观察、推理和动作三个阶段，在防止未授权状态变更的同时支持安全学习；（3）失败轨迹闭环演化器（Failure Trajectory Closed-Loop Evolver），主动挖掘失败轨迹并将其转化为纠正性监督信号，实现持续的数据增强与模型改进。

【实验结果 / Results】

实验在AIOpsLab基准的86项任务上验证了三个层级的累积增益：（1）AOI运行时本身达到66.3% best@5成功率，较先前SOTA（41.9%）提升24.4个百分点；（2）经Observer GRPO训练后，本地14B模型在63个未见故障类型的保留任务上达到42.9% avg@1，性能超越Claude Sonnet 4.5；（3）Evolver组件将37条失败轨迹转化为诊断指导，使端到端avg@5提升4.8个百分点，同时将方差降低35%。

【应用价值 / Applications】

AOI为企业级站点可靠性工程（SRE）自动化提供了可落地的技术方案，特别适用于金融、医疗等对数据隐私和系统安全有严格要求的行业场景。该框架使组织能够在本地部署开源模型进行智能运维诊断，无需将敏感数据上传至第三方API，同时通过失败轨迹的持续学习机制实现系统的自我进化，大幅降低人工运维成本并提升故障响应的自动化水平。
