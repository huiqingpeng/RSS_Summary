---
title: "HOMEY: Heuristic Object Masking with Enhanced YOLO for Property Insurance Risk Detection"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18502"
published: "2026-03-20"
summarized: "2026-03-20T15:10:33.100664"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了HOMEY（Heuristic Object Masking with Enhanced YOLO），一种用于财产保险风险检测的新型目标检测框架。该框架结合YOLO与领域特定的掩码机制和自定义损失函数，能够检测17类财产风险（包括结构损坏、维护疏忽和责任隐患）。实验表明，HOMEY在保持快速推理的同时，检测精度和可靠性均优于基线YOLO模型，为可扩展的AI驱动财产保险工作流程奠定了基础。

【方法概述 / Method】
HOMEY的核心创新包括两方面：一是启发式对象掩码（heuristic object masking），用于增强杂乱背景中的弱信号；二是风险感知损失校准（risk-aware loss calibration），用于平衡类别不平衡并引入严重程度加权。该方法基于YOLO架构进行增强，专门针对房地产影像中的风险检测任务进行优化。

【实验结果 / Results】
论文在真实世界房产图像数据集上进行实验，结果显示HOMEY相比基线YOLO模型取得了更优的检测精度和可靠性，同时保持了快速的推理速度。具体量化指标未在摘要中详细披露，但强调了该方法在准确性和效率之间的有效平衡。

【应用价值 / Applications】
HOMEY可直接应用于房地产评估、保险承保和保险运营自动化领域，实现可解释且成本高效的风险分析。该技术为财产保险行业提供了可扩展的AI解决方案，能够自动识别房屋结构缺陷、维护问题和安全隐患，从而降低人工勘察成本并提升风险评估的客观性和效率。
