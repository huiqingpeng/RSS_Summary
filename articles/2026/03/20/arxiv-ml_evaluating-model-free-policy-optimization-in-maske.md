---
title: "Evaluating Model-Free Policy Optimization in Masked-Action Environments via an Exact Blackjack Oracle"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18642"
published: "2026-03-20"
fetched: "2026-03-20T12:14:01.709327"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Evaluating Model-Free Policy Optimization in Masked-Action Environments via an Exact Blackjack Oracle
View PDF HTML (experimental)Abstract:Infinite-shoe casino blackjack provides a rigorous, exactly verifiable benchmark for discrete stochastic control under dynamically masked actions. Under a fixed Vegas-style ruleset (S17, 3:2 payout, dealer peek, double on any two, double after split, resplit to four), an exact dynamic programming (DP) oracle was derived over 4,600 canonical decision cells. This oracle yielded ground-truth action values, optimal policy labels, and a theoretical expected value (EV) of -0.00161 per hand. To evaluate sample-efficient policy recovery, three model-free optimizers were trained via simulated interaction: masked REINFORCE with a per-cell exponential moving average baseline, simultaneous perturbation stochastic approximation (SPSA), and the cross-entropy method (CEM). REINFORCE was the most sample-efficient, achieving a 46.37% action-match rate and an EV of -0.04688 after 10^6 hands, outperforming CEM (39.46%, 7.5x10^6 evaluations) and SPSA (38.63%, 4.8x10^6 evaluations). However, all methods exhibited substantial cell-conditional regret, indicating persistent policy-level errors despite smooth reward convergence. This gap shows that tabular environments with severe state-visitation sparsity and dynamic action masking remain challenging, while aggregate reward curves can obscure critical local failures. As a negative control, it was proven and empirically confirmed that under i.i.d. draws without counting, optimal bet sizing collapses to the table minimum. In addition, larger wagers strictly increased volatility and ruin without improving expectation. These results highlight the need for exact oracles and negative controls to avoid mistaking stochastic variability for genuine algorithmic performance.
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
