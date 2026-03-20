---
title: "Redundancy-as-Masking: Formalizing the Artificial Age Score (AAS) to Model Memory Aging in Generative AI"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.01242"
published: "2026-03-20"
summarized: "2026-03-20T14:17:14.392846"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了"人工年龄评分"（Artificial Age Score, AAS），一种基于对数缩放和熵信息的记忆老化度量指标，用于量化生成式AI中因结构不对称导致的记忆性能衰退。该指标在温和且与模型无关的假设下被严格证明为良定义、有界且单调的。通过在ChatGPT-5上进行的25天双语研究，作者发现持久会话中模型能保持语义和情景记忆连续性（AAS趋近理论最小值），而会话重置则导致情景记忆断裂、AAS急剧上升，从而验证了其作为诊断工具的有效性。

【方法概述 / Method】
AAS基于"冗余即掩码"（Redundancy-as-Masking）框架构建，将冗余解释为重叠信息以降低惩罚质量；本研究采用冗余中性假设（R=0）以获得保守上界。评分从可观测的召回行为中导出，融合了香农信息论中的熵与冗余概念，并借鉴了冯·诺依曼的自动机理论和图灵的行为主义智能观。

【实验结果 / Results】
25天实验分为无状态（stateless）和持久（persistent）两种交互阶段：持久会话中模型稳定回忆语义线索（如星期名称）和情景细节（如实验序号），AAS维持在低位；会话重置后语义一致性得以保留，但情景连续性崩溃，AAS显著攀升。结果支持AAS作为结构年轻度与记忆老化的可靠指标。

【应用价值 / Applications】
AAS为评估对话式AI系统的记忆退化提供了理论扎实、任务无关的诊断工具，可应用于聊天机器人的长期交互稳定性监测、模型版本迭代中的记忆性能基准测试，以及设计更具持续情境感知能力的生成式AI架构。
