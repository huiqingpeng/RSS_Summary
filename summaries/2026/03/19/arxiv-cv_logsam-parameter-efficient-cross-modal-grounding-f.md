---
title: "LoGSAM: Parameter-Efficient Cross-Modal Grounding for MRI Segmentation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17576"
published: "2026-03-19"
summarized: "2026-03-19T15:14:24.342024"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了LoGSAM，一种参数高效的跨模态定位框架，用于MRI脑肿瘤分割。该框架将放射科医生的语音口述转换为文本提示，通过LoRA适配的Grounding DINO模型进行肿瘤定位，再利用MedSAM生成像素级分割掩码。在BRISC 2025数据集上取得了80.32%的Dice分数，并在真实德语口述的12例未见MRI扫描中达到91.7%的病例级准确率，展示了构建模块化语音到分割流程的可行性。

【方法概述 / Method】
LoGSAM采用三级流水线架构：首先使用预训练Whisper ASR模型转录并翻译放射科医生口述，经否定感知临床NLP提取肿瘤特异性文本提示；然后通过LoRA适配（仅更新5%参数）的Grounding DINO进行文本条件肿瘤定位；最后将预测的边界框作为提示输入冻结的MedSAM生成分割掩码，无需额外微调。

【实验结果 / Results】
在BRISC 2025基准测试中，以LoGSAM先验条件化的冻结MedSAM达到80.32%的SOTA Dice分数；在真实临床验证中，使用认证放射科医生的德语口述对12例未见MRI扫描进行端到端评估，取得91.7%的病例级准确率，证明了该流程在实际临床环境中的有效性。

【应用价值 / Applications】
该研究为神经外科手术规划和放疗方案制定提供了高效的自动化工具，通过语音交互实现直观的肿瘤定位与分割，显著降低了对大规模标注数据的依赖。其模块化设计和参数高效特性使其易于部署于资源受限的临床环境，为智能放射学工作流和实时手术导航系统的开发奠定了基础。
