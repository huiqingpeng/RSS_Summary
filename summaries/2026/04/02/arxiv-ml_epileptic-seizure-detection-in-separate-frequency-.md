---
title: "Epileptic Seizure Detection in Separate Frequency Bands Using Feature Analysis and Graph Convolutional Neural Network (GCN) from Electroencephalogram (EEG) Signals"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00163"
published: "2026-04-02"
summarized: "2026-04-03T07:17:48.967560"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究提出了一种基于频率感知的癫痫发作检测框架，通过将EEG信号分解为五个频带（delta、theta、alpha、低beta、高beta）并提取11种判别性特征，利用图卷积神经网络（GCN）建模电极间的空间依赖关系。在CHB-MIT头皮EEG数据集上的实验表明，该方法在alpha频带达到99.7%的准确率，整体宽带准确率为99.01%，显著优于传统宽带EEG方法，同时提升了可解释性和神经生理学相关性。

【方法概述 / Method】
该方法首先将原始EEG信号分解为五个独立频带，从每个频带提取11种时域和频域特征；然后将EEG电极构建为图结构，以电极作为节点、空间关系作为边，采用GCN捕获通道间的空间依赖模式进行癫痫发作分类。

【实验结果 / Results】
各频带检测准确率分别为：delta（97.1%）、theta（97.13%）、alpha（99.5%）、低beta（99.7%）、高beta（51.4%），表明中频带（alpha和低beta）具有最强的癫痫发作判别能力；整体宽带EEG分析准确率达99.01%，揭示了频率特异性的癫痫发作模式。

【应用价值 / Applications】
该研究为临床癫痫诊断提供了高准确且可解释的自动化检测工具，特别是通过识别中频带的关键作用，有助于开发针对性的神经调控治疗策略；频率分解的方法还可拓展至其他神经精神疾病（如睡眠障碍、认知障碍）的EEG分析应用中。
