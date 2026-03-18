---
title: "High-dimensional estimation with missing data: Statistical and computational limits"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16712"
published: "2026-03-18"
fetched: "2026-03-18T16:13:59.851696"
---

Mathematics > Statistics Theory
[Submitted on 17 Mar 2026]
Title:High-dimensional estimation with missing data: Statistical and computational limits
View PDFAbstract:We consider computationally-efficient estimation of population parameters when observations are subject to missing data. In particular, we consider estimation under the realizable contamination model of missing data in which an $\epsilon$ fraction of the observations are subject to an arbitrary (and unknown) missing not at random (MNAR) mechanism. When the true data is Gaussian, we provide evidence towards statistical-computational gaps in several problems. For mean estimation in $\ell_2$ norm, we show that in order to obtain error at most $\rho$, for any constant contamination $\epsilon \in (0, 1)$, (roughly) $n \gtrsim d e^{1/\rho^2}$ samples are necessary and that there is a computationally-inefficient algorithm which achieves this error. On the other hand, we show that any computationally-efficient method within certain popular families of algorithms requires a much larger sample complexity of (roughly) $n \gtrsim d^{1/\rho^2}$ and that there exists a polynomial time algorithm based on sum-of-squares which (nearly) achieves this lower bound. For covariance estimation in relative operator norm, we show that a parallel development holds. Finally, we turn to linear regression with missing observations and show that such a gap does not persist. Indeed, in this setting we show that minimizing a simple, strongly convex empirical risk nearly achieves the information-theoretic lower bound in polynomial time.
Current browse context:
math.ST
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
