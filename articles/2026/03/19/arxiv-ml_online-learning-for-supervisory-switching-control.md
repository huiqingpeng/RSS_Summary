---
title: "Online Learning for Supervisory Switching Control"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14762"
published: "2026-03-19"
fetched: "2026-03-19T14:20:04.214238"
---

Mathematics > Optimization and Control
[Submitted on 16 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Online Learning for Supervisory Switching Control
View PDF HTML (experimental)Abstract:We study supervisory switching control for partially-observed linear dynamical systems. The objective is to identify and deploy the best controller for the unknown system by periodically selecting among a collection of $N$ candidate controllers, some of which may destabilize the underlying system. While classical estimator-based supervisory control guarantees asymptotic stability, it lacks quantitative finite-time performance bounds. Conversely, current non-asymptotic methods in both online learning and system identification require restrictive assumptions that are incompatible in a control setting, such as system stability, which preclude testing potentially unstable controllers. To bridge this gap, we propose a novel, non-asymptotic analysis of supervisory control that adapts multi-armed bandit algorithms to a control-theoretic setting. The proposed data-driven algorithm evaluates candidate controllers via scoring criteria that leverage system observability to isolate the effects of state history, enabling both detection of destabilizing controllers and accurate system identification. We present two algorithmic variants with dimension-free, finite-time guarantees, where each identifies the most suitable controller in $\mathcal{O}(N \log N)$ steps, while simultaneously achieving finite $L_2$-gain with respect to system disturbances.
Submission history
From: Haoyuan Sun [view email][v1] Mon, 16 Mar 2026 02:52:09 UTC (36 KB)
[v2] Tue, 17 Mar 2026 21:11:18 UTC (36 KB)
Current browse context:
math.OC
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
