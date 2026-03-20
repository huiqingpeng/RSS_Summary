---
title: "PREBA: Surgical Duration Prediction via PCA-Weighted Retrieval-Augmented LLMs and Bayesian Averaging Aggregation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.13275"
published: "2026-03-20"
fetched: "2026-03-20T14:13:05.406526"
---

Computer Science > Machine Learning
This paper has been withdrawn by Kanxue Li
[Submitted on 27 Feb 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:PREBA: Surgical Duration Prediction via PCA-Weighted Retrieval-Augmented LLMs and Bayesian Averaging Aggregation
No PDF available, click to view other formatsAbstract:Accurate prediction of surgical duration is pivotal for hospital resource management. Although recent supervised learning approaches-from machine learning (ML) to fine-tuned large language models (LLMs)-have shown strong performance, they remain constrained by the need for high-quality labeled data and computationally intensive training. In contrast, zero-shot LLM inference offers a promising training-free alternative but it lacks grounding in institution-specific clinical context (e.g., local demographics and case-mix distributions), making its predictions clinically misaligned and prone to instability. To address these limitations, we present PREBA, a retrieval-augmented framework that integrates PCA-weighted retrieval and Bayesian averaging aggregation to ground LLM predictions in institution-specific clinical evidence and statistical priors. The core of PREBA is to construct an evidence-based prompt for the LLM, comprising (1) the most clinically similar historical surgical cases and (2) clinical statistical priors. To achieve this, PREBA first encodes heterogeneous clinical features into a unified representation space enabling systematic retrieval. It then performs PCA-weighted retrieval to identify clinically relevant historical cases, which form the evidence context supplied to the LLM. Finally, PREBA applies Bayesian averaging to fuse multi-round LLM predictions with population-level statistical priors, yielding calibrated and clinically plausible duration estimates. We evaluate PREBA on two real-world clinical datasets using three state-of-the-art LLMs, including Qwen3, DeepSeek-R1, and HuatuoGPT-o1. PREBA significantly improves performance-for instance, reducing MAE by up to 40% and raising R^2 from -0.13 to 0.62 over zero-shot inference-and it achieves accuracy competitive with supervised ML methods, demonstrating strong effectiveness and generalization.
Submission history
From: Kanxue Li [view email][v1] Fri, 27 Feb 2026 07:19:23 UTC (1,923 KB)
[v2] Thu, 19 Mar 2026 01:00:17 UTC (1 KB) (withdrawn)
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
