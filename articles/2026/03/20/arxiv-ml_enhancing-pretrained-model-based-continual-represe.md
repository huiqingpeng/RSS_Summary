---
title: "Enhancing Pretrained Model-based Continual Representation Learning via Guided Random Projection"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.19145"
published: "2026-03-20"
fetched: "2026-03-20T13:05:45.222559"
---

Computer Science > Machine Learning
[Submitted on 19 Mar 2026]
Title:Enhancing Pretrained Model-based Continual Representation Learning via Guided Random Projection
View PDF HTML (experimental)Abstract:Recent paradigms in Random Projection Layer (RPL)-based continual representation learning have demonstrated superior performance when building upon a pre-trained model (PTM). These methods insert a randomly initialized RPL after a PTM to enhance feature representation in the initial stage. Subsequently, a linear classification head is used for analytic updates in the continual learning stage. However, under severe domain gaps between pre-trained representations and target domains, a randomly initialized RPL exhibits limited expressivity under large domain shifts. While largely scaling up the RPL dimension can improve expressivity, it also induces an ill-conditioned feature matrix, thereby destabilizing the recursive analytic updates of the linear head. To this end, we propose the Stochastic Continual Learner with MemoryGuard Supervisory Mechanism (SCL-MGSM). Unlike random initialization, MGSM constructs the projection layer via a principled, data-guided mechanism that progressively selects target-aligned random bases to adapt the PTM representation to downstream tasks. This facilitates the construction of a compact yet expressive RPL while improving the numerical stability of analytic updates. Extensive experiments on multiple exemplar-free Class Incremental Learning (CIL) benchmarks demonstrate that SCL-MGSM achieves superior performance compared to state-of-the-art methods.
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
