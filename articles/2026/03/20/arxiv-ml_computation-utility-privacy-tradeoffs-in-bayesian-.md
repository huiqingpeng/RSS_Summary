---
title: "Computation-Utility-Privacy Tradeoffs in Bayesian Estimation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18254"
published: "2026-03-20"
fetched: "2026-03-20T13:10:58.311715"
---

Computer Science > Data Structures and Algorithms
[Submitted on 18 Mar 2026]
Title:Computation-Utility-Privacy Tradeoffs in Bayesian Estimation
View PDF HTML (experimental)Abstract:Bayesian methods lie at the heart of modern data science and provide a powerful scaffolding for estimation in data-constrained settings and principled quantification and propagation of uncertainty. Yet in many real-world use cases where these methods are deployed, there is a natural need to preserve the privacy of the individuals whose data is being scrutinized. While a number of works have attempted to approach the problem of differentially private Bayesian estimation through either reasoning about the inherent privacy of the posterior distribution or privatizing off-the-shelf Bayesian methods, these works generally do not come with rigorous utility guarantees beyond low-dimensional settings. In fact, even for the prototypical tasks of Gaussian mean estimation and linear regression, it was unknown how close one could get to the Bayes-optimal error with a private algorithm, even in the simplest case where the unknown parameter comes from a Gaussian prior. In this work, we give the first efficient algorithms for both of these problems that achieve mean-squared error $(1+o(1))\mathrm{OPT}$ and additionally show that both tasks exhibit an intriguing computational-statistical gap. For Bayesian mean estimation, we prove that the excess risk achieved by our method is optimal among all efficient algorithms within the low-degree framework, yet is provably worse than what is achievable by an exponential-time algorithm. For linear regression, we prove a qualitatively similar lower bound. Our algorithms draw upon the privacy-to-robustness framework of arXiv:2212.05015, but with the curious twist that to achieve private Bayes-optimal estimation, we need to design sum-of-squares-based robust estimators for inherently non-robust objects like the empirical mean and OLS estimator. Along the way we also add to the sum-of-squares toolkit a new kind of constraint based on short-flat decompositions.
Current browse context:
cs.DS
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
