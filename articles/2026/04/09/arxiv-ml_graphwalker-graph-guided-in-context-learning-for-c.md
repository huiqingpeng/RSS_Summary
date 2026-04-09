---
title: "GraphWalker: Graph-Guided In-Context Learning for Clinical Reasoning on Electronic Health Records"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06684"
published: "2026-04-09"
fetched: "2026-04-10T07:05:05.018727"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:GraphWalker: Graph-Guided In-Context Learning for Clinical Reasoning on Electronic Health Records
View PDF HTML (experimental)Abstract:Clinical Reasoning on Electronic Health Records (EHRs) is a fundamental yet challenging task in modern healthcare. While in-context learning (ICL) offers a promising inference-time adaptation paradigm for large language models (LLMs) in EHR reasoning, existing methods face three fundamental challenges: (1) Perspective Limitation, where data-driven similarity fails to align with LLM reasoning needs and model-driven signals are constrained by limited clinical competence; (2) Cohort Awareness, as demonstrations are selected independently without modeling population-level structure; and (3) Information Aggregation, where redundancy and interaction effects among demonstrations are ignored, leading to diminishing marginal gains. To address these challenges, we propose GraphWalker, a principled demonstration selection framework for EHR-oriented ICL. GraphWalker (i) jointly models patient clinical information and LLM-estimated information gain by integrating data-driven and model-driven perspectives, (ii) incorporates Cohort Discovery to avoid noisy local optima, and (iii) employs a Lazy Greedy Search with Frontier Expansion algorithm to mitigate diminishing marginal returns in information aggregation. Extensive experiments on multiple real-world EHR benchmarks demonstrate that GraphWalker consistently outperforms state-of-the-art ICL baselines, yielding substantial improvements in clinical reasoning performance. Our code is open-sourced at this https URL
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
IArxiv Recommender
(What is IArxiv?)
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
