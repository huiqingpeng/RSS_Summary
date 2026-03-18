---
title: "CRIMSON: A Clinically-Grounded LLM-Based Metric for Generative Radiology Report Evaluation"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.06183"
published: "2026-03-18"
summarized: "2026-03-18T19:07:22.364300"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了CRIMSON，一种基于临床的LLM评估框架，用于胸部X光报告生成任务。该框架从诊断正确性、上下文相关性和患者安全性三个维度评估报告，并整合患者年龄、临床指征等完整临床上下文，避免正常或临床无关发现对评分的过度影响。CRIMSON通过临床显著性分级（紧急、需行动非紧急、无需行动、预期/良性）实现错误严重性感知的加权评分，并在多个基准测试中展现出与放射科专家判断的高度一致性。

【方法概述 / Method】
CRIMSON采用基于指南的决策规则，将错误分类为涵盖虚假发现、遗漏发现及八种属性级错误（位置、严重程度、测量值、诊断过度解读等）的综合分类体系。每个发现根据与心胸放射科主治医师合作开发的指南被分配临床显著性等级，从而实现对临床后果严重错误的优先加权。该方法利用大型语言模型进行自动化评估，同时结合完整的临床上下文信息。

【实验结果 / Results】
在ReXVal数据集上，CRIMSON与六位委员会认证放射科医师标注的临床显著错误计数显示出强相关性（Kendall's τ = 0.61-0.71，Pearson's r = 0.71-0.84）。在新增的RadJudge挑战性通过-失败场景基准和包含100+配对案例的RadPref放射科医师偏好基准中，CRIMSON均展现出与专家判断的最强一致性，优于现有评估指标。

【应用价值 / Applications】
CRIMSON可用于自动化评估放射学报告生成系统的临床质量，支持AI辅助诊断工具的开发与监管审批。该框架及其发布的基准测试（RadJudge、RadPref）和微调MedGemma模型为可复现的医学报告生成评估提供了标准化工具，有助于推动临床安全的医疗AI系统部署，减少因评估指标与临床实际脱节而导致的患者安全风险。
