---
title: "Automated Wicket-Taking Delivery Segmentation and Trajectory-Based Dismissal-Zone Analysis in Cricket Videos Using OCR-Guided YOLOv8"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.18405"
published: "2026-03-19"
summarized: "2026-03-19T16:27:04.652472"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本研究提出了一种自动化板球视频分析系统，用于识别 wicket-taking deliveries（导致击球手出局的投球）、检测球场和球体，并建模球体轨迹以进行赛后评估。该系统结合光学字符识别（OCR）与图像预处理技术提取记分牌信息并检测出局事件，同时采用 YOLOv8 实现球场和球体的高精度检测。基于检测结果，系统进一步建模球体轨迹以揭示与 wicket-taking deliveries 相关的区域，为轨迹导向的出局区域分析和潜在击球弱点评估提供数据支持，在多个板球比赛视频中验证了有效性。

【方法概述 / Method】

论文采用 OCR 引导的图像预处理流程（包括灰度转换、幂变换和形态学操作）从转播视频中提取记分牌信息并识别 wicket 事件。视觉理解方面，使用 YOLOv8 分别训练球场检测模型和基于迁移学习的球体检测模型，其中球体检测模型采用预训练权重进行微调以适应板球场景。

【实验结果 / Results】

球场检测模型达到 99.5% 的 mAP50 和 0.999 的精确率；球体检测模型达到 99.18% 的 mAP50、0.968 精确率和 0.978 召回率。系统在多个板球比赛视频上的实验结果表明，该方法能够有效识别 wicket-taking deliveries 并建模球体轨迹，实现出局区域的自动化分析。

【应用价值 / Applications】

该研究可应用于教练团队的战术分析、球员技术评估和数据驱动的决策支持，帮助识别击球手的弱点区域和投球手的有效投球策略。系统为板球运动提供了高效、客观的自动化分析工具，有望替代传统依赖人工慢速回放的战术评估方式，推动板球运动的智能化发展。
