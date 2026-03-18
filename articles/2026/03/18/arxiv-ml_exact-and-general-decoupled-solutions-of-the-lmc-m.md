---
title: "Exact and general decoupled solutions of the LMC Multitask Gaussian Process model"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2310.12032"
published: "2026-03-18"
fetched: "2026-03-18T16:15:39.155849"
---

Computer Science > Machine Learning
[Submitted on 18 Oct 2023 (v1), last revised 17 Mar 2026 (this version, v3)]
Title:Exact and general decoupled solutions of the LMC Multitask Gaussian Process model
View PDF HTML (experimental)Abstract:The Linear Model of Co-regionalization (LMC) is a very general multitask gaussian process model for regression or classification. While its expressiveness and conceptual simplicity are appealing, naive implementations have cubic complexity in the product (number of datapoints $\times$ number of tasks), making approximations mandatory for most applications. However, recent work has shown that in some settings the latent processes of the model can be decoupled, leading to a complexity that is only linear in the number of said processes. We here extend these results, showing from the most general assumptions that the only condition necessary to an efficient exact computation of the LMC is a mild hypothesis on the noise model. We introduce a full parametrization of the resulting \emph{projected LMC} model, enabling its efficient optimization. The effectiveness of this approach is assessed through synthetic and real-data experiments, testing in particular the behavior of its underlying noise model restriction.\\ Overall, the projected LMC appears as a competitive and simpler alternative to state-of-the art multitask gaussian process models. It greatly facilitates some computations such as training data updates or leave-one-out cross-validation, and is more interpretable, for it gives access to its low-dimensional quantities and to their explicit relation with the full-dimensional data. These qualities could facilitate the adoption by various industries of entire classes of methodologies, notably multitask bayesian optimization.
Submission history
From: Olivier Truffinet [view email][v1] Wed, 18 Oct 2023 15:16:24 UTC (834 KB)
[v2] Thu, 21 Mar 2024 14:36:26 UTC (816 KB)
[v3] Tue, 17 Mar 2026 14:19:06 UTC (1,285 KB)
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
