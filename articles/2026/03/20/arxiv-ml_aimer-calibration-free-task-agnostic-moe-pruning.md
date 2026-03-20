---
title: "AIMER: Calibration-Free Task-Agnostic MoE Pruning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18492"
published: "2026-03-20"
fetched: "2026-03-20T12:12:13.355830"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:AIMER: Calibration-Free Task-Agnostic MoE Pruning
View PDF HTML (experimental)Abstract:Mixture-of-Experts (MoE) language models increase parameter capacity without proportional per-token compute, but the deployment still requires storing all experts, making expert pruning important for reducing memory and serving overhead. Existing task-agnostic expert pruning methods are typically calibration-dependent: they estimate expert importance from routing or activation statistics on a calibration set, which makes pruning outcomes sensitive to the choice of calibration set and adds substantial preprocessing cost. We introduce AIMER (\textbf{A}bsolute mean over root mean square \textbf{IM}portance for \textbf{E}xpert \textbf{R}anking), a simple calibration-free criterion that yields clear within-layer score separation and distinct expert stratification. Across 7B to 30B MoE language models at 25\% and 50\% pruning ratios over 16 benchmarks, AIMER consistently delivers competitive or stronger overall performance against state-of-the-art calibration-based expert pruning baselines with only 0.22--1.27 seconds for scoring the experts.
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
