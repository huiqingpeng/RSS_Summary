---
title: "Cost-Penalized Fitness in FMA-Orchestrated Mixture of Experts: Experimental Evidence for Molecular Memory in Domain Adaptation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00812"
published: "2026-04-02"
fetched: "2026-04-03T07:25:13.136085"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Cost-Penalized Fitness in FMA-Orchestrated Mixture of Experts: Experimental Evidence for Molecular Memory in Domain Adaptation
View PDFAbstract:We present experimental results from seven controlled runs of nanoFMT, a Free-Market Algorithm (FMA) orchestrated transformer with dynamic Mixture-of-Experts (MoE) management. The experiments address a fundamental question for advanced LLM development: how should an MoE system manage its expert pool when operating at full capacity under changing data distributions? We demonstrate that cost-penalized fitness metrics, combined with a linear grace period for newborn experts, produce a system that accumulates domain expertise through diversification rather than replacement. The central result is a round-trip domain shift experiment showing 9-11x faster recovery when returning to a previously learned domain, with zero expert births or replacements required. This "molecular memory" effect -- where dormant experts survive and reactivate when their domain returns -- has no analogue in current MoE management approaches. A preliminary cost analysis estimates annual savings of $39.1M and 27.1 GWh energy reduction for an OpenAI-scale provider under a moderate scenario.
Submission history
From: Martin Jaraiz Prof. [view email][v1] Wed, 1 Apr 2026 12:19:57 UTC (779 KB)
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
