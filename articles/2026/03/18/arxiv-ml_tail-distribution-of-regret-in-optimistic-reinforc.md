---
title: "Tail Distribution of Regret in Optimistic Reinforcement Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2511.18247"
published: "2026-03-18"
fetched: "2026-03-18T17:03:10.011856"
---

Computer Science > Machine Learning
[Submitted on 23 Nov 2025 (v1), last revised 16 Mar 2026 (this version, v3)]
Title:Tail Distribution of Regret in Optimistic Reinforcement Learning
View PDF HTML (experimental)Abstract:We derive instance-dependent tail bounds for the regret of optimism-based reinforcement learning in finite-horizon tabular Markov decision processes with unknown transition dynamics. We first study a UCBVI-type (model-based) algorithm and characterize the tail distribution of the cumulative regret $R_K$ over $K$ episodes via explicit bounds on $P(R_K \ge x)$, going beyond analyses limited to $E[R_K]$ or a single high-probability quantile. We analyze two natural exploration-bonus schedules for UCBVI: (i) a $K$-dependent scheme that explicitly incorporates the total number of episodes $K$, and (ii) a $K$-independent (anytime) scheme that depends only on the current episode index. We then complement the model-based results with an analysis of optimistic Q-learning (model-free) under a $K$-dependent bonus schedule.
Across both the model-based and model-free settings, we obtain upper bounds on $P(R_K \ge x)$ with a distinctive two-regime structure: a sub-Gaussian tail starting from an instance-dependent scale up to a transition threshold, followed by a sub-Weibull tail beyond that point. We further derive corresponding instance-dependent bounds on the expected regret $E[R_K]$. The proposed algorithms depend on a tuning parameter $\alpha$, which balances the expected regret and the range over which the regret exhibits sub-Gaussian decay.
Submission history
From: Sajad Khodadadian [view email][v1] Sun, 23 Nov 2025 02:23:09 UTC (18 KB)
[v2] Mon, 26 Jan 2026 04:16:22 UTC (20 KB)
[v3] Mon, 16 Mar 2026 19:23:19 UTC (27 KB)
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
