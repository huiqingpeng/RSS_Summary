---
title: "High-Dimensional Gaussian Mean Estimation under Realizable Contamination"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16798"
published: "2026-03-18"
fetched: "2026-03-18T16:03:30.962964"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:High-Dimensional Gaussian Mean Estimation under Realizable Contamination
View PDF HTML (experimental)Abstract:We study mean estimation for a Gaussian distribution with identity covariance in $\mathbb{R}^d$ under a missing data scheme termed realizable $\epsilon$-contamination model. In this model an adversary can choose a function $r(x)$ between 0 and $\epsilon$ and each sample $x$ goes missing with probability $r(x)$. Recent work Ma et al., 2024 proposed this model as an intermediate-strength setting between Missing Completely At Random (MCAR) -- where missingness is independent of the data -- and Missing Not At Random (MNAR) -- where missingness may depend arbitrarily on the sample values and can lead to non-identifiability issues. That work established information-theoretic upper and lower bounds for mean estimation in the realizable contamination model. Their proposed estimators incur runtime exponential in the dimension, leaving open the possibility of computationally efficient algorithms in high dimensions. In this work, we establish an information-computation gap in the Statistical Query model (and, as a corollary, for Low-Degree Polynomials and PTF tests), showing that algorithms must either use substantially more samples than information-theoretically necessary or incur exponential runtime. We complement our SQ lower bound with an algorithm whose sample-time tradeoff nearly matches our lower bound. Together, these results qualitatively characterize the complexity of Gaussian mean estimation under $\epsilon$-realizable contamination.
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
