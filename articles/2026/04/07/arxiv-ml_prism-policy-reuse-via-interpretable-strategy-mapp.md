---
title: "Prism: Policy Reuse via Interpretable Strategy Mapping in Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2604.02353"
published: "2026-04-07"
fetched: "2026-04-08T07:02:37.180099"
---

Computer Science > Machine Learning
[Submitted on 4 Mar 2026]
Title:Prism: Policy Reuse via Interpretable Strategy Mapping in Reinforcement Learning
View PDF HTML (experimental)Abstract:We present PRISM (Policy Reuse via Interpretable Strategy Mapping), a framework that grounds reinforcement learning agents' decisions in discrete, causally validated concepts and uses those concepts as a zero-shot transfer interface between agents trained with different algorithms. PRISM clusters each agent's encoder features into $K$ concepts via K-means. Causal intervention establishes that these concepts directly drive - not merely correlate with - agent behavior: overriding concept assignments changes the selected action in 69.4% of interventions ($p = 8.6 \times 10^{-86}$, 2500 interventions). Concept importance and usage frequency are dissociated: the most-used concept (C47, 33.0% frequency) causes only a 9.4% win-rate drop when ablated, while ablating C16 (15.4% frequency) collapses win rate from 100% to 51.8%. Because concepts causally encode strategy, aligning them via optimal bipartite matching transfers strategic knowledge zero-shot. On Go~7$\times$7 with three independently trained agents, concept transfer achieves 69.5%$\pm$3.2% and 76.4%$\pm$3.4% win rate against a standard engine across the two successful transfer pairs (10 seeds), compared to 3.5% for a random agent and 9.2% without alignment. Transfer succeeds when the source policy is strong; geometric alignment quality predicts nothing ($R^2 \approx 0$). The framework is scoped to domains where strategic state is naturally discrete: the identical pipeline on Atari Breakout yields bottleneck policies at random-agent performance, confirming that the Go results reflect a structural property of the domain.
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
