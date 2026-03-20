---
title: "RE-SAC: Disentangling aleatoric and epistemic risks in bus fleet control: A stable and robust ensemble DRL approach"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18396"
published: "2026-03-20"
summarized: "2026-03-20T12:11:05.057678"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文针对公交车辆驻站控制（bus holding control）问题，提出了一种鲁棒集成软演员-评论家算法（RE-SAC），用于显式解耦偶然不确定性（aleatoric uncertainty）与认知不确定性（epistemic uncertainty）。核心贡献在于通过积分概率度量（IPM）正则化和多样化Q集成网络，分别对冲这两类风险，避免了传统DRL方法将噪声误判为数据缺口导致的策略崩溃。实验表明，RE-SAC在累积奖励上显著优于标准SAC，并在稀有分布外状态下将Oracle Q值估计误差降低62%。

【方法概述 / Method】
RE-SAC采用双机制架构：针对偶然不确定性，在评论网络中引入基于积分概率度量（IPM）的权重正则化，为鲁棒贝尔曼算子提供平滑的解析下界，无需昂贵的内循环扰动；针对认知不确定性，构建多样化的Q值集成网络，对稀疏覆盖区域中过度自信的估值进行惩罚，防止集成方差将噪声错误识别为数据缺口。

【实验结果 / Results】
在真实双向公交走廊仿真环境中，RE-SAC获得最高累积奖励（约-0.4×10⁶），相比 vanilla SAC（-0.55×10⁶）提升显著。马氏距离稀有度分析证实，在高交通变异性下的稀有分布外状态中，RE-SAC将Oracle Q值估计的平均绝对误差从4343降至1647，误差降低达62%，展现出卓越的鲁棒性。

【应用价值 / Applications】
该研究可直接应用于智能公交调度系统，提升在随机交通流和动态乘客需求波动环境下的运营稳定性与可靠性。其不确定性解耦框架具有通用性，可扩展至其他存在多重不确定性来源的实时控制场景，如自动驾驶车队管理、智能交通信号控制等安全关键型强化学习应用。
