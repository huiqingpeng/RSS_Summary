---
title: "Delightful Distributed Policy Gradient"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.20521"
published: "2026-03-24"
fetched: "2026-03-25T07:10:45.931352"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Delightful Distributed Policy Gradient
View PDF HTML (experimental)Abstract:Distributed reinforcement learning trains on data from stale, buggy, or mismatched actors, producing actions with high surprisal (negative log-probability) under the learner's policy. The core difficulty is not surprising data per se, but \emph{negative learning from surprising data}. High-surprisal failures can dominate the update direction despite carrying little useful signal, while high-surprisal successes reveal opportunities the current policy would otherwise miss. The \textit{Delightful Policy Gradient} (DG) separates these cases by gating each update with delight, the product of advantage and surprisal, suppressing rare failures and amplifying rare successes without behavior probabilities. Under contaminated sampling, the cosine similarity between the standard policy gradient and the true gradient collapses, while DG's grows as the policy improves. No sign-blind reweighting, including exact importance sampling, can reproduce this effect. On MNIST with simulated staleness, DG without off-policy correction outperforms importance-weighted PG with exact behavior probabilities. On a transformer sequence task with staleness, actor bugs, reward corruption, and rare discovery, DG achieves roughly $10{\times}$ lower error. When all four frictions act simultaneously, its compute advantage is order-of-magnitude and grows with task complexity.
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
