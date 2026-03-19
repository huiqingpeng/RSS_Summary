---
title: "Den-TP: A Density-Balanced Data Curation and Evaluation Framework for Trajectory Prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2409.17385"
published: "2026-03-19"
fetched: "2026-03-19T13:18:07.203360"
---

Computer Science > Machine Learning
[Submitted on 25 Sep 2024 (v1), last revised 18 Mar 2026 (this version, v4)]
Title:Den-TP: A Density-Balanced Data Curation and Evaluation Framework for Trajectory Prediction
View PDF HTML (experimental)Abstract:Trajectory prediction in autonomous driving has traditionally been studied from a model-centric perspective. However, existing datasets exhibit a strong long-tail distribution in scenario density, where common low-density cases dominate and safety-critical high-density cases are severely underrepresented. This imbalance limits model robustness and hides failure modes when standard evaluations average errors across all scenarios. We revisit trajectory prediction from a data-centric perspective and present Den-TP, a framework for density-aware dataset curation and evaluation. Den-TP first partitions data into density-conditioned regions using agent count as a dataset-agnostic proxy for interaction complexity. It then applies a gradient-based submodular selection objective to choose representative samples within each region while explicitly rebalancing across densities. The resulting subset reduces the dataset size by 50\% yet preserves overall performance and significantly improves robustness in high-density scenarios. We further introduce density-conditioned evaluation protocols that reveal long-tail failure modes overlooked by conventional metrics. Experiments on Argoverse 1 and 2 with state-of-the-art models show that robust trajectory prediction depends not only on data scale, but also on balancing scenario density.
Submission history
From: Ruining Yang [view email][v1] Wed, 25 Sep 2024 22:00:11 UTC (1,015 KB)
[v2] Thu, 20 Mar 2025 03:32:59 UTC (582 KB)
[v3] Tue, 30 Sep 2025 03:58:18 UTC (728 KB)
[v4] Wed, 18 Mar 2026 17:31:09 UTC (405 KB)
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
