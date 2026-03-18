---
title: "KidsNanny: A Two-Stage Multimodal Content Moderation Pipeline Integrating Visual Classification, Object Detection, OCR, and Contextual Reasoning for Child Safety"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.16181"
published: "2026-03-18"
summarized: "2026-03-18T18:07:57.875178"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了KidsNanny，一种面向儿童安全的两阶段多模态内容审核架构。第一阶段采用视觉Transformer与目标检测器进行快速视觉筛查（11.7毫秒），输出文本描述而非原始像素传递至第二阶段；第二阶段结合OCR与70亿参数语言模型进行上下文推理，总延迟仅120毫秒。在UnsafeBench性内容类别（1,054张图像）上的评估表明，该完整管道在准确率和F1分数上优于ShieldGemma-2和LlavaGuard等基线模型，同时在文本嵌入威胁检测上展现出更高的召回率和更低的延迟。

【方法概述 / Method】
KidsNanny采用级联式两阶段架构：第一阶段使用ViT进行图像分类并结合目标检测器提取视觉信息，生成结构化文本描述；第二阶段接收文本输出，通过OCR提取图像中的文字内容，再利用70亿参数的语言模型进行综合上下文推理。这种设计将像素级处理与语义理解分离，实现了效率与精度的平衡。

【实验结果 / Results】
第一阶段单独运行达到80.27%准确率和85.39% F1分数，显著优于视觉基线（59.01%-77.04%准确率）；完整两阶段管道达到81.40%准确率和86.16% F1分数，延迟仅120毫秒，而ShieldGemma-2为64.80%准确率/1,136毫秒，LlavaGuard为80.36%准确率/4,138毫秒。在文本关键型子集（44张图像）上，KidsNanny实现100%召回率（25/25正例）和75.76%精确率，优于ShieldGemma-2的84%召回率和60%精确率。

【应用价值 / Applications】
KidsNanny可部署于社交媒体平台、儿童教育应用及内容分发网络，实现实时有害内容过滤，保护未成年人网络安全。其低延迟特性（120毫秒）适合高吞吐量在线场景，而模块化架构便于根据监管要求灵活调整审核策略。该研究为高效、可解释的儿童安全内容审核系统提供了可复用的技术框架和评估方法论。
