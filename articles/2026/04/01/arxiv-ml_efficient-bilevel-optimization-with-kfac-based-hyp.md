---
title: "Efficient Bilevel Optimization with KFAC-Based Hypergradients"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.29108"
published: "2026-04-01"
fetched: "2026-04-02T07:15:24.056202"
---

Computer Science > Machine Learning
[Submitted on 31 Mar 2026]
Title:Efficient Bilevel Optimization with KFAC-Based Hypergradients
View PDF HTML (experimental)Abstract:Bilevel optimization (BO) is widely applicable to many machine learning problems. Scaling BO, however, requires repeatedly computing hypergradients, which involves solving inverse Hessian-vector products (IHVPs). In practice, these operations are often approximated using crude surrogates such as one-step gradient unrolling or identity/short Neumann expansions, which discard curvature information. We build on implicit function theorem-based algorithms and propose to incorporate Kronecker-factored approximate curvature (KFAC), yielding curvature-aware hypergradients with a better performance efficiency trade-off than Conjugate Gradient (CG) or Neumann methods and consistently outperforming unrolling. We evaluate this approach across diverse tasks, including meta-learning and AI safety problems. On models up to BERT, we show that curvature information is valuable at scale, and KFAC can provide it with only modest memory and runtime overhead. Our implementation is available at this https URL.
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
