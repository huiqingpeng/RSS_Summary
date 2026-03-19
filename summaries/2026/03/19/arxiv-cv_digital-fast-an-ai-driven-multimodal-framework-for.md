---
title: "Digital FAST: An AI-Driven Multimodal Framework for Rapid and Early Stroke Screening"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2601.11896"
published: "2026-03-19"
summarized: "2026-03-19T16:30:05.974232"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究提出了一种基于F.A.S.T.评估的快速、无创多模态深度学习框架，用于自动脑卒中二元筛查。该方法整合面部表情、语音信号和上肢运动的互补信息，通过Transformer、Audio Spectrogram Transformer和MLP-Mixer网络分别处理三种模态，并采用注意力机制进行融合。在37名受试者的222段视频数据集上，该模型达到95.83%的准确率和96.00%的F1分数，成功检测出所有测试集中的脑卒中病例，展现了多模态学习在早期脑卒中筛查中的潜力。

【方法概述 / Method】
研究采用多模态深度学习架构：面部动态通过面部关键点特征和Transformer建模时序依赖；语音信号转换为梅尔频谱图后用Audio Spectrogram Transformer处理；上肢姿态序列通过MLP-Mixer网络建模时空运动模式。三种模态的表征通过基于注意力的融合机制整合，以学习跨模态交互。

【实验结果 / Results】
在自建数据集上的实验表明，多模态模型持续优于单模态基线，准确率达95.83%，F1分数为96.00%，灵敏度与特异性平衡良好，且成功识别了测试集中的全部脑卒中病例。结果验证了多模态学习和迁移学习在早期脑卒中筛查中的有效性。

【应用价值 / Applications】
该框架适用于院前急救场景的快速脑卒中筛查，可辅助急救人员和非专业人员在黄金救治时间内识别脑卒中症状，为及时干预争取宝贵时间。研究同时强调了构建更大规模、更具临床代表性数据集的必要性，以支持可靠的实际部署。
