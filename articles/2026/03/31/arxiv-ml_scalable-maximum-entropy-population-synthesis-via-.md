---
title: "Scalable Maximum Entropy Population Synthesis via Persistent Contrastive Divergence"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.27312"
published: "2026-03-31"
fetched: "2026-04-01T07:22:53.524794"
---

Computer Science > Machine Learning
[Submitted on 28 Mar 2026]
Title:Scalable Maximum Entropy Population Synthesis via Persistent Contrastive Divergence
View PDF HTML (experimental)Abstract:Maximum entropy (MaxEnt) modelling provides a principled framework for generating synthetic populations from aggregate census data, without access to individual-level microdata. The bottleneck of existing approaches is exact expectation computation, which requires summing over the full tuple space $\cX$ and becomes infeasible for more than $K \approx 20$ categorical attributes. We propose \emph{GibbsPCDSolver}, a stochastic replacement for this computation based on Persistent Contrastive Divergence (PCD): a persistent pool of $N$ synthetic individuals is updated by Gibbs sweeps at each gradient step, providing a stochastic approximation of the model expectations without ever materialising $\cX$. We validate the approach on controlled benchmarks and on \emph{Syn-ISTAT}, a $K{=}15$ Italian demographic benchmark with analytically exact marginal targets derived from ISTAT-inspired conditional probability tables. Scaling experiments across $K \in \{12, 20, 30, 40, 50\}$ confirm that GibbsPCDSolver maintains $\MRE \in [0.010, 0.018]$ while $|\cX|$ grows eighteen orders of magnitude, with runtime scaling as $O(K)$ rather than $O(|\cX|)$. On Syn-ISTAT, GibbsPCDSolver reaches $\MRE{=}0.03$ on training constraints and -- crucially -- produces populations with effective sample size $\Neff = N$ versus $\Neff \approx 0.012\,N$ for generalised raking, an $86.8{\times}$ diversity advantage that is essential for agent-based urban simulations.
Submission history
From: Mirko Degli Esposti [view email][v1] Sat, 28 Mar 2026 15:36:20 UTC (829 KB)
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
