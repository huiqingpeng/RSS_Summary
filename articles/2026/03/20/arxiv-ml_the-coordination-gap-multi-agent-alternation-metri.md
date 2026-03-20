---
title: "The Coordination Gap: Multi-Agent Alternation Metrics for Temporal Fairness in Repeated Games"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.05789"
published: "2026-03-20"
fetched: "2026-03-20T15:04:22.751327"
---

Computer Science > Multiagent Systems
[Submitted on 6 Mar 2026 (v1), last revised 19 Mar 2026 (this version, v3)]
Title:The Coordination Gap: Multi-Agent Alternation Metrics for Temporal Fairness in Repeated Games
View PDF HTML (experimental)Abstract:Multi-agent coordination dilemmas expose a fundamental tension between individual optimization and collective welfare, yet characterizing such coordination requires metrics sensitive to temporal structure and collective dynamics. As a diagnostic testbed, we study a BoE-derived multi-agent variant of the Battle of the Exes, formalizing it as a Markov game in which turn-taking emerges as a periodic coordination regime. Conventional outcome-based metrics (e.g., efficiency and min/max fairness) are temporally blind (they cannot distinguish structured alternation from monopolistic or random access patterns) and fairness ratios lose discriminative power as n grows, obscuring inequities.
To address this limitation, we introduce Perfect Alternation (PA) as a reference coordination regime and propose six novel Alternation (ALT) metrics designed as temporally sensitive observables of coordination quality. Using Q-learning agents as a minimal adaptive diagnostic baseline, and comparing against random-policy null processes, we uncover a clear measurement failure: despite exhibiting deceptively high traditional metrics (e.g., reward fairness often exceeding 0.9), learned policies perform up to 81% below random baselines under ALT-variant evaluation, a deficit already present in the two-agent case and intensifying as n grows.
These results demonstrate, in this setting, that high aggregate payoffs can coexist with poor temporal coordination, and that conventional metrics may severely mischaracterize emergent dynamics. Our findings underscore the necessity of temporally aware observables for analyzing coordination in multi-agent games and highlight random-policy baselines as essential null processes for interpreting coordination outcomes relative to chance-level behavior.
Submission history
From: Nikolaos Papadopoulos [view email][v1] Fri, 6 Mar 2026 00:43:53 UTC (14,814 KB)
[v2] Tue, 10 Mar 2026 19:21:45 UTC (14,793 KB)
[v3] Thu, 19 Mar 2026 02:04:50 UTC (7,444 KB)
Current browse context:
cs.MA
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
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs.
