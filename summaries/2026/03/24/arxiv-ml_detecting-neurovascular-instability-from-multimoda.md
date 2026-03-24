---
title: "Detecting Neurovascular Instability from Multimodal Physiological Signals Using Wearable-Compatible Edge AI: A Responsible Computational Framework"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20442"
published: "2026-03-24"
summarized: "2026-03-25T07:09:54.082081"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了Melaguard，一种轻量级多模态机器学习框架（Transformer-lite架构，120万参数，4头自注意力），用于在结构性脑卒中病理发生前，通过可穿戴设备兼容的生理信号检测神经血管不稳定性（NVI）。该模型融合心率变异性（HRV）、外周灌注指数、血氧饱和度（SpO2）和双侧相位相干性，构建复合NVI评分，专为边缘计算设计（Cortex-M4上最坏执行时间≤4毫秒）。研究通过三阶段独立验证表明，多模态融合始终优于单模态基线方法，为社区规模卒中筛查提供了可行路径。

【方法概述 / Method】
Melaguard采用Transformer-lite神经网络架构，通过自注意力机制融合四种生理信号模态：HRV、外周灌注指数、SpO2和双侧相位相干性，输出标准化的NVI评分。模型针对资源受限的边缘设备进行优化，参数量控制在120万，确保在Cortex-M4微控制器上实现亚4毫秒的实时推理，满足可穿戴设备的功耗和延迟约束。

【实验结果 / Results】
三阶段验证显示：（1）合成基准测试（n=10,000）AUC达0.88；（2）临床队列PhysioNet CVES（n=172）中，Transformer-lite AUC为0.755，显著优于LSTM（0.643）、随机森林（0.665）和SVM（0.472），且HRV-SDNN指标可有效区分卒中患者（p=0.011）；（3）PPG信号验证中，脉搏率与ECG金标准相关系数r=0.748，HRV替代指标r=0.690。跨模态验证（PPG-BP, n=219）进一步证实PPG形态学特征对脑血管疾病的分类AUC达0.923。

【应用价值 / Applications】
该研究为卒中预防提供了社区级筛查的技术基础，使连续、无创的神经血管监测通过消费级可穿戴设备成为可能。边缘AI设计确保患者隐私数据本地处理，降低云端传输的延迟和安全风险，特别适用于资源有限地区的早期卒中风险预警和慢性病管理，有望显著降低全球每年1220万新发卒中事件的健康负担。
