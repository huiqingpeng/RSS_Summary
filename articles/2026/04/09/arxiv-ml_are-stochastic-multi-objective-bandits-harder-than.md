---
title: "Are Stochastic Multi-objective Bandits Harder than Single-objective Bandits?"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.07096"
published: "2026-04-09"
fetched: "2026-04-10T07:05:13.219681"
---

Computer Science > Machine Learning
[Submitted on 8 Apr 2026]
Title:Are Stochastic Multi-objective Bandits Harder than Single-objective Bandits?
View PDF HTML (experimental)Abstract:Multi-objective bandits have attracted increasing attention because of their broad applicability and mathematical elegance, where the reward of each arm is a multi-dimensional vector rather than a scalar. This naturally introduces Pareto order relations and Pareto regret. A long-standing question in this area is whether performance is fundamentally harder to optimize because of this added complexity. A recent surprising result shows that, in the adversarial setting, Pareto regret is no larger than classical regret; however, in the stochastic setting, where the regret notion is different, the picture remains unclear. In fact, existing work suggests that Pareto regret in the stochastic case increases with the dimensionality. This controversial yet subtle phenomenon motivates our central question: \emph{are multi-objective bandits actually harder than single-objective ones?} We answer this question in full by showing that, in the stochastic setting, Pareto regret is in fact governed by the maximum sub-optimality gap \(g^\dagger\), and hence by the minimum marginal regret of order \(\Omega(\frac{K\log T}{g^\dagger})\). We further develop a new algorithm that achieves Pareto regret of order \(O(\frac{K\log T}{g^\dagger})\), and is therefore optimal. The algorithm leverages a nested two-layer uncertainty quantification over both arms and objectives through upper and lower confidence bound estimators. It combines a top-two racing strategy for arm selection with an uncertainty-greedy rule for dimension selection. Together, these components balance exploration and exploitation across the two layers. We also conduct comprehensive numerical experiments to validate the proposed algorithm, showing the desired regret guarantee and significant gains over benchmark methods.
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
