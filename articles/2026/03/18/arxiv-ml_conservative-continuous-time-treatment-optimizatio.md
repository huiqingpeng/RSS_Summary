---
title: "Conservative Continuous-Time Treatment Optimization"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.16789"
published: "2026-03-18"
fetched: "2026-03-18T15:48:15.220153"
---

Computer Science > Machine Learning
[Submitted on 17 Mar 2026]
Title:Conservative Continuous-Time Treatment Optimization
View PDF HTML (experimental)Abstract:We develop a conservative continuous-time stochastic control framework for treatment optimization from irregularly sampled patient trajectories. The unknown patient dynamics are modeled as a controlled stochastic differential equation with treatment as a continuous-time control. Naive model-based optimization can exploit model errors and propose out-of-support controls, so optimizing the estimated dynamics may not optimize the true dynamics. To limit extrapolation, we add a consistent signature-based MMD regularizer on path space that penalizes treatment plans whose induced trajectory distribution deviates from observed trajectories. The resulting objective minimizes a computable upper bound on the true cost. Experiments on benchmark datasets show improved robustness and performance compared to non-conservative baselines.
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
