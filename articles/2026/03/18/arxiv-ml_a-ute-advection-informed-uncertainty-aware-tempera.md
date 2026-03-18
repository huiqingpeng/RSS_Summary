---
title: "A-UTE: Advection Informed, Uncertainty Aware Temperature Emulator"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2410.21657"
published: "2026-03-18"
fetched: "2026-03-18T17:08:53.264839"
---

Physics > Atmospheric and Oceanic Physics
[Submitted on 29 Oct 2024 (v1), last revised 16 Mar 2026 (this version, v5)]
Title:A-UTE: Advection Informed, Uncertainty Aware Temperature Emulator
View PDF HTML (experimental)Abstract:Physics-based Earth system models (ESMs) are essential for attributing climate change and generating scenario projections, yet their reliance on high-resolution numerical integration makes multi-decadal experiments expensive. In parallel, deep learning has delivered strong gains in short-range weather forecasting; however, auto-regressive roll-outs can accumulate error and become unstable when extended to decade-scale climate emulation. We introduce A-UTE: Advection Informed, Uncertainty Aware Temperature Emulator, aimed at stable multi-year emulation across heterogeneous climate models and grid resolutions. A-UTE is trained on various physics-based models at varying spatial resolutions to emulate temperature fields over a 10-year horizon. A-UTE formulates climate emulation as a forward-time stochastic dynamical system. We propose an auto-regressive ODE-SDE surrogate in which transport dynamics are constrained by an advection consistent ODE component, while a learned neural SDE term models coarse-grained variability and cross-model discrepancy at monthly resolution. We train A-UTE under negative log-likelihood objective for principled uncertainty estimates and probabilistic evaluation. Experiments across 20 climate models show that A-UTE improves long roll-out stability and accuracy relative to relevant baselines, advancing data-driven climate emulation with explicit physical structure and uncertainty-aware predictions.
Submission history
From: Hira Saleem [view email][v1] Tue, 29 Oct 2024 01:53:40 UTC (3,279 KB)
[v2] Wed, 30 Oct 2024 05:33:12 UTC (1,608 KB)
[v3] Mon, 29 Sep 2025 00:21:49 UTC (5,304 KB)
[v4] Mon, 6 Oct 2025 22:35:00 UTC (5,304 KB)
[v5] Mon, 16 Mar 2026 23:08:43 UTC (14,309 KB)
Current browse context:
physics.ao-ph
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
