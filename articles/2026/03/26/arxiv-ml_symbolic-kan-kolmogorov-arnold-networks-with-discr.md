---
title: "Symbolic--KAN: Kolmogorov-Arnold Networks with Discrete Symbolic Structure for Interpretable Learning"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.23854"
published: "2026-03-26"
fetched: "2026-03-27T07:17:44.620972"
---

Computer Science > Machine Learning
[Submitted on 25 Mar 2026]
Title:Symbolic--KAN: Kolmogorov-Arnold Networks with Discrete Symbolic Structure for Interpretable Learning
View PDFAbstract:Symbolic discovery of governing equations is a long-standing goal in scientific machine learning, yet a fundamental trade-off persists between interpretability and scalable learning. Classical symbolic regression methods yield explicit analytic expressions but rely on combinatorial search, whereas neural networks scale efficiently with data and dimensionality but produce opaque representations. In this work, we introduce Symbolic Kolmogorov-Arnold Networks (Symbolic-KANs), a neural architecture that bridges this gap by embedding discrete symbolic structure directly within a trainable deep network. Symbolic-KANs represent multivariate functions as compositions of learned univariate primitives applied to learned scalar projections, guided by a library of analytic primitives, hierarchical gating, and symbolic regularization that progressively sharpens continuous mixtures into one-hot selections. After gated training and discretization, each active unit selects a single primitive and projection direction, yielding compact closed-form expressions without post-hoc symbolic fitting. Symbolic-KANs further act as scalable primitive discovery mechanisms, identifying the most relevant analytic components that can subsequently inform candidate libraries for sparse equation-learning methods. We demonstrate that Symbolic-KAN reliably recovers correct primitive terms and governing structures in data-driven regression and inverse dynamical systems. Moreover, the framework extends to forward and inverse physics-informed learning of partial differential equations, producing accurate solutions directly from governing constraints while constructing compact symbolic representations whose selected primitives reflect the true analytical structure of the underlying equations. These results position Symbolic-KAN as a step toward scalable, interpretable, and mechanistically grounded learning of governing laws.
Submission history
From: Salah A Faroughi [view email][v1] Wed, 25 Mar 2026 02:31:13 UTC (3,264 KB)
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
