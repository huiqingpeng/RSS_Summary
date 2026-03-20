---
title: "QualitEye: Public and Privacy-preserving Gaze Data Quality Verification"
source: "arXiv Computer Vision"
url: "https://arxiv.org/abs/2506.05908"
published: "2026-03-20"
summarized: "2026-03-20T16:19:48.441693"
ai_provider: "openai"
---

【论文摘要 / Abstract】
本文提出了QualitEye——首个用于验证基于图像的眼动数据质量的方法。该方法采用一种新的眼动图像语义表示，在包含验证所需信息的同时排除无关信息，以实现更好的领域自适应。QualitEye支持两种场景：公开场景（各方可自由交换数据）和隐私保护场景（各方无法泄露原始数据，也无法通过改进的私有集合求交协议推断他人的眼动特征/标签）。在MPIIFaceGaze和GazeCapture数据集上的评估表明，该方法实现了高质量验证性能，且隐私保护版本仅带来较小的运行时开销。

【方法概述 / Method】
QualitEye的核心是一种新颖的眼动图像语义表示方法，该表示仅保留数据质量验证所需的关键信息，同时过滤掉与验证无关的敏感信息（如具体的注视标签）。对于隐私保护场景，作者采用改进的私有集合求交（Private Set Intersection）密码学协议，确保多方协作验证过程中原始数据不泄露，且无法反推其他参与方的眼动特征或标签。

【实验结果 / Results】
在MPIIFaceGaze和GazeCapture两个公开眼动数据集上的实验表明，QualitEye能够有效验证眼动数据质量，达到较高的验证准确率。隐私保护版本在保持相近验证性能的同时，仅引入了较小的计算开销，证明了该方法在实际应用中的可行性。

【应用价值 / Applications】
QualitEye可应用于大规模眼动数据集的质量控制，特别是在需要多方协作的数据收集场景中（如跨机构医疗眼动研究、众包眼动数据平台）。其隐私保护特性使其适用于对数据敏感性要求高的领域，如临床诊断、用户行为分析等，为机器学习、人机交互和密码学交叉领域的眼动分析新方法奠定了基础。
