---
title: "Modeling Overlapped Speech with Shuffles"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17769"
published: "2026-03-19"
summarized: "2026-03-19T13:15:17.493110"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出使用洗牌（shuffle）操作对并行数据流（如重叠语音）进行建模。核心贡献包括：利用洗牌积（shuffle product）和部分序有限状态自动机（FSA）实现重叠语音的对齐与说话人归属转录；通过在所有可能的序列化上边缘化来训练模型；并首次实现了多说话人录音的单遍对齐。该方法在合成LibriSpeech重叠数据上进行了评估，所有算法均基于k2/Icefall实现。

【方法概述 / Method】
论文采用洗牌积运算将多个并行语音流组合成统一的FSA表示，并构建部分序FSA以施加时间约束、降低图规模。训练时以FSA的总得分作为损失函数，在子词、词和短语级别对所有可能的重叠序列序列化进行边缘化，同时直接建模（token, speaker）元组来处理说话人归属问题。

【实验结果 / Results】
该方法在合成的LibriSpeech重叠数据上进行了评估，实现了单遍Viterbi对齐。论文声称这是首个支持多说话人录音单遍对齐的算法，但具体数值指标（如WER、DER等）在提供的摘要中未明确给出。

【应用价值 / Applications】
该技术可直接应用于会议转录、多人对话识别等真实场景中的重叠语音处理，解决了传统方法需要多遍解码或复杂后处理的痛点。基于k2/Icefall的开源实现也为语音识别社区提供了可复用的工具，有望推动端到端重叠语音识别系统的实用化部署。
