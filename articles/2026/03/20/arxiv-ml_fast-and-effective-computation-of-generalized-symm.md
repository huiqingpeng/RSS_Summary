---
title: "Fast and Effective Computation of Generalized Symmetric Matrix Factorization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19147"
published: "2026-03-20"
fetched: "2026-03-20T13:20:31.511506"
---

Mathematics > Optimization and Control
[Submitted on 19 Mar 2026]
Title:Fast and Effective Computation of Generalized Symmetric Matrix Factorization
View PDF HTML (experimental)Abstract:In this paper, we study a nonconvex, nonsmooth, and non-Lipschitz generalized symmetric matrix factorization model that unifies a broad class of matrix factorization formulations arising in machine learning, image science, engineering, and related areas. We first establish two exactness properties. On the modeling side, we prove an exact penalty property showing that, under suitable conditions, the symmetry-inducing quadratic penalty enforces symmetry whenever the penalty parameter is sufficiently large but finite, thereby exactly recovering the associated symmetric formulation. On the algorithmic side, we introduce an auxiliary-variable splitting formulation and establish an exact relaxation relationship that rigorously links stationary points of the original objective function to those of a relaxed potential function. Building on these exactness properties, we propose an average-type nonmonotone alternating updating method (A-NAUM) based on the relaxed potential function. At each iteration, A-NAUM alternately updates the two factor blocks by (approximately) minimizing the potential function, while the auxiliary block is updated in closed form. To ensure the convergence and enhance practical performance, we further incorporate an average-type nonmonotone line search and show that it is well-defined under mild conditions. Moreover, based on the Kurdyka-Łojasiewicz property and its associated exponent, we establish global convergence of the entire sequence to a stationary point and derive convergence rate results. Finally, numerical experiments on real datasets demonstrate the efficiency of A-NAUM.
Current browse context:
math.OC
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
