---
title: "Adversarial Latent-State Training for Robust Policies in Partially Observable Domains"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.07313"
published: "2026-03-20"
fetched: "2026-03-20T14:12:18.683965"
---

Computer Science > Machine Learning
[Submitted on 7 Mar 2026 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Adversarial Latent-State Training for Robust Policies in Partially Observable Domains
View PDF HTML (experimental)Abstract:Robustness under latent distribution shift remains challenging in partially observable reinforcement learning. We formalize a focused setting where an adversary selects a hidden initial latent distribution before the episode, termed an adversarial latent-initial-state POMDP. Theoretically, we prove a latent minimax principle, characterize worst-case defender distributions, and derive approximate best-response inequalities with finite-sample concentration bounds that make the optimization and sampling terms explicit. Empirically, using a Battleship benchmark, we demonstrate that targeted exposure to shifted latent distributions reduces average robustness gaps between Spread and Uniform distributions from 10.3 to 3.1 shots at equal budget. Furthermore, iterative best-response training exhibits budget-sensitive behavior that is qualitatively consistent with the theorem-guided diagnostics once one accounts for discounted PPO surrogates and finite-sample noise. Ultimately, we show that for latent-initial-state problems, the framework yields a clean evaluation game and useful theorem-motivated diagnostics while also making clear where implementation-level surrogates and optimization limits enter.
Submission history
From: Angad Ahuja Mr. [view email][v1] Sat, 7 Mar 2026 19:06:49 UTC (56 KB)
[v2] Tue, 10 Mar 2026 17:36:57 UTC (60 KB)
[v3] Wed, 18 Mar 2026 18:48:25 UTC (125 KB)
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
