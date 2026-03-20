---
title: "Kernel Single-Index Bandits: Estimation, Inference, and Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18938"
published: "2026-03-20"
fetched: "2026-03-20T13:17:45.227535"
---

Statistics > Machine Learning
[Submitted on 19 Mar 2026]
Title:Kernel Single-Index Bandits: Estimation, Inference, and Learning
View PDFAbstract:We study contextual bandits with finitely many actions in which the reward of each arm follows a single-index model with an arm-specific index parameter and an unknown nonparametric link function. We consider a regime in which arms correspond to stable decision options and covariates evolve adaptively under the bandit policy. This setting creates significant statistical challenges: the sampling distribution depends on the allocation rule, observations are dependent over time, and inverse-propensity weighting induces variance inflation. We propose a kernelized $\varepsilon$-greedy algorithm that combines Stein-based estimation of the index parameters with inverse-propensity-weighted kernel ridge regression for the reward functions. This approach enables flexible semiparametric learning while retaining interpretability. Our analysis develops new tools for inference with adaptively collected data. We establish asymptotic normality for the single-index estimator under adaptive sampling, yielding valid confidence regions, and derive a directional functional central limit theorem for the RKHS estimator, which provides asymptotically valid pointwise confidence intervals. The analysis relies on concentration bounds for inverse-weighted Gram matrices together with martingale central limit theorems. We further obtain finite-time regret guarantees, including $\tilde{O}(\sqrt{T})$ rates under common-link Lipschitz conditions, showing that semiparametric structure can be exploited without sacrificing statistical efficiency. These results provide a unified framework for simultaneous learning and inference in single-index contextual bandits.
Current browse context:
stat.ML
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
