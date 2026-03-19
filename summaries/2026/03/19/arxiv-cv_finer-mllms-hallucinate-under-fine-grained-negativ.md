---
title: "FINER: MLLMs Hallucinate under Fine-grained Negative Queries"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2603.17662"
published: "2026-03-19"
summarized: "2026-03-19T15:15:37.404082"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文揭示了多模态大语言模型（MLLMs）在细粒度否定查询下容易产生幻觉的问题，现有基准测试主要关注粗粒度图像相关问题，未能充分覆盖这一挑战。研究提出了FINER（细粒度否定查询）框架及两个新基准FINER-CompreCap和FINER-DOCCI，系统分析了多对象、多属性、多关系和"what"类问题四种场景下的幻觉现象。基于研究发现，作者开发了FINER-Tuning方法，通过直接偏好优化（DPO）在FINER风格数据上进行微调，在多个前沿MLLM上实现了显著的性能提升。

【方法概述 / Method】
FINER-Tuning采用直接偏好优化（DPO）技术，利用FINER-inspired数据对模型进行微调，使模型学会区分图像中真实存在的元素与细粒度不匹配的内容。该方法通过构建包含细粒度否定查询的偏好数据对，训练模型在面对复杂、精细的图像-文本不匹配情况时做出更准确判断。

【实验结果 / Results】
在InternVL3.5-14B模型上，FINER-Tuning实现了高达24.2%的幻觉抑制增益；同时，该方法在八个现有幻觉测试套件上均取得性能提升，并在六个通用多模态基准上增强了模型的整体多模态能力。实验表明，针对细粒度否定查询的专门优化能够带来广泛的泛化效益。

【应用价值 / Applications】
该研究为开发更可靠的视觉-语言交互系统提供了重要工具，特别适用于需要精确图像理解的应用场景，如医疗影像分析、自动驾驶视觉感知、内容审核和视觉问答系统等。FINER基准和调优方法可帮助研究者和工程师系统性地评估和改进MLLM在复杂真实场景中的幻觉问题，提升模型的实用性和可信度。
