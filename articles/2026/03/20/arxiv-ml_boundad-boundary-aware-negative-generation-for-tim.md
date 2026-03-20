---
title: "BoundAD: Boundary-Aware Negative Generation for Time Series Anomaly Detection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.18111"
published: "2026-03-20"
fetched: "2026-03-20T12:07:48.036535"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:BoundAD: Boundary-Aware Negative Generation for Time Series Anomaly Detection
View PDF HTML (experimental)Abstract:Contrastive learning methods for time series anomaly detection (TSAD) heavily depend on the quality of negative sample construction. However, existing strategies based on random perturbations or pseudo-anomaly injection often struggle to simultaneously preserve temporal semantic consistency and provide effective decision-boundary supervision. Most existing methods rely on prior anomaly injection, while overlooking the potential of generating hard negatives near the data manifold boundary directly from normal samples themselves. To address this issue, we propose a reconstruction-driven boundary negative generation framework that automatically constructs hard negatives through the reconstruction process of normal samples. Specifically, the method first employs a reconstruction network to capture normal temporal patterns, and then introduces a reinforcement learning strategy to adaptively adjust the optimization update magnitude according to the current reconstruction state. In this way, boundary-shifted samples close to the normal data manifold can be induced along the reconstruction trajectory and further used for subsequent contrastive representation learning. Unlike existing methods that depend on explicit anomaly injection, the proposed framework does not require predefined anomaly patterns, but instead mines more challenging boundary negatives from the model's own learning dynamics. Experimental results show that the proposed method effectively improves anomaly representation learning and achieves competitive detection performance on the current dataset.
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
