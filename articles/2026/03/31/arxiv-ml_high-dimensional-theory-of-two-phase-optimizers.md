---
title: "High dimensional theory of two-phase optimizers"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.26954"
published: "2026-03-31"
fetched: "2026-04-01T07:20:39.700704"
---

Computer Science > Machine Learning
[Submitted on 27 Mar 2026]
Title:High dimensional theory of two-phase optimizers
View PDF HTML (experimental)Abstract:The trend towards larger training setups has brought a renewed interest in partially asynchronous two-phase optimizers which optimize locally and then synchronize across workers. Additionally, recent work suggests that the one-worker version of one of these algorithms, DiLoCo, shows promising results as a (synchronous) optimizer. Motivated by these studies we present an analysis of LA-DiLoCo, a simple member of the DiLoCo family, on a high-dimensional linear regression problem. We show that the one-worker variant, LA, provides a different tradeoff between signal and noise than SGD, which is beneficial in many scenarios. We also show that the multi-worker version generates more noise than the single worker version, but that this additional noise generation can be ameliorated by appropriate choice of hyperparameters. We conclude with an analysis of SLA -- LA with momentum -- and show that stacking two momentum operators gives an opportunity for acceleration via a non-linear transformation of the "effective'' Hessian spectrum, which is maximized for Nesterov momentum. Altogether our results show that two-phase optimizers represent a fruitful new paradigm for understanding and improving training algorithms.
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
