---
title: "Genomic Next-Token Predictors are In-Context Learners"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2511.12797"
published: "2026-03-19"
fetched: "2026-03-19T14:09:39.979311"
---

Computer Science > Machine Learning
[Submitted on 16 Nov 2025 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Genomic Next-Token Predictors are In-Context Learners
View PDF HTML (experimental)Abstract:In-context learning (ICL) -- the capacity of a model to infer and apply abstract patterns from examples provided within its input -- has been extensively studied in large language models trained for next-token prediction on human text. In fact, prior work often attributes this emergent behavior to distinctive statistical properties in human language. This raises a fundamental question: can ICL arise organically in other sequence domains purely through large-scale predictive training?
To explore this, we turn to genomic sequences, an alternative symbolic domain rich in statistical structure. Specifically, we study the Evo2 genomic model, trained predominantly on next-nucleotide (A/T/C/G) prediction, at a scale comparable to mid-sized LLMs. We develop a controlled experimental framework comprising symbolic reasoning tasks instantiated in both linguistic and genomic forms, enabling direct comparison of ICL across genomic and linguistic models. Our results show that genomic models, like their linguistic counterparts, exhibit log-linear gains in pattern induction as the number of in-context demonstrations increases. To the best of our knowledge, this is the first evidence of organically emergent ICL in genomic sequences, supporting the hypothesis that ICL arises as a consequence of large-scale predictive modeling over rich data. These findings extend emergent meta-learning beyond language, pointing toward a unified, modality-agnostic view of in-context learning.
Submission history
From: Nathan Breslow [view email][v1] Sun, 16 Nov 2025 21:56:39 UTC (3,099 KB)
[v2] Fri, 21 Nov 2025 02:11:05 UTC (3,099 KB)
[v3] Tue, 17 Mar 2026 23:52:42 UTC (1,950 KB)
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
