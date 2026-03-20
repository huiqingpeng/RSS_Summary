---
title: "An Improved Model-Free Decision-Estimation Coefficient with Applications in Adversarial MDPs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2510.08882"
published: "2026-03-20"
fetched: "2026-03-20T14:08:23.466021"
---

Computer Science > Machine Learning
[Submitted on 10 Oct 2025 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:An Improved Model-Free Decision-Estimation Coefficient with Applications in Adversarial MDPs
View PDFAbstract:We study decision making with structured observation (DMSO). Previous work (Foster et al., 2021b, 2023a) has characterized the complexity of DMSO via the decision-estimation coefficient (DEC), but left a gap between the regret upper and lower bounds that scales with the size of the model class. To tighten this gap, Foster et al. (2023b) introduced optimistic DEC, achieving a bound that scales only with the size of the value-function class. However, their optimism-based exploration is only known to handle the stochastic setting, and it remains unclear whether it extends to the adversarial setting.
We introduce Dig-DEC, a model-free DEC that removes optimism and drives exploration purely by information gain. Dig-DEC is always no larger than optimistic DEC and can be much smaller in special cases. Importantly, the removal of optimism allows it to handle adversarial environments without explicit reward estimators. By applying Dig-DEC to hybrid MDPs with stochastic transitions and adversarial rewards, we obtain the first model-free regret bounds for hybrid MDPs with bandit feedback under several general transition structures, resolving the main open problem left by Liu et al. (2025).
We also improve the online function-estimation procedure in model-free learning: For average estimation error minimization, we refine the estimator in Foster et al. (2023b) to achieve sharper concentration, improving their regret bounds from $T^{3/4}$ to $T^{2/3}$ (on-policy) and from $T^{5/6}$ to $T^{7/9}$ (off-policy). For squared error minimization in Bellman-complete MDPs, we redesign their two-timescale procedure, improving the regret bound from $T^{2/3}$ to $\sqrt{T}$. This is the first time a DEC-based method achieves performance matching that of optimism-based approaches (Jin et al., 2021; Xie et al., 2023) in Bellman-complete MDPs.
Submission history
From: Haolin Liu [view email][v1] Fri, 10 Oct 2025 00:25:12 UTC (120 KB)
[v2] Wed, 18 Mar 2026 22:25:36 UTC (127 KB)
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
