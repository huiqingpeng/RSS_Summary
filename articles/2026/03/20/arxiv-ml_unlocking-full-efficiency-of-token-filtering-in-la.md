---
title: "Unlocking Full Efficiency of Token Filtering in Large Language Model Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2502.00340"
published: "2026-03-20"
fetched: "2026-03-20T14:05:15.317654"
---

Computer Science > Machine Learning
[Submitted on 1 Feb 2025 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Unlocking Full Efficiency of Token Filtering in Large Language Model Training
View PDF HTML (experimental)Abstract:Token filtering has been proposed to enhance the utility of large language models (LLMs) by eliminating inconsequential tokens during training. While usingfewer tokens is expected to reduce computational workloads, existing methods have not yet achieved a real-world efficiency boost. This is primarily due to two factors: (1) existing work has inadequate sparsity for speedup, and (2) token filtering operates within a sparsity range that is non-standard in existing machine learning (ML) libraries and thus cannot be efficiently supported. This paper presents Centrifuge, a system that leverages algorithm and system co-design to unleash the full efficiency of token filtering in LLM training. At the algorithm level, Centrifuge filters activations of inconsequential tokens in the attention backward kernel to amplify the sparsity in backward computation. At the system level, Centrifuge proposes an automatic workflow that transforms sparse GEMM into dimension-reduced dense GEMM for optimized efficiency using standard ML libraries. Evaluations on models with various scales--from 1.1B to 40B--demonstrate that Centrifuge reduces backpropagation time by up to 49.9\% and end-to-end training time by up to 34.7\% when filtering 50\% of tokens. Utility assessments indicate that Centrifuge preserves the utility benefits of token filtering and significantly enhances model performance by up to 26.6\% compared to standard training. Centrifuge is designed for seamless integration into existing LLM training frameworks, enabling systems already utilizing token filtering to accelerate training with just one line of code.
Submission history
From: Di Chai [view email][v1] Sat, 1 Feb 2025 06:57:01 UTC (1,511 KB)
[v2] Thu, 19 Mar 2026 03:23:04 UTC (629 KB)
Current browse context:
cs.LG
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
Papers with Code (What is Papers with Code?)
ScienceCast (What is ScienceCast?)
Demos
Recommenders and Search Tools
Influence Flower (What are Influence Flowers?)
CORE Recommender (What is CORE?)
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
