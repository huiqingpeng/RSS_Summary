---
title: "Med-DualLoRA: Local Adaptation of Foundation Models for 3D Cardiac MRI"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.10967"
published: "2026-03-18"
summarized: "2026-03-18T19:03:30.826638"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Med-DualLoRA，一种用于3D心脏MRI（CMR）疾病检测的联邦参数高效微调框架，旨在解决基础模型在多中心非独立同分布（non-IID）数据下的联邦微调挑战。该方法通过加性分解将全局共享的低秩适应（LoRA）与本地私有LoRA模块分离，在保护隐私的同时实现个性化适应。实验表明，Med-DualLoRA在ACDC和M&Ms多中心数据集上取得了显著优于其他联邦PEFT基线的性能（平衡准确率0.768，特异性0.612），同时大幅降低通信开销。

【方法概述 / Method】
Med-DualLoRA采用双LoRA分解策略，将适配器参数拆分为全局共享组件和本地私有组件，两者均在本地训练但仅聚合全局部分。该方法仅需微调两个Transformer块即可保持性能，通过选择性参数共享实现高效个性化。框架在联邦学习设置下运行，每个数据供应商作为独立客户端，确保本地适配器不离开站点。

【实验结果 / Results】
在基于3D电影CMR基础模型的多中心疾病检测任务中，Med-DualLoRA相比其他联邦PEFT基线实现了统计显著的改进。关键指标包括平衡准确率0.768和特异性0.612，同时通过仅共享全局LoRA组件将通信成本降至最低。消融实验证实，仅适应两个Transformer块即可在效率与性能间取得最佳平衡。

【应用价值 / Applications】
该研究为临床环境下医学基础模型的隐私保护部署提供了可扩展解决方案，特别适用于多中心医院协作场景。Med-DualLoRA使各机构能在不共享原始数据的前提下联合优化模型，同时保留针对本地患者群体的个性化适应能力，对推动公平、高效的医疗AI系统具有重要实践意义。
