---
title: "Multi-Preconditioned LBFGS for Training Finite-Basis PINNs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2601.08709"
published: "2026-03-20"
fetched: "2026-03-20T15:02:59.544977"
---

Mathematics > Numerical Analysis
[Submitted on 13 Jan 2026 (v1), last revised 19 Mar 2026 (this version, v2)]
Title:Multi-Preconditioned LBFGS for Training Finite-Basis PINNs
View PDF HTML (experimental)Abstract:A multi-preconditioned LBFGS (MP-LBFGS) algorithm is introduced for training finite-basis physics-informed neural networks (FBPINNs). The algorithm is motivated by the nonlinear additive Schwarz method and exploits the domain-decomposition-inspired additive architecture of FBPINNs, in which local neural networks are defined on subdomains, thereby localizing the network representation. Parallel, subdomain-local quasi-Newton corrections are then constructed on the corresponding local parts of the architecture. A key feature is a novel nonlinear multi-preconditioning mechanism, in which subdomain corrections are optimally combined through the solution of a low-dimensional subspace minimization problem. Numerical experiments indicate that MP-LBFGS can improve convergence speed, as well as model accuracy over standard LBFGS while incurring lower communication overhead.
Submission history
From: Aymane Kssim [view email][v1] Tue, 13 Jan 2026 16:38:15 UTC (2,642 KB)
[v2] Thu, 19 Mar 2026 16:25:50 UTC (2,650 KB)
Current browse context:
math.NA
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
