---
title: "Reinforcement Learning from Multi-Source Imperfect Preferences: Best-of-Both-Regimes Regret"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20453"
published: "2026-03-24"
fetched: "2026-03-25T07:10:03.559926"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Reinforcement Learning from Multi-Source Imperfect Preferences: Best-of-Both-Regimes Regret
View PDF HTML (experimental)Abstract:Reinforcement learning from human feedback (RLHF) replaces hard-to-specify rewards with pairwise trajectory preferences, yet regret-oriented theory often assumes that preference labels are generated consistently from a single ground-truth objective. In practical RLHF systems, however, feedback is typically \emph{multi-source} (annotators, experts, reward models, heuristics) and can exhibit systematic, persistent mismatches due to subjectivity, expertise variation, and annotation/modeling artifacts. We study episodic RL from \emph{multi-source imperfect preferences} through a cumulative imperfection budget: for each source, the total deviation of its preference probabilities from an ideal oracle is at most $\omega$ over $K$ episodes. We propose a unified algorithm with regret $\tilde{O}(\sqrt{K/M}+\omega)$, which exhibits a best-of-both-regimes behavior: it achieves $M$-dependent statistical gains when imperfection is small (where $M$ is the number of sources), while remaining robust with unavoidable additive dependence on $\omega$ when imperfection is large. We complement this with a lower bound $\tilde{\Omega}(\max\{\sqrt{K/M},\omega\})$, which captures the best possible improvement with respect to $M$ and the unavoidable dependence on $\omega$, and a counterexample showing that naïvely treating imperfect feedback as as oracle-consistent can incur regret as large as $\tilde{\Omega}(\min\{\omega\sqrt{K},K\})$. Technically, our approach involves imperfection-adaptive weighted comparison learning, value-targeted transition estimation to control hidden feedback-induced distribution shift, and sub-importance sampling to keep the weighted objectives analyzable, yielding regret guarantees that quantify when multi-source feedback provably improves RLHF and how cumulative imperfection fundamentally limits it.
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
