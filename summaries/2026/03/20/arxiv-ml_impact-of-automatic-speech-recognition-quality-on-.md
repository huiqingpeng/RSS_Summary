---
title: "Impact of automatic speech recognition quality on Alzheimer's disease detection from spontaneous speech: a reproducible benchmark study with lexical modeling and statistical validation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18239"
published: "2026-03-20"
summarized: "2026-03-20T13:10:56.943148"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究探讨了自动语音识别（ASR）质量对阿尔茨海默病（AD）检测的影响，使用Whisper ASR转录的词汇特征在ADReSSo 2021数据集上进行诊断分析。研究发现，ASR转录质量对分类性能有统计显著性影响——Whisper-small转录本训练的模型持续优于Whisper-base，线性SVM达到0.7850以上的平衡准确率，且分类器复杂度对性能变异的影响小于ASR质量。认知正常说话者产生更多语义精确的物体和场景描述性语言，而AD患者的言语特征为模糊表达、话语标记增多和犹豫模式增加。

【方法概述 / Method】
研究采用可解释的机器学习模型（逻辑回归和线性支持向量机），基于TF-IDF文本表示，在重复5×5分层交叉验证框架下评估ASR质量的影响。实验对比了Whisper-base与Whisper-small两种ASR模型生成的转录本，并通过配对统计检验验证性能差异的显著性，同时进行了特征层面的语言学分析。

【实验结果 / Results】
Whisper-small转录本 consistently 优于Whisper-base，线性SVM达到最高平衡准确率（>0.7850），配对统计检验确认改进具有显著性。关键发现是：ASR转录质量对性能变异的影响大于分类器复杂度的影响。特征分析揭示了两组人群在词汇使用模式上的系统性差异——正常组使用更精确的实体描述词，AD组则表现出更多的模糊限定词和话语填充词。

【应用价值 / Applications】
该研究为临床语音AI系统提供了可复现的基准流程，证明高质量ASR可使简单的词汇模型无需显式声学建模即可达到有竞争力的AD检测性能。这一发现对远程医疗筛查和早期诊断工具开发具有直接指导意义，强调ASR选择是临床语音分析系统中的关键设计决策，有助于推动低成本、可解释的非侵入式认知障碍筛查技术的实际部署。
