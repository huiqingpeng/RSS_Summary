---
title: "MARIS: Marine Open-Vocabulary Instance Segmentation with Geometric Enhancement and Semantic Alignment"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2510.15398"
published: "2026-03-18"
summarized: "2026-03-18T18:28:01.687468"
ai_provider: "openai"
---

【论文摘要 / Abstract】

本文提出了首个大规模细粒度水下开放词汇实例分割基准数据集MARIS，包含有限的可见类别和多样化的不可见类别。针对水下场景迁移中存在的严重视觉退化（如颜色衰减）和语义不对齐问题，作者设计了统一框架，通过几何先验增强模块（GPEM）和语义对齐注入机制（SAIM）两个互补组件，在域内和跨域设置上均显著优于现有开放词汇基线方法。

【方法概述 / Method】

该框架包含两个核心组件：几何先验增强模块（GPEM）利用稳定的部件级和结构线索在视觉退化条件下保持目标一致性；语义对齐注入机制（SAIM）通过注入领域特定先验来丰富语言嵌入，缓解语义歧义并提升对不可见类别的识别能力。

【实验结果 / Results】

实验表明，所提框架在MARIS数据集的域内（In-Domain）和跨域（Cross-Domain）设置上均持续优于现有开放词汇基线方法，为水下感知研究奠定了坚实基础。

【应用价值 / Applications】

该研究可应用于水下机器人视觉、海洋生态监测、水下考古探测等场景，解决了传统闭集分割方法无法识别新类别海洋生物的局限，为开放环境下的水下智能感知系统提供了关键技术支撑。
