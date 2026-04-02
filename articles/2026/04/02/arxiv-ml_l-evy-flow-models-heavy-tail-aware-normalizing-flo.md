---
title: "L\'evy-Flow Models: Heavy-Tail-Aware Normalizing Flows for Financial Risk Management"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00195"
published: "2026-04-02"
fetched: "2026-04-03T07:17:57.088069"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Lévy-Flow Models: Heavy-Tail-Aware Normalizing Flows for Financial Risk Management
View PDF HTML (experimental)Abstract:We introduce Lévy-Flows, a class of normalizing flow models that replace the standard Gaussian base distribution with Lévy process-based distributions, specifically Variance Gamma (VG) and Normal-Inverse Gaussian (NIG). These distributions naturally capture heavy-tailed behavior while preserving exact likelihood evaluation and efficient reparameterized sampling. We establish theoretical guarantees on tail behavior, showing that for regularly varying bases the tail index is preserved under asymptotically linear flow transformations, and that identity-tail Neural Spline Flow architectures preserve the base distribution's tail shape exactly outside the transformation region. Empirically, we evaluate on S&P 500 daily returns and additional assets, demonstrating substantial improvements in density estimation and risk calibration. VG-based flows reduce test negative log-likelihood by 69% relative to Gaussian flows and achieve exact 95% VaR calibration, while NIG-based flows provide the most accurate Expected Shortfall estimates. These results show that incorporating Lévy process structure into normalizing flows yields significant gains in modeling heavy-tailed data, with applications to financial risk management.
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
