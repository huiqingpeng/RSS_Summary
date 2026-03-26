---
title: "Optimal Variance-Dependent Regret Bounds for Infinite-Horizon MDPs"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23926"
published: "2026-03-26"
fetched: "2026-03-27T07:18:35.920551"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Optimal Variance-Dependent Regret Bounds for Infinite-Horizon MDPs
View PDF HTML (experimental)Abstract:Online reinforcement learning in infinite-horizon Markov decision processes (MDPs) remains less theoretically and algorithmically developed than its episodic counterpart, with many algorithms suffering from high ``burn-in'' costs and failing to adapt to benign instance-specific complexity. In this work, we address these shortcomings for two infinite-horizon objectives: the classical average-reward regret and the $\gamma$-regret. We develop a single tractable UCB-style algorithm applicable to both settings, which achieves the first optimal variance-dependent regret guarantees. Our regret bounds in both settings take the form $\tilde{O}( \sqrt{SA\,\text{Var}} + \text{lower-order terms})$, where $S,A$ are the state and action space sizes, and $\text{Var}$ captures cumulative transition variance. This implies minimax-optimal average-reward and $\gamma$-regret bounds in the worst case but also adapts to easier problem instances, for example yielding nearly constant regret in deterministic MDPs. Furthermore, our algorithm enjoys significantly improved lower-order terms for the average-reward setting. With prior knowledge of the optimal bias span $\Vert h^\star\Vert_\text{sp}$, our algorithm obtains lower-order terms scaling as $\Vert h^\star\Vert_\text{sp} S^2 A$, which we prove is optimal in both $\Vert h^\star\Vert_\text{sp}$ and $A$.
Without prior knowledge, we prove that no algorithm can have lower-order terms smaller than $\Vert h^\star \Vert_\text{sp}^2 S A$, and we provide a prior-free algorithm whose lower-order terms scale as $\Vert h^\star\Vert_\text{sp}^2 S^3 A$, nearly matching this lower bound. Taken together, these results completely characterize the optimal dependence on $\Vert h^\star\Vert_\text{sp}$ in both leading and lower-order terms, and reveal a fundamental gap in what is achievable with and without prior knowledge.
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
