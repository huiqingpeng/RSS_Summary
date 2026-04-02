---
title: "Differentially Private Manifold Denoising"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.00942"
published: "2026-04-02"
fetched: "2026-04-03T07:26:21.891824"
---

Computer Science > Machine Learning
[Submitted on 1 Apr 2026]
Title:Differentially Private Manifold Denoising
View PDF HTML (experimental)Abstract:We introduce a differentially private manifold denoising framework that allows users to exploit sensitive reference datasets to correct noisy, non-private query points without compromising privacy. The method follows an iterative procedure that (i) privately estimates local means and tangent geometry using the reference data under calibrated sensitivity, (ii) projects query points along the privately estimated subspace toward the local mean via corrective steps at each iteration, and (iii) performs rigorous privacy accounting across iterations and queries using $(\varepsilon,\delta)$-differential privacy (DP). Conceptually, this framework brings differential privacy to manifold methods, retaining sufficient geometric signal for downstream tasks such as embedding, clustering, and visualization, while providing formal DP guarantees for the reference data. Practically, the procedure is modular and scalable, separating DP-protected local geometry (means and tangents) from budgeted query-point updates, with a simple scheduler allocating privacy budget across iterations and queries. Under standard assumptions on manifold regularity, sampling density, and measurement noise, we establish high-probability utility guarantees showing that corrected queries converge toward the manifold at a non-asymptotic rate governed by sample size, noise level, bandwidth, and the privacy budget. Simulations and case studies demonstrate accurate signal recovery under moderate privacy budgets, illustrating clear utility-privacy trade-offs and providing a deployable DP component for manifold-based workflows in regulated environments without reengineering privacy systems.
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
