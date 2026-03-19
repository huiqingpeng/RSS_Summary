---
title: "SCALE:Scalable Conditional Atlas-Level Endpoint transport for virtual cell perturbation prediction"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.17380"
published: "2026-03-19"
fetched: "2026-03-19T12:10:45.752704"
---

Computer Science > Machine Learning
[Submitted on 18 Mar 2026]
Title:SCALE:Scalable Conditional Atlas-Level Endpoint transport for virtual cell perturbation prediction
View PDF HTML (experimental)Abstract:Virtual cell models aim to enable in silico experimentation by predicting how cells respond to genetic, chemical, or cytokine perturbations from single-cell measurements. In practice, however, large-scale perturbation prediction remains constrained by three coupled bottlenecks: inefficient training and inference pipelines, unstable modeling in high-dimensional sparse expression space, and evaluation protocols that overemphasize reconstruction-like accuracy while underestimating biological fidelity. In this work we present a specialized large-scale foundation model SCALE for virtual cell perturbation prediction that addresses the above limitations jointly. First, we build a BioNeMo-based training and inference framework that substantially improves data throughput, distributed scalability, and deployment efficiency, yielding 12.51* speedup on pretrain and 1.29* on inference over the prior SOTA pipeline under matched system settings. Second, we formulate perturbation prediction as conditional transport and implement it with a set-aware flow architecture that couples LLaMA-based cellular encoding with endpoint-oriented supervision. This design yields more stable training and stronger recovery of perturbation effects. Third, we evaluate the model on Tahoe-100M using a rigorous cell-level protocol centered on biologically meaningful metrics rather than reconstruction alone. On this benchmark, our model improves PDCorr by 12.02% and DE Overlap by 10.66% over STATE. Together, these results suggest that advancing virtual cells requires not only better generative objectives, but also the co-design of scalable infrastructure, stable transport modeling, and biologically faithful evaluation.
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
