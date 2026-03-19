---
title: "Learning Adaptive Distribution Alignment with Neural Characteristic Function for Graph Domain Adaptation"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2602.10489"
published: "2026-03-19"
fetched: "2026-03-19T14:11:38.064524"
---

Computer Science > Machine Learning
[Submitted on 11 Feb 2026 (v1), last revised 18 Mar 2026 (this version, v2)]
Title:Learning Adaptive Distribution Alignment with Neural Characteristic Function for Graph Domain Adaptation
View PDF HTML (experimental)Abstract:Graph Domain Adaptation (GDA) transfers knowledge from labeled source graphs to unlabeled target graphs but is challenged by complex, multi-faceted distributional shifts. Existing methods attempt to reduce distributional shifts by aligning manually selected graph elements (e.g., node attributes or structural statistics), which typically require manually designed graph filters to extract relevant features before alignment. However, such approaches are inflexible: they rely on scenario-specific heuristics, and struggle when dominant discrepancies vary across transfer scenarios. To address these limitations, we propose \textbf{ADAlign}, an Adaptive Distribution Alignment framework for GDA. Unlike heuristic methods, ADAlign requires no manual specification of alignment criteria. It automatically identifies the most relevant discrepancies in each transfer and aligns them jointly, capturing the interplay between attributes, structures, and their dependencies. This makes ADAlign flexible, scenario-aware, and robust to diverse and dynamically evolving shifts. To enable this adaptivity, we introduce the Neural Spectral Discrepancy (NSD), a theoretically principled parametric distance that provides a unified view of cross-graph shifts. NSD leverages neural characteristic function in the spectral domain to encode feature-structure dependencies of all orders, while a learnable frequency sampler adaptively emphasizes the most informative spectral components for each task via minimax paradigm. Extensive experiments on 10 datasets and 16 transfer tasks show that ADAlign not only outperforms state-of-the-art baselines but also achieves efficiency gains with lower memory usage and faster training.
Submission history
From: Wei Chen [view email][v1] Wed, 11 Feb 2026 03:48:04 UTC (1,794 KB)
[v2] Wed, 18 Mar 2026 08:03:42 UTC (1,794 KB)
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
