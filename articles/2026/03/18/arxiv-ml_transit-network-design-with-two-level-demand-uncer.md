---
title: "Transit Network Design with Two-Level Demand Uncertainties: A Machine Learning and Contextual Stochastic Optimization Framework"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.00010"
published: "2026-03-18"
fetched: "2026-03-18T17:04:46.527128"
---

Computer Science > Machine Learning
[Submitted on 27 Jan 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Transit Network Design with Two-Level Demand Uncertainties: A Machine Learning and Contextual Stochastic Optimization Framework
View PDF HTML (experimental)Abstract:Transit Network Design is a well-studied problem in the field of transportation, typically addressed by solving optimization models under fixed demand assumptions. Considering the limitations of these assumptions, this paper proposes a new framework, namely the Two-Level Rider Choice Transit Network Design (2LRC-TND), that leverages machine learning and contextual stochastic optimization (CSO) through constraint programming (CP) to incorporate two layers of demand uncertainties into the network design process. The first level identifies travelers who rely on public transit (core demand), while the second level captures the conditional adoption behavior of those who do not (latent demand), based on the availability and quality of transit services. To capture these two types of uncertainties, 2LRC-TND relies on two travel mode choice models, that use multiple machine learning models. To design a network, 2LRC-TND integrates the resulting choice models into a CSO that is solved using a CP-SAT solver. 2LRC-TND is evaluated through a case study involving over 6,600 travel arcs and more than 38,000 trips in the Atlanta metropolitan area. The computational results demonstrate the effectiveness of the 2LRC-TND in designing transit networks that account for demand uncertainties and contextual information, offering a more realistic alternative to fixed-demand models.
Submission history
From: Hongzhao Guan [view email][v1] Tue, 27 Jan 2026 01:12:19 UTC (1,665 KB)
[v2] Tue, 17 Mar 2026 17:54:46 UTC (1,665 KB)
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
