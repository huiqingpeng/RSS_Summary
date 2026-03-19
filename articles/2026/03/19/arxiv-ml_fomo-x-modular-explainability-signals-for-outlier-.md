---
title: "FoMo X: Modular Explainability Signals for Outlier Detection Foundation Models"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17570"
published: "2026-03-19"
fetched: "2026-03-19T12:13:41.851567"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:FoMo X: Modular Explainability Signals for Outlier Detection Foundation Models
View PDF HTML (experimental)Abstract:Tabular foundation models, specifically Prior-Data Fitted Networks (PFNs), have revolutionized outlier detection (OD) by enabling unsupervised zero-shot adaptation to new datasets without training. However, despite their predictive power, these models typically function as opaque black boxes, outputting scalar outlier scores that lack the operational context required for safety-critical decision-making. Existing post-hoc explanation methods are often computationally prohibitive for real-time deployment or fail to capture the epistemic uncertainty inherent in zero-shot inference. In this work, we introduce FoMo-X, a modular framework that equips OD foundation models with intrinsic, lightweight diagnostic capabilities. We leverage the insight that the frozen embeddings of a pretrained PFN backbone already encode rich, context-conditioned relational information. FoMo-X attaches auxiliary diagnostic heads to these embeddings, trained offline using the same generative simulator prior as the backbone. This allows us to distill computationally expensive properties, such as Monte Carlo dropout based epistemic uncertainty, into a deterministic, single-pass inference. We instantiate FoMo-X with two novel heads: a Severity Head that discretizes deviations into interpretable risk tiers, and an Uncertainty Head that provides calibrated confidence measures. Extensive evaluation on synthetic and real-world benchmarks (ADBench) demonstrates that FoMo-X recovers ground-truth diagnostic signals with high fidelity and negligible inference overhead. By bridging the gap between foundation model performance and operational explainability, FoMo-X offers a scalable path toward trustworthy, zero-shot outlier detection.
Submission history
From: Simon Klüttermann [view email][v1] Wed, 18 Mar 2026 10:22:51 UTC (3,081 KB)
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
