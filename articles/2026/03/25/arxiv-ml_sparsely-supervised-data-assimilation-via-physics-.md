---
title: "Sparsely-Supervised Data Assimilation via Physics-Informed Schr\"odinger Bridge"
source: "arXiv Machine Learning"
url: "https://arxiv.org/abs/2603.22319"
published: "2026-03-25"
fetched: "2026-03-26T07:10:45.526435"
---

Computer Science > Machine Learning
[Submitted on 20 Mar 2026]
Title:Sparsely-Supervised Data Assimilation via Physics-Informed Schrödinger Bridge
View PDF HTML (experimental)Abstract:Data assimilation (DA) for systems governed by partial differential equations (PDE) aims to reconstruct full spatiotemporal fields from sparse high-fidelity (HF) observations while respecting physical constraints. While full-grid low-fidelity (LF) simulations provide informative priors in multi-fidelity settings, recovering an HF field consistent with both sparse observations and the governing PDE typically requires per-instance test-time optimization, which becomes a major bottleneck in time-critical applications. To alleviate this, amortized reconstruction using generative models has recently been proposed; however, such approaches rely on full-field HF supervision during training, which is often impractical in real-world settings. From a more realistic perspective, we propose the Physics-Informed Conditional Schrödinger Bridge (PICSB), which transports an informative LF prior toward an observation-conditioned HF posterior without any additional inference-time guidance. To enable learning without HF endpoints, PICSB employs an iterative surrogate-endpoint refresh scheme, and directly incorporates PDE residuals into the training objective while enforcing observations via hard conditioning throughout sampling. Experiments on fluid PDE benchmarks demonstrate that PICSB enables extremely fast spatiotemporal field reconstruction while maintaining competitive accuracy under sparse HF supervision.
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
