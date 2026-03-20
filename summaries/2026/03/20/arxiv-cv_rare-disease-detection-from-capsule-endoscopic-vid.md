---
title: "RARE disease detection from Capsule Endoscopic Videos based on Vision Transformers"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.18045"
published: "2026-03-20"
summarized: "2026-03-20T15:05:27.868425"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本研究针对胶囊内镜视频（CEV）的多标签分类任务，参与Gastro Competition竞赛，旨在检测17种消化道解剖结构和病变。研究团队采用基于Transformer的深度学习网络进行微调，使用Google Vision Transformer（ViT）作为基础模型。然而，该方法在测试集上表现较差，mAP@0.5仅为0.0205，mAP@0.95为0.0196，表明模型在罕见疾病检测任务中面临重大挑战。

【方法概述 / Method】
研究采用Google Vision Transformer（ViT）作为主干网络，配置为batch size 16和224×224输入分辨率。模型针对17类标签进行多标签分类微调，包括消化道各部位（口腔、食管、胃、小肠、结肠等）及多种病变（活动性出血、血管扩张、糜烂、溃疡等）。

【实验结果 / Results】
在包含三个视频的测试集上，模型整体性能显著偏低：mAP@0.5为0.0205，mAP@0.95为0.0196。这一结果表明，直接应用标准ViT模型于胶囊内镜视频的多标签罕见疾病检测任务效果不佳，可能存在类别不平衡、视频时序信息利用不足或微调策略不当等问题。

【应用价值 / Applications】
本研究揭示了现有Vision Transformer方法在胶囊内镜视频分析中的局限性，为后续改进提供了基线参考。其探索方向对自动化消化道疾病筛查具有临床意义，有望辅助胃肠科医生提高罕见病变的检出率，减少漏诊风险，推动胶囊内镜技术的智能化诊断发展。
