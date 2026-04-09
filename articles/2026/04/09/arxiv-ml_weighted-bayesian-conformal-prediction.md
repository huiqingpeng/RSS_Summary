---
title: "Weighted Bayesian Conformal Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.06464"
published: "2026-04-09"
fetched: "2026-04-10T07:04:59.841341"
---

Computer Science > Machine Learning
[Submitted on 7 Apr 2026]
Title:Weighted Bayesian Conformal Prediction
View PDFAbstract:Conformal prediction provides distribution-free prediction intervals with finite-sample coverage guarantees, and recent work by Snell \& Griffiths reframes it as Bayesian Quadrature (BQ-CP), yielding powerful data-conditional guarantees via Dirichlet posteriors over thresholds. However, BQ-CP fundamentally requires the i.i.d. assumption -- a limitation the authors themselves identify. Meanwhile, weighted conformal prediction handles distribution shift via importance weights but remains frequentist, producing only point-estimate thresholds. We propose \textbf{Weighted Bayesian Conformal Prediction (WBCP)}, which generalizes BQ-CP to arbitrary importance-weighted settings by replacing the uniform Dirichlet $\Dir(1,\ldots,1)$ with a weighted Dirichlet $\Dir(\neff \cdot \tilde{w}_1, \ldots, \neff \cdot \tilde{w}_n)$, where $\neff$ is Kish's effective sample size. We prove four theoretical results: (1)~$\neff$ is the unique concentration parameter matching frequentist and Bayesian variances; (2)~posterior standard deviation decays as $O(1/\sqrt{\neff})$; (3)~BQ-CP's stochastic dominance guarantee extends to per-weight-profile data-conditional guarantees; (4)~the HPD threshold provides $O(1/\sqrt{\neff})$ improvement in conditional coverage. We instantiate WBCP for spatial prediction as \emph{Geographical BQ-CP}, where kernel-based spatial weights yield per-location posteriors with interpretable diagnostics. Experiments on synthetic and real-world spatial datasets demonstrate that WBCP maintains coverage guarantees while providing substantially richer uncertainty information.
Current browse context:
cs.LG
Change to browse by:
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
