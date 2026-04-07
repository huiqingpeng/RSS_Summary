---
title: "D-Legion: A Scalable Many-Core Architecture for Accelerating Matrix Multiplication in Quantized LLMs"
source: "arXiv Computer Architecture"
url: "https://arxiv.org/abs/2602.06252"
published: "2026-04-07"
fetched: "2026-04-08T07:02:27.033592"
---

Computer Science > Hardware Architecture
[Submitted on 5 Feb 2026 (v1), last revised 4 Apr 2026 (this version, v2)]
Title:D-Legion: A Scalable Many-Core Architecture for Accelerating Matrix Multiplication in Quantized LLMs
View PDF HTML (experimental)Abstract:The performance gains obtained by large language models (LLMs) are closely linked to their substantial computational and memory requirements. Quantized LLMs offer significant advantages with extremely quantized models, motivating the development of specialized architectures to accelerate their workloads. This paper proposes D-Legion, a novel scalable many-core architecture, designed using many adaptive-precision systolic array cores, to accelerate matrix multiplication in quantized LLMs. The proposed architecture consists of a set of Legions where each Legion has a group of adaptive-precision systolic arrays. D-Legion supports multiple computation modes, including quantized sparse and dense matrix multiplications. The block structured sparsity is exploited within a fully-sparse, or partially-sparse windows. In addition, memory accesses of partial summations (psums) are spatially reduced through parallel accumulators. Furthermore, data reuse is maximized through optimized scheduling techniques by multicasting matrix tiles across the Legions. A comprehensive design space exploration is performed in terms of Legion/core granularity to determine the optimal Legion configuration. Moreover, D-Legion is evaluated on attention workloads from two BitNet models, delivering up to 8.2$\times$ lower latency, up to 3.8$\times$ higher memory savings, and up to 3$\times$ higher psum memory savings compared to state-of-the-art work. D-Legion, with eight Legions and 64 total cores, achieves a peak throughput of 135.68 TOPS at a frequency of 1 GHz. A scaled version of D-Legion, with 32 Legions, is compared to Google TPUv4i, achieving up to 2.5$\times$ lower total latency, up to 2.3$\times$ higher total throughput, and up to 2.7$\times$ higher total memory savings.
Submission history
From: Ahmed Abdelmaksoud [view email][v1] Thu, 5 Feb 2026 23:02:23 UTC (9,121 KB)
[v2] Sat, 4 Apr 2026 16:57:05 UTC (9,121 KB)
References & Citations
export BibTeX citation
Loading...
Bibliographic and Citation Tools
Bibliographic Explorer (What is the Explorer?)
Connected Papers (What is Connected Papers?)
Litmaps (What is Litmaps?)
scite Smart Citations (What are Smart Citations?)
Code, Data and Media Associated with this Article
alphaXiv (What is alphaXiv?)
CatalyzeX Code Finder for Papers (What is CatalyzeX?)
DagsHub (What is DagsHub?)
Gotit.pub (What is GotitPub?)
Hugging Face (What is Huggingface?)
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
