---
title: "IA2: Alignment with ICL Activations Improves Supervised Fine-Tuning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2509.22621"
published: "2026-03-19"
fetched: "2026-03-19T14:06:53.319188"
---

Computer Science > Machine Learning
[Submitted on 26 Sep 2025 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:IA2: Alignment with ICL Activations Improves Supervised Fine-Tuning
View PDF HTML (experimental)Abstract:Supervised Fine-Tuning (SFT) is used to specialize model behavior by training weights to produce intended target responses for queries. In contrast, In-Context Learning (ICL) adapts models during inference with instructions or demonstrations in the prompt. ICL can offer better generalizability and more calibrated responses compared to SFT in data scarce settings, at the cost of more inference compute. In this work, we ask the question: Can ICL's internal computations be used to improve the qualities of SFT? We first show that ICL and SFT produce distinct activation patterns, indicating that the two methods achieve adaptation through different functional mechanisms. Motivated by this observation and to use ICL's rich functionality, we introduce ICL Activation Alignment (IA2), a self-distillation technique which aims to replicate ICL's activation patterns in SFT models and incentivizes ICL-like internal reasoning. Performing IA2 as a priming step before SFT significantly improves the accuracy and calibration of model outputs, as shown by our extensive empirical results on 12 popular benchmarks and two model families. This finding is not only practically useful, but also offers a conceptual window into the inner mechanics of model adaptation.
Submission history
From: Aayush Mishra [view email][v1] Fri, 26 Sep 2025 17:46:32 UTC (2,222 KB)
[v2] Mon, 15 Dec 2025 18:01:10 UTC (2,224 KB)
[v3] Wed, 18 Mar 2026 16:05:51 UTC (2,216 KB)
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
