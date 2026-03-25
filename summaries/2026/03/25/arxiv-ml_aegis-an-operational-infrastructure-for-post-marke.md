---
title: "AEGIS: An Operational Infrastructure for Post-Market Governance of Adaptive Medical AI Under US and EU Regulations"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22322"
published: "2026-03-25"
summarized: "2026-03-26T07:11:08.554459"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了AEGIS（AI/ML Evaluation and Governance Infrastructure for Safety），一个适用于任何医疗AI系统的治理框架，旨在确保机器学习医疗系统的安全性同时支持持续改进。AEGIS通过三个模块（数据同化与重训练、模型监控、条件决策）将FDA的预定变更控制计划（PCCP）和欧盟AI法案第43(4)条的规定转化为可执行的治理程序。该框架采用四类别部署决策分类法（批准、条件批准、临床审查、拒绝）并配备独立的市场后监测（PMS）警报信号，能够检测"无可用部署模型且已发布模型同时处于风险中"的关键状态。

【方法概述 / Method】
AEGIS包含三个核心模块：数据集同化与重训练模块处理新数据的整合和模型更新；模型监控模块持续追踪模型性能；条件决策模块基于预设规则输出部署决策。框架采用四类别决策分类法（APPROVE、CONDITIONAL APPROVAL、CLINICAL REVIEW、REJECT），并引入独立的ALARM信号机制标识关键风险状态，实现监管合规要求的技术落地。

【实验结果 / Results】
研究在脓毒症预测（电子健康记录）和脑肿瘤分割（医学影像）两个异构临床场景中验证了AEGIS。在脓毒症案例的11次模拟迭代中，AEGIS产生了8次批准、1次条件批准、1次临床审查和1次拒绝决策，完整覆盖了所有决策类别；ALARM信号在第8和第10次迭代触发，成功识别了关键风险状态。AEGIS能够在可观测的性能退化之前检测到模型漂移。

【应用价值 / Applications】
AEGIS为自适应医疗AI的安全持续学习提供了可操作的治理基础设施，帮助医疗机构和AI开发商在符合美国和欧盟监管要求的前提下实现模型的迭代更新。该框架的模块化设计使其可配置于多样化的临床应用场景，降低合规成本的同时保障患者安全，对推动医疗AI从静态审批向动态治理转型具有重要实践意义。
