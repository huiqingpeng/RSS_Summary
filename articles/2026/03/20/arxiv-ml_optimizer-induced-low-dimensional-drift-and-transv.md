---
title: "Optimizer-Induced Low-Dimensional Drift and Transverse Dynamics in Transformer Training"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.23696"
published: "2026-03-20"
fetched: "2026-03-20T14:11:42.641986"
---

Computer Science > Machine Learning
[Submitted on 27 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v3)]
Title:Optimizer-Induced Low-Dimensional Drift and Transverse Dynamics in Transformer Training
View PDF HTML (experimental)Abstract:We analyze cumulative parameter trajectories of transformer training under AdamW and identify a dominant low-dimensional drift direction ("backbone") that captures 60--80% of long-horizon displacement from initialization. This direction is highly stable over rolling training windows yet reorients gradually across phases, particularly following objective reweighting. Per-batch gradients exhibit near-noise-floor alignment with the backbone, whereas optimizer-integrated updates align strongly with it, indicating that the structure emerges from accumulated optimizer dynamics rather than instantaneous gradient geometry.
Replacing AdamW with SGD-family optimizers eliminates this structure, and reducing $\beta_2$ smoothly degrades backbone dominance and reheating recoverability. Reheating experiments show that transverse probe modes can be transiently re-excited without substantially altering accumulated backbone drift.
These results provide a trajectory-level characterization of optimizer-induced geometric structure in transformer training and shift attention from instantaneous gradient properties to cumulative update dynamics.
Submission history
From: Yongzhong Xu [view email][v1] Fri, 27 Feb 2026 05:53:25 UTC (67 KB)
[v2] Mon, 2 Mar 2026 06:00:21 UTC (78 KB)
[v3] Wed, 18 Mar 2026 21:53:04 UTC (79 KB)
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
