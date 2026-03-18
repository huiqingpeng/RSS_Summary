---
title: "Efficient Federated Conformal Prediction with Group-Conditional Guarantees"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.14198"
published: "2026-03-18"
fetched: "2026-03-18T17:06:46.557026"
---

Computer Science > Machine Learning
[Submitted on 15 Mar 2026 (v1), last revised 17 Mar 2026 (this version, v2)]
Title:Efficient Federated Conformal Prediction with Group-Conditional Guarantees
View PDF HTML (experimental)Abstract:Deploying trustworthy AI systems requires principled uncertainty quantification. Conformal prediction (CP) is a widely used framework for constructing prediction sets with distribution-free coverage guarantees. In many practical settings, including healthcare, finance, and mobile sensing, the calibration data required for CP are distributed across multiple clients, each with its own local data distribution. In this federated setting, data can often be partitioned into, potentially overlapping, groups, which may reflect client-specific strata or cross-cutting attributes such as demographic or semantic categories. We propose group-conditional federated conformal prediction (GC-FCP), a novel protocol that provides group-conditional coverage guarantees. GC-FCP constructs mergeable, group-stratified coresets from local calibration scores, enabling clients to communicate compact weighted summaries that support efficient aggregation and calibration at the server. Experiments on synthetic and real-world datasets validate the performance of GC-FCP compared to centralized calibration baselines.
Submission history
From: Wen Haifeng [view email][v1] Sun, 15 Mar 2026 03:17:14 UTC (1,122 KB)
[v2] Tue, 17 Mar 2026 12:10:46 UTC (1,123 KB)
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
